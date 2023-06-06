from interfaces.visual_audio_mixer import VisualAudioMixer
from moviepy.editor import ImageClip, AudioFileClip
from utils.global_media_handle import GlobalMediaHandle
from config.config import Config


class MoviePyMixer(VisualAudioMixer):
    def __init__(self):
        super().__init__()

    def convert(self, image_path, audio_path):
        image_clip = ImageClip(image_path)
        audio_clip = AudioFileClip(audio_path)
        video_clip = image_clip.set_audio(audio_clip)
        video_clip.duration = audio_clip.duration
        video_clip.fps = Config.VIDEO_FPS
        output_path = GlobalMediaHandle.get_next_video_file_path()
        video_clip.write_videofile(output_path)
        return output_path
