import _io
import json
from typing import TextIO


class Dictionary:
    """
    a class to facilitate using a python dict as an actual dictionary
    """

    def __init__(self, data: dict | TextIO, pre_processing=lambda a: a):
        """
        either data or data_location must be specified
        :param data: a dict containing dictionary data in {word: definition} format, OR a file object pointing to a file with json data in the same format
        :param pre_processing: a function that is used to process all input to get_definition and get_nearest
        """
        if type(data) == _io.TextIOWrapper:
            self.__source = json.load(data)
        elif type(data) == dict:
            self.__source = data
        else:
            raise ValueError("arg data must be a file object or dict")

        self.__pre_processing = pre_processing

    def define(self, word: str, err=lambda a: f"<err>{a}d"):
        print("first,", word)
        processed = self.__pre_processing(word)
        print("second,", processed)
        if processed in self.__source:
            return self.__source[processed]
        else:
            return err(word)

    def define_multi(self, phrase: str, delimiter: str, joint=" ", err=lambda a: f"<err>{a}m"):
        print("pre_first,", phrase)
        processed = [self.__pre_processing(word) for word in phrase.split(delimiter)]
        print("pre_second,", processed)
        response = ""
        for word in processed:
            if word:
                if "<err>" in word or not word in self.__source:
                    response += err(word) + joint
                else:
                    response += self.__source[word] + joint

        return response.strip()
