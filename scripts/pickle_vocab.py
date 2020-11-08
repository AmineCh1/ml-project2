#!/usr/bin/env python3
import pickle
from helpers import *


def main():
    vocab = dict()

    with open(vocab_data_path('vocab_cut.txt')) as f:
        for idx, line in enumerate(f):
            vocab[line.strip()] = idx

    with open(vocab_data_path('vocab.pkl'), 'wb') as f:
        pickle.dump(vocab, f, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
