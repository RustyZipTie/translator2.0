from language.Dictionary import Dictionary

with open("../json-data/tibetan-wylie.json", mode="r", encoding="utf-8") as file:
    wylie = Dictionary(file)

with open("../json-data/dictionary.json", mode="r", encoding="utf-8") as file:
    main = Dictionary(file, pre_processing=lambda a: wylie.define_multi(a, "་"))

print(main.define("སངས་རྒྱlས་"))