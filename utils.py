import io
import os
import string
import random
import glob
import unicodedata
import torch

# alphabet small + capital letters + " .,;'"
ALL_CHARS = string.ascii_letters + " .,;'"
N_LETTERS = len(ALL_CHARS)


def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in ALL_CHARS
    )

def load_data():
    # Build the category_lines dictionary, a list of names per language
    category_lines = {}
    all_categories = []

    def find_files(path):
        return glob.glob(path)
    
    # Read a file and split into lines
    def read_lines(filename):
        lines = io.open(filename, encoding='utf-8').read().strip().split('\n')
        return [unicode_to_ascii(line) for line in lines]

    for filename in find_files('data/names/*.txt'):
        #Extract categories from each filename
        category = os.path.splitext(os.path.basename(filename))[0]
        all_categories.append(category)
        #Extract line
        lines = read_lines(filename)
        category_lines[category] = lines

    return category_lines, all_categories

# Find letter index from all_letters, e.g. "a" = 0
def letter_to_index(letter):
    return ALL_CHARS.find(letter)

def letter_to_tensor(letter):
    tensor = torch.zeros(1, N_LETTERS)
    tensor[0][letter_to_index(letter)] = 1
    return tensor

def line_to_tensor(line):
    tensor = torch.zeros(len(line), 1, N_LETTERS)
    for i, letter in enumerate(line):
        tensor[i][0][letter_to_index(letter)] = 1
    return tensor

def random_training_example(category_lines, all_categories):
    
    def random_choice(a):
        random_idx = random.randint(0, len(a) - 1)
        return a[random_idx]
    
    category = random_choice(all_categories)
    line = random_choice(category_lines[category])
    category_tensor = torch.tensor([all_categories.index(category)], dtype=torch.long)
    line_tensor = line_to_tensor(line)
    return category, line, category_tensor, line_tensor
    
if __name__ == '__main__':
    print(unicode_to_ascii('Ślusàrski'))
    category_lines, all_categories = load_data()
    print(line_to_tensor('Jones').size()) # [5, 1, 57]