from sys import argv
from os.path import normpath, dirname, join
from os import listdir


if __name__ == '__main__':
    try:
        if len(argv) > 1 and argv[1] == "--path":
            hpath = normpath(argv[2])
            path = listdir(hpath)
        else:
            hpath = dirname(__file__)
            path = ['logs.txt']
        count = 0
        types = {}
        size = []
        top_four = {}
        for file in path:
            with open(join(hpath, file), "r") as f:
                for line in f:
                    count += 1
                    method = line.split('"')[1].split(' ')[0]
                    if method in types:
                        types[method] += 1
                    else:
                        types[method] = 1

                    size.append((line.split('"')[0] + line.split('"')[1], int(line.split('"')[2].split(' ')[2]))) 
                    size.sort(key=lambda i: i[1], reverse=True)

                    if int(line.split('"')[2].split(' ')[1]) // 100 == 4:
                        url = line.split('"')[1]
                        if url in types:
                            types[url] += 1
                        else:
                            types[url] = 1
        print(f"all requests {count}")
        for key, item in types.items():
            print(f'{key} = {item}')
    except Exception:
        print("sluchilas eres'")
