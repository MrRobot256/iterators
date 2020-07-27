import hashlib


def use_generator(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        start = 0
        end = len(lines)

        while start < end:
            data = hashlib.md5(lines[start].encode())
            data1 = data.hexdigest()
            yield data1
            start += 1


for i in use_generator('file.txt'):
    print(i)


