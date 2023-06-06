import os
import glob
import json
import shutil


class FileUtility:

    @staticmethod
    def read_file_data(file_path):
        with open(file_path) as file:
            return file.read()

    @staticmethod
    def write_file_data(file_path, data):
        with open(file_path, 'w') as file:
            file.write(data)

    @staticmethod
    def create_directory(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def get_real_path(path):
        return os.path.realpath(path)

    @staticmethod
    def delete_file(file_path):
        os.remove(file_path)

    @staticmethod
    def delete_file_by_regex(regex):
        for filename in glob.glob(regex):
            os.remove(filename)

    @staticmethod
    def copy_file(src, dst):
        shutil.copy(src, dst)

    @staticmethod
    def load_json_file(file_path):
        return json.loads(FileUtility.read_file_data(file_path))

    @staticmethod
    def dump_json_file(file_path, data):
        with open(file_path, 'w') as outfile:
            json.dump(data, outfile)
