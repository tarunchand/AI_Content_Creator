import warnings
import os
import shlex
from config.config import Config
from implementation.bing import BingImageGenerator
from implementation.eleven_labs_tts import ElevenLabsTTS
from implementation.movie_py_mixer import MoviePyMixer
from implementation.movie_py_assembler import MoviePyAssembler
from utils.file_utility import FileUtility
from utils.console_utility import Console

warnings.filterwarnings("ignore")
from implementation.chatgpt import ChatGPTParagraphSplitter, ChatGPTImagePromptGenerator


def generate_paragraph(input_text):
    Console.info('Generating Paragraphs')
    paragraph_splitter = ChatGPTParagraphSplitter(input_text)
    return paragraph_splitter.split_data()


def prompt_vi(paragraphs):
    if Console.ask('Would you like to verify/edit the paragraphs?(y/n)').lower() == 'y':
        paragraph_data = '\n\n'.join(paragraphs)
        FileUtility.write_file_data(Config.TEMP_FILE, paragraph_data)
        os.system('vi {}'.format(shlex.quote(Config.TEMP_FILE)))
        if Console.ask('Would you like to continue?(y/n)').lower() == 'y':
            paragraphs = FileUtility.read_file_data(Config.TEMP_FILE).split('\n\n')
        else:
            exit(0)
        FileUtility.delete_file(Config.TEMP_FILE)
    return paragraphs


def generate_image_prompts(paragraphs, total_images, person_name, conclusion):
    Console.info('Generating Image Prompts')
    image_prompt_generator = ChatGPTImagePromptGenerator(paragraphs)
    prompts, merged_paragraphs = image_prompt_generator.generate_prompt(total_images)
    merged_paragraphs.append([conclusion])
    if person_name is not None:
        prompts.append(person_name)
    else:
        new_prompt, _ = ChatGPTImagePromptGenerator(conclusion).generate_prompt(1)
        prompts.append(new_prompt[0])
    return prompts, merged_paragraphs


def generate_images(image_prompts):
    Console.info('Generating Images')
    generated_images = []
    image_generator = BingImageGenerator()
    i = 1
    n = len(image_prompts)
    for prompt in image_prompts:
        Console.info('Generating Image : ({}/{})'.format(i, n))
        generated_images.append(image_generator.generate_image(prompt))
        i += 1
    return generated_images


def generate_audio(merged_paragraphs):
    Console.info('Generating Audio')
    audio_generator = ElevenLabsTTS()
    generated_audio = []
    i = 1
    n = len(merged_paragraphs)
    for merged_paragraph in merged_paragraphs:
        audio_list = []
        Console.info('Generating Audio - Progress : ({}/{})'.format(i, n))
        for paragraph in merged_paragraph:
            audio_list.append(audio_generator.generate_audio(paragraph))
        generated_audio.append(audio_list)
        i += 1
    return generated_audio


def generate_video(generated_images, generated_audio):
    video_list = [Config.INPUT_INTRO_VIDEO]
    Console.info('Generating Video')
    video_mixer = MoviePyMixer()
    for i in range(0, len(generated_images)):
        image_pos = 0
        for audio_path in generated_audio[i]:
            image_path = os.path.join(generated_images[i], '{}.jpeg'.format(
                image_pos % Config.BING_IMAGE_CREATOR_RESULTS_LEN))
            video_list.append(video_mixer.convert(image_path, audio_path))
            image_pos += 1
    return video_list


def generate_final_video(video_list):
    Console.info('Generating Final Video')
    video_assembler = MoviePyAssembler()
    return video_assembler.assemble(video_list)


def main():
    FileUtility.create_directory(Config.CURRENT_OUTPUT_DIR)
    input_text = FileUtility.read_file_data(Config.INPUT_STORY)
    conclusion = FileUtility.read_file_data(Config.INPUT_CONCLUSION)
    person_name = None
    if Console.ask('Is this story about a famous person?(y/n)').lower() == 'y':
        person_name = Console.ask('Enter the name of the person')
    total_images = int(Console.ask('Enter the number of images requests to send : '))
    paragraphs = generate_paragraph(input_text)
    paragraphs = prompt_vi(paragraphs)
    image_prompts, merged_paragraphs = generate_image_prompts(paragraphs, total_images, person_name, conclusion)
    generated_images = generate_images(image_prompts)
    generated_audio = generate_audio(merged_paragraphs)
    video_list = generate_video(generated_images, generated_audio)
    final_video = generate_final_video(video_list)
    Console.info('Final Video : {}'.format(final_video))
    os.system('cvlc {}'.format(shlex.quote(final_video)))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, OSError, Exception) as ex:
        Console.error(ex)
    finally:
        ElevenLabsTTS.save_cache()
