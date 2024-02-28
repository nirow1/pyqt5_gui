import sys
import csv


def get_people_list():
    data = []
    with open('C:/Users/Radan Krch/Desktop/github_projects/pyqt5_gui/TableDatabase/Data/people.csv', 'r')as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append(row)
    return data


if __name__ == '__main__':
    for row in get_people_list():
        print(row[2])
