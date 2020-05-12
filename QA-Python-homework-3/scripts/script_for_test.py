import os


if __name__ == '__main__':
    with open("logs.txt") as f:
        for line in f:
            os.system(f'sql_script.py {line}')
