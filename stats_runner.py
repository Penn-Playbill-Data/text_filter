# Note - CSV writer functions present, but not active.
import csv
import csv_dict_writer
import word_counter
import os
import sys


def csv_reader(file):
    words = []
    if ".csv" in file:
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if row[0] != "Word":
                    words.append(row[0])
    return words


def create_list(words):
    lst = []
    for word in words:
        lst.append([word, 0, 0, 0])
    return lst


def get_text(words, files):
    stats = []
    for file in files:
        with open(file, "r") as f:
            text = f.read()
        text = text.split()
        stats.append(get_stats(words, text))
    return stats


def get_stats(words, text):
    stats = create_list(words)
    for word in text:
        if not word.isalpha():
            word = ''.join([i for i in word if i.isalpha() or i == "'"])
        for item in range(len(stats)):
            if word == stats[item][0]:
                stats[item][1] += 1
                stats[item][2] = len(text)
                stats[item][3] = float(stats[item][1]) / stats[item][2]
    return stats


def get_path(folder):
    path = "{}/stats_results.csv".format(folder)
    if os.path.isfile(path):
        file = "stats_results_{}.csv".format(word_counter.get_date())
        path = "{}/{}".format(folder, file)
    return path


def get_avg(stats):
    sum = 0
    avgs = []
    if len(stats) > 1:
        for i in range(len(stats[0])):
            for j in range(len(stats)):
                sum += stats[j][i][3]
                sum = sum / float(len(stats))
            avgs.append(sum)
    elif len(stats) == 1:
        for i in range(len(stats[0])):
            avgs.append(stats[0][i][3])
    return avgs


# Only prints the word and average percentage - good for comparisons
def csv_next_writer(stats, words, path):
    data = ["Word,Average Percentage".split(",")]
    avgs = get_avg(stats)
    for i in range(len(words)):
        if avgs[i] > 0.001:
            data.append("{},{}".format(words[i], str(avgs[i])).split(","))
    csv_dict_writer.run_csv_writer(data, path)


# Writes the total information for each file, is a bit clunky format wise
def csv_writer(stats, files, path):
    data = ["File,Word,Times Appeared,Total Words,Percentage".split(",")]
    for i in range(len(files)):
        for j in range(len(stats[i])):
            if stats[i][j][1] != 0:
                str = "{},{},{},{},{}".format(
                    files[i], stats[i][j][0],
                    stats[i][j][1], stats[i][j][2], stats[i][j][3])
                data.append(str.split(","))
    csv_dict_writer.run_csv_writer(data, path)


def avg_sum(avgs):
    sum = 0
    for avg in avgs:
        sum += avg
    # TODO finish


def main():
    file = sys.argv[1]
    folder = sys.argv[2]
    files = []
    files = word_counter.file_reader(folder, files)
    file = os.path.expanduser(file)
    path = get_path(os.path.expanduser(folder))
    words = csv_reader(file)
    stats = get_text(words, files)
    csv_next_writer(stats, words, path)


if __name__ == "__main__":
    main()
