import csv

class CSVReader:
    @staticmethod
    def read(file_path):
        with open(file_path, newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
