import random
from pathlib import Path
import os
import csv


def create_directories(current_path, input_data):
    countMonths = 0
    countTime = 0
    if input_data[0][0].find('-') == -1:
        months = [findOriginal(allMonthsShortcut, allMonths, input_data[0][0])]
    else:
        begin, end = input_data[0][0].split('-')[0], input_data[0][0].split('-')[1]
        months = findAll(allMonthsShortcut, allMonths, begin, end)
    current_path.mkdir()
    for month in months:
        current_path_month = Path(os.path.join(current_path, month))
        current_path_month.mkdir()
        if input_data[1][countMonths].find('-') == -1:
            daysOfTheWeek = [findOriginal(allDaysOfTheWeekShortcut, allDaysOfTheWeek, input_data[1][countMonths])]
        else:
            begin, end = input_data[1][countMonths].split('-')[0], input_data[1][countMonths].split('-')[1]
            daysOfTheWeek = findAll(allDaysOfTheWeekShortcut, allDaysOfTheWeek, begin, end)
        countMonths += 1
        for day in daysOfTheWeek:
            current_path_day = Path(os.path.join(current_path_month, day))
            current_path_day.mkdir()
            if countTime + 1 > len(input_data[2]):
                time = baseTimeOfTheDay
            else:
                time = findOriginal(allTimesOfTheDayShortuct, allTimesOfTheDay, input_data[2][countTime])
            current_path_time = Path(os.path.join(current_path_day, time))
            current_path_time.mkdir()
            current_path_txt = Path(os.path.join(current_path_time, 'Solutions.csv'))
            create_file(current_path_txt)
            countTime += 1


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


def findOriginal(shortcutList, originalList, el):
    i = 0
    while shortcutList[i] != el:
        i += 1
    return originalList[i]


def findAll(shortcutList, originalList, first, last):
    i = 0
    while shortcutList[i] != first:
        i += 1
    result = []
    while shortcutList[i - 1] != last:
        result.append(originalList[i])
        i += 1
    return result


if __name__ == '__main__':
    allMonths = ['Januray', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']
    allMonthsShortcut = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    allDaysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    allDaysOfTheWeekShortcut = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    baseTimeOfTheDay = 'Morning'
    allTimesOfTheDay = ['Morning', 'Evening']
    allTimesOfTheDayShortuct = ['m', 'e']
    firstRow = 'Model; Output value; Time of computation'
    models = ['A', 'B', 'C']

    inputData = [['Feb-Sep'], ['Tue-Fri', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                 ['m', 'm', 'e', 'e', 'm', 'e']]
    cPath = Path(os.getcwd())
    cPath = Path(os.path.join(cPath, "Solution"))
    create_directories(cPath, inputData)
    result_dictionary = {'A': 0, 'B': 0, 'C': 0}
    result_dictionary = summed_time_of_computation(cPath, result_dictionary)
    print(result_dictionary)