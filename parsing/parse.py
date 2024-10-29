import json

def make_dicts():
    dictionaries = {}

    for file_name in [
        "Rangjung Yeshe",
        "Ives Waldo",
        "Richard Barron",
        "84000",
        "Dan Martin",
        "Hopkins 2015",
        "Jim Valby",
        "Verbinator"
    ]:
        with open(file_name, mode="r", encoding="utf-8") as file:
            text = file.read()

        dictionaries[file_name] = ({line.split("|")[0]: line.split("|")[1] for line in text.split("\n") if "|" in line})


    with open("../json-data/dictionaries.json", mode="w", encoding="utf-8") as file:
        file.write(json.dumps(dictionaries, indent=4))


def make_big_dict():
    with open("../json-data/dictionaries.json", mode="r", encoding="utf-8") as file:
        dictionaries = json.load(file)



    dictionary = {}

    for i in range(len(dictionaries)):
        a_dict = list(dictionaries.values())[i]
        dict_name = list(dictionaries)[i]
        for word in a_dict:
            definition = a_dict[word]
            if not word in dictionary:
                dictionary[word] = ""

            dictionary[word] += f"*{dict_name}:\n{definition}\n\n"

    with open("../json-data/dictionary.json", mode="w", encoding="utf-8") as file:
        json.dump(dictionary, file, indent=4)


with open("../json-data/dictionary.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

print(data["sangs rgyas"])

# make_big_dict()