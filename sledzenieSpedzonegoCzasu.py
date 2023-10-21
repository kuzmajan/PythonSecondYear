# Użyta struktura danych: w słowniku dla każdego klucza wartość jest listą,
# której pierwszy element to suma czasów, a każda kolejna wartość to dodany przez użytkownika czas
def addActivity(dict, name, time):          # Dodawanie aktywności do słownika
    if dict.get(name, 'error') != 'error':  # Jeśli nie ma w słowniku wartości, to dict.get zwróci 'error'
        dict[name].append(time)
        dict[name][0] += time
    else:
        dict[name] = [time]                 # Tworzenie nowej aktywności
        dict[name].append(time)


def showActivityTime(dict, name):           # Na pierwszym miejscu listy jest suma czasów dla danej aktywności
    if dict.get(name, 'error') == 'error':
        print("Nie ma takiej aktywności")
    else:
        print(dict[name][0])


def showTop3Activities(dict):
    lista = []                              # Tworzymy liste którą posortujemy, znajdziemy w niej najwięszke wartości
    for value, key in dict.items():
        lista.append([key, value])
    result = list(sorted(lista, key=lambda x: x[1][0]))     # Sortujemy według pierwszej wartości w liście- jest to suma czasów
    i = 0
    while (i < 3) and (i < len(result)):
        if result[i][0][0] > 0:
            print(result[i][1])                             # Druga wartość to nazwa aktywności
        i += 1


if __name__ == '__main__':
    dict = {'Oglądanie filmów': [0]}                        # Początkowow w słowniku znajduje się aktywność 'Oglądanie filmów'
    addActivity(dict, "Oglądanie filmów", 10)
    showActivityTime(dict, "Oglądanie filmów")
    addActivity(dict, "Nauka", 20)
    addActivity(dict, "Nauka", 30)
    addActivity(dict, "Pływanie", 100)
    showActivityTime(dict, "Nauka")
    showTop3Activities(dict)
