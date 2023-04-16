import random
import time

import yaml

from distributor import ContentDistributor


class FileReader:

    def __init__(self, distributor: ContentDistributor) -> None:
        self._distributor = distributor

    @staticmethod
    def read_yaml() -> dict:
        with open('test_yaml_file.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        return data

    def get_data(self) -> list:
        data = self.read_yaml()

        data_list = []
        for key, value in data.items():
            s = f"{key}: {value}"
            data_list.append(s)

        data_list.sort()

        return data_list

    def forward(self) -> None:
        data = self.get_data()
        for message in data:
            self._distributor.set_message(message)
            time.sleep(random.randint(0, 1))
        self._distributor.set_message(None)
