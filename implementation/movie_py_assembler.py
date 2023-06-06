from moviepy.editor import VideoFileClip, concatenate_videoclips
from interfaces.video_assembler import VideoAssembler
from config.config import Config
from utils.file_utility import FileUtility


class MoviePyAssembler(VideoAssembler):
    def __init__(self):
        super().__init__()

    def assemble(self, video_parts_path):
        video_parts = []
        for video_part_path in video_parts_path:
            video_parts.append(VideoFileClip(video_part_path))
        final_video = concatenate_videoclips(video_parts)
        final_video.write_videofile(Config.OUTPUT_VIDEO_FILE)
        FileUtility.delete_file_by_regex('image_*TEMP*')
        FileUtility.delete_file_by_regex('video_*TEMP*')
        return Config.OUTPUT_VIDEO_FILE
