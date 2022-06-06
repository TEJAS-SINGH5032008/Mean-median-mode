import csv
with open('Data.csv,new line = "" ')'as f':
    readre = csv.reader(f)
    file_data = list(reader)

    from collections import counter
    new_data = "Data"
    data = counter(new_data)
    print('data')

    file_data.pop(0)
    new_data = []
    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(flant(n_num))

        n = len(new_data)
        total = 0
        forx in new_data:
            total += x
            mean = total/n
            print('mean/average is'+str(mean))
            