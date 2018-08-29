import os
import csv_dict_writer
from datetime import datetime
import sys


def file_reader(path, files):
    for i in os.listdir(path):
        test = "{}/{}".format(path, i)
        if i.endswith('.txt'):
            files.append(os.path.join(path, i))
        elif os.path.isdir(test):
            files = file_reader(test, files)
    return files


def get_date():
    now = datetime.now()
    return '%002d-%002d-%004d_%02d-%02d-%02d' % (
        now.month, now.day, now.year, now.hour, now.minute, now.second)


def get_totals(text, dict):
    for word in text:
        if not word.isalpha():
            word = ''.join([i for i in word if i.isalpha() or i == "'"])
        if len(word) > 1 or word == "I" or word == "A" or word == "a":
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
    return dict


def narrow(dict):
    rank = sorted(dict.items(), key=lambda kv: kv[1])
    if len(rank) < 200:
        num = int(len(rank) * 0.66)
    else:
        num = len(rank) - 200
    rank = rank[num:len(rank) + 1]
    return rank


def open_files(files):
    dict = {}
    for file in files:
        with open(file, "r") as f:
            text = f.read()
        text = text.split()
        dict = get_totals(text, dict)
    rank = narrow(dict)
    return rank


def csv_writer(rank, path):
    data = ["Word,Total".split(",")]
    for key in rank:
        str = "{},{}".format(key[0], key[1])
        data.append(str.split(","))
    csv_dict_writer.run_csv_writer(data, path)


def get_path(folder):
    path = "{}/rank_results.csv".format(folder)
    if os.path.isfile(path):
        file = "rank_results_{}.csv".format(get_date())
        path = "{}/{}".format(folder, file)
    return path


def main():
    folder = sys.argv[1]
    files = []
    files = file_reader(folder, files)
    rank = open_files(files)
    path = get_path(folder)
    csv_writer(rank, path)


if __name__ == "__main__":
    main()
