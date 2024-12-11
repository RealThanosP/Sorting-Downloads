import os
import shutil


class Sorter:
    '''Sorts a folder based on the file extensions in different folders'''
    def __init__(self, path):
        self.path = os.chdir(path)

    def create_folder_if_not_exists(self, extension):
        # os.splitext return "" when applied to a folder.
        # This check avoids the folders so chek_for_extension_folder 
        # is not throwing an error
        if not extension:
            return None

        if self.check_for_extension_folder(extension):
            return None
        # Makes a folder only when it doesn't already exist
        os.mkdir(f"{extension}")

    def check_for_extension_folder(self, extension):
        if not(extension in os.listdir(self.path)):
            return False
        return True

    def sort_files(self):
        '''Constantly runs on the folder to defaultly sort everything you move there'''
        
        for file in os.listdir(self.path):
            if not os.path.isfile(file):
                continue
            # Create the extension folders
            file_name, file_extension = os.path.splitext(file)
            self.create_folder_if_not_exists(file_extension)
            
            # Move the correct items to its correct location
            shutil.move(file, file_extension)



