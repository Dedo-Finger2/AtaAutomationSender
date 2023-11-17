import os
import shutil


class FileManagment:

    @staticmethod
    def get_files(directory_path: str):
        all_items = os.listdir(directory_path)
        files = [file for file in all_items if os.path.isfile(os.path.join(directory_path, file))]
        return files
