"""Task 1."""
from keyword import iskeyword
from typing import Union


class KeyValueStorage:
    """Storage class.

    Class that gets text file as input with 'key=value' format, and transforms it
    into dict, int values are changed into ints. Later you can access to the
    stored through this class.
    """

    def __init__(self, filename: str):
        """Innit.

        :param filename: path to file to work with
        """
        self.stor = {}
        with open(filename) as f:
            text = f.read()
        key_val = [x.split("=") for x in text.split()]
        for key, value in key_val:
            if iskeyword(key) or not key.isidentifier():
                raise ValueError("Invalid key!")
            if value.isdigit():
                value = int(value)
            self.stor[key] = value

    def __getitem__(self, key: str) -> Union[str, int]:
        """Get item.

        Gets item that bounded to given key value. Example: storage['key'] returns
        item

        :param key: key
        :return: item
        """
        return self.stor[key]

    def __getattr__(self, key: str) -> Union[str, int]:
        """Get attribute.

        Gets item that bounded to given key value. Example: storage.key returns
        item

        :param key: key
        :return: item
        """
        return self.stor[key]
