import os
from config.config import Config
from utils.file_utility import FileUtility


class GlobalMediaHandle:
    audio_file_prefix = os.path.join(Config.CURRENT_OUTPUT_DIR, Config.AUDIO_SEQUENCE_PREFIX)
    image_dir_prefix = os.path.join(Config.CURRENT_OUTPUT_DIR, Config.IMAGE_SEQUENCE_PREFIX)
    video_file_prefix = os.path.join(Config.CURRENT_OUTPUT_DIR, Config.VIDEO_SEQUENCE_PREFIX)
    current_audio_handle = 0
    current_image_handle = 0
    current_video_handle = 0

    @staticmethod
    def get_next_audio_file_path():
        GlobalMediaHandle.current_audio_handle += 1
        return GlobalMediaHandle.audio_file_prefix + str(GlobalMediaHandle.current_audio_handle) + '.mp3'

    @staticmethod
    def get_next_image_dir_path():
        GlobalMediaHandle.current_image_handle += 1
        res = GlobalMediaHandle.image_dir_prefix + str(GlobalMediaHandle.current_image_handle)
        FileUtility.create_directory(res)
        return res

    @staticmethod
    def get_next_video_file_path():
        GlobalMediaHandle.current_video_handle += 1
        return GlobalMediaHandle.video_file_prefix + str(GlobalMediaHandle.current_video_handle) + '.mp4'
