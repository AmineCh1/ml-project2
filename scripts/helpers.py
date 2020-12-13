import pathlib
from os import path, pardir


def data_path(filename):
    return path.join(pathlib.Path(__file__).parent, pardir, 'data', filename)


def vocab_data_path(filename):
    return path.join(data_path(), 'vocab', filename)
