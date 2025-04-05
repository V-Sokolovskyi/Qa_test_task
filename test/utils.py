import os
import shutil
from faker import Faker
import logging
logger = logging.getLogger()


class Fake_data():

    def fake_data_create(self,folder_name, file_count):
        fake = Faker()
        for i in range(file_count):
            file_name =  f"{fake.word()}.txt"
            file_path = os.path.join(folder_name,file_name)
            with open(file_path, "w", encoding="utf=8")as f:
                f.write(fake.text())
            logger.info(f"Created file: {file_path}")

    def fake_data_delete(self,folder_path):
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path,item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
            logger.info(f"Removed file: {item_path}")

    def feke_folder_create(self, base_folder,count_folder, count_file_in_folder):
        fake = Faker()
        for i in range(count_folder):
            folder_name = fake.word()
            foldr_path = os.path.join(base_folder, folder_name)
            os.makedirs(foldr_path, exist_ok=True)
            Fake_data.fake_data_create(self,foldr_path, count_file_in_folder)
            logger.info(f"Created directory: {foldr_path}")


def count_of_files(folder):
    count = 0 
    for root, _, files in os.walk(folder):
        count += len(files)
    return count
