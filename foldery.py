import random
from pathlib import Path
import os
import csv


def create_directories(current_path):
    current_path.mkdir()
    for month in months:
        current_path_month = Path(os.path.join(current_path, month))
        current_path_month.mkdir()
        for day in daysOfTheWeek:
            current_path_day = Path(os.path.join(current_path_month, day))
            current_path_day.mkdir()
            for time in timeOfTheDay:
                current_path_time = Path(os.path.join(current_path_day, time))
                current_path_time.mkdir()
                current_path_txt = Path(os.path.join(current_path_time, 'Solutions.csv'))
                create_file(current_path_txt)


def create_file(current_path):
    with open(current_path, 'w', newline='') as plik:
        writer = csv.writer(plik)
        writer.writerow([firstRow])
        second_row = ''
        x = random.randint(0, 2)
        y = str(random.randint(0, 1000))
        z = str(random.randint(0, 1000))
        second_row += models[x] + ';' + y + ';' + z + 's'
        writer.writerow([second_row])


def summed_time_of_computation(current_path, dictionary):
    for i in os.listdir(current_path):
        updated_path = Path(os.path.join(current_path, i))
        if updated_path.is_file():
            dictionary = adding_result(updated_path, dictionary)
        else:
            dictionary = summed_time_of_computation(updated_path, dictionary)
    return dictionary


def adding_result(path, dictionary):
    with open(path, 'r') as plik:
        line_count = 0
        reader = csv.reader(plik, delimiter=';')
        for row in reader:
            if line_count == 0:
                line_count += 1
            else:
                x = row[2].rstrip(row[2][-1])
                dictionary[row[0]] += int(x)
    return dictionary


if __name__ == '__main__':
    months = ['Januray', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    timeOfTheDay = ['Morning', 'Evening']
    firstRow = 'Model; Output value; Time of computation'
    models = ['A', 'B', 'C']

    cPath = Path(os.getcwd())
    cPath = Path(os.path.join(cPath, "Solution"))
    create_directories(cPath)
    result_dictionary = {'A': 0, 'B': 0, 'C': 0}
    result_dictionary = summed_time_of_computation(cPath, result_dictionary)
    print(result_dictionary)
