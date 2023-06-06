import os
from elevenlabs import set_api_key, generate, save
from interfaces.text_to_speech import TTS
from utils.file_utility import FileUtility
from config.config import Config
from utils.global_media_handle import GlobalMediaHandle
from implementation.hashing import MD5
from utils.console_utility import Console


class ElevenLabsTTS(TTS):
    cache = FileUtility.load_json_file(Config.CACHE)

    def __init__(self):
        super().__init__()
        self.hash_fn = MD5()
        set_api_key(FileUtility.read_file_data(os.path.join('config', 'eleven_labs_api_key')))

    def generate_audio(self, text):
        hashed_text = self.hash_fn.hash(text)
        if hashed_text in self.cache['elevenlabs']:
            Console.info('Cached audio found -> ' + hashed_text)
            src_path = self.cache['elevenlabs'][hashed_text]
            dst_path = GlobalMediaHandle.get_next_audio_file_path()
            FileUtility.copy_file(src_path, dst_path)
            return dst_path
        Console.info('Sending eleven labs TTS request -> ' + hashed_text)
        audio = generate(text=text, voice=Config.ELEVEN_LABS_PREFERRED_VOICE)
        output_file = GlobalMediaHandle.get_next_audio_file_path()
        save(audio, output_file)
        self.cache['elevenlabs'][hashed_text] = output_file
        return output_file

    @staticmethod
    def save_cache():
        Console.info('Saving eleven labs cache')
        FileUtility.dump_json_file(Config.CACHE, ElevenLabsTTS.cache)
