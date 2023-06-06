import os
from utils.file_utility import FileUtility
from utils.general_utilities import GeneralUtility


class Config:
    INPUT_STORY = FileUtility.get_real_path(os.path.join(os.getcwd(), 'input', 'story.txt'))
    INPUT_CONCLUSION = FileUtility.get_real_path(os.path.join(os.getcwd(), 'input', 'conclusion.txt'))
    INPUT_INTRO_VIDEO = FileUtility.get_real_path(os.path.join(os.getcwd(), 'input', 'intro.mp4'))
    CURRENT_OUTPUT_DIR = FileUtility.get_real_path(os.path.join(os.getcwd(), 'output', GeneralUtility.get_date_time()))
    CACHE = FileUtility.get_real_path(os.path.join(os.getcwd(), 'config', 'cache.json'))
    TEMP_FILE = os.path.join(CURRENT_OUTPUT_DIR, 'temp.txt')
    MAX_SPLIT_LENGTH = 3000
    AUDIO_SEQUENCE_PREFIX = 'audio_'
    VIDEO_SEQUENCE_PREFIX = 'video_'
    IMAGE_SEQUENCE_PREFIX = 'image_'
    OUTPUT_VIDEO_FILE = os.path.join(CURRENT_OUTPUT_DIR, 'output.mp4')
    VIDEO_FPS = 60
    BING_IMAGE_CREATOR_RESULTS_LEN = 4
    IMAGE_RESOLUTION = (1920, 1080)
    IMAGE_PROMPT_MAX_MODIFIERS = 10
    ELEVEN_LABS_VOICES = [
        'Rachel',
        'Domi',
        'Bella',
        'Antoni',  # Pref 2
        'Elli',
        'Josh',  # Pref 1
        'Arnold',  # Pref 3
        'Adam',
        'Sam'
    ]
    ELEVEN_LABS_PREFERRED_VOICE = 'Josh'
