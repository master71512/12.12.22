def record_1(record):
    data = open('HW/12.12.22/format_1.txt', 'a')
    for i in record:
        data.write(i + '\n')
    data.write('\n')
    data.close()

def record_2(record):
    data = open('HW/12.12.22/format_2.txt', 'a')
    for i in range(len(record)):
        data.write(record[i])
        if i < len(record) - 1:
            data.write(', ')
        else:
            data.write('\n')
    data.close()
