import json
import os
import sys
from functools import reduce

pathToFile = os.getcwd()
pathToFile = os.path.join(pathToFile, sys.argv[1])
with open(pathToFile + ".ipynb", 'r') as file:
    fileData = json.load(file)

    #file data to słownik zawierający 1 parę klucz wartość
    #klucz to 'cells', wartość to tablica słowników będących poszczególnymi komórkami
    fileData["cells"] = list(map(lambda x: (x.update({"outputs": ""}), x)[1]
                    if x["cell_type"] == "code" else x, fileData["cells"]))

    #Najpierw mapujemy, aby usunąć wyjście, a potem reduce, aby usunąć kod jeśli porzpednia komórka to markdown.
    #"# Ä†wiczenie", to po zakodowaniu w json "# Ćwiczenie".

    fileData["cells"] = reduce(lambda x, y: (y.update({"source": ""}), x.append(y), [el for el in x])[2]
                    if len(x) > 0
                    and x[len(x) - 1]["cell_type"] == "markdown"
                    and str(x[len(x) - 1]["source"]).find("# Ä†wiczenie") > -1
                    and y["cell_type"] == "code"
                    else (x.append(y), [el for el in x])[1], fileData["cells"], [])

    with open(pathToFile + ".czysty.ipynb", 'w') as result:
        json.dump(fileData, result, ensure_ascii=False)
