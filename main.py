import json
import logging
from pathlib import Path
from os import path
import csv


def text_file(file_path):
    try:
        print(f'Inside file path, {file_path}')
        file_name = 'products'
        with open(str(file_path + '/') + str(file_name) + ".txt", "r") as file1:
            file_2 = file1.readlines()
        dict = {}
        for i in file_2:
            p = i.strip().split(':')
            if len(p) != 2:
                raise ValueError("Invalid format in line: {}".format(file_2))
            try:
                if dict.keys() == 'Null' or dict.keys() == '':
                    print('Keys cannot be null')
            except Exception as e:
                print(e)
                logging.info(e)
            try:
                if dict.values() == '' or dict.values() == 'Null':
                    print('Values cannot be null')
            except Exception as e:
                print(e)
                logging.info(e)
            key, value = p
            dict[key.strip()] = value.strip()
        output_file = json.dumps(dict, indent=4)
        print(output_file)
    except Exception as e:
        print(e)
        logging.info(e)

def csv_file(file_path):
    try:
        print(f'Inside file path, {file_path}')
        file_name = 'products'
        input_csv = file_path + '/' + file_name + '.csv'
        if path.exists(input_csv):
            try:
                with open(input_csv, 'r') as input_file:
                    csv_reader = csv.DictReader(input_file)
                    try:
                        data = list(csv_reader)
                        print(data)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        logging.info(e)



if __name__ == '__main__':
    file_path = Path('..').cwd().as_posix()
    text_file(file_path)
    csv_file(file_path)

