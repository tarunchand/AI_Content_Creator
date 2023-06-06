import os
from PIL import Image
from utils.file_utility import FileUtility
from interfaces.text_to_image import TTI
from BingImageCreator import ImageGen
from utils.global_media_handle import GlobalMediaHandle
from config.config import Config


class BingImageGenerator(TTI):
    def __init__(self):
        super().__init__()
        self.image_gen = ImageGen(auth_cookie=FileUtility.read_file_data(os.path.join('config', 'bing_auth_cookie')))

    def generate_image(self, prompt):
        links_of_images = self.image_gen.get_images(prompt)
        save_directory = GlobalMediaHandle.get_next_image_dir_path()
        self.image_gen.save_images(links_of_images, save_directory)
        self.resize_images(save_directory)
        return save_directory

    @staticmethod
    def resize_images(image_dir):
        for file in os.listdir(image_dir):
            with Image.open(os.path.join(image_dir, file)) as image:
                resized_image = image.resize(Config.IMAGE_RESOLUTION)
                resized_image.save(os.path.join(image_dir, file))
