from os import listdir
from os.path import isfile, join
import re

DIR_PATH = 'data'
FILES = [DIR_PATH + '/' + file for file in listdir(DIR_PATH) if isfile(join(DIR_PATH, file))]


def main_code():
    p = re.compile(r'^".*"$')
    is_blank = False
    for file in FILES:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                if p.search(line):
                    print(line.replace('"', '').strip())
                    is_blank = False
                else:
                    if not is_blank:
                        is_blank = True
                        print()
        print('-- ' * 100)


if __name__ == '__main__':
    main_code()
