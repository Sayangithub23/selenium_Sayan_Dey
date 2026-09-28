import configparser
import os

class ConfigReader:
    def __init__(self, file_path=None):
        file_path = file_path or os.path.join(os.path.dirname(__file__), "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get(self, section, option):
        return self.config.get(section, option)

    def get_int(self, section, option):
        return self.config.getint(section, option)

    def get_bool(self, section, option):
        return self.config.getboolean(section, option)
