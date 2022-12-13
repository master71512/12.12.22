def reader_1():
    data = open('HW/12.12.22/format_1.txt', 'r')
    for string in data:
        print(string, end = '')
    data.close()

def reader_2():
    data = open('HW/12.12.22/format_2.txt', 'r')
    for string in data:
        print(string, end = '')
    print()
    data.close()
