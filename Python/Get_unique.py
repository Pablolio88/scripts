from os import listdir
import os
from os.path import isfile, join


def get_unique(folder):
    ip_unique_list = []
    for f in listdir(folder):
        f = os.path.join(folder, f)
        with open(f) as file:
            start_list = []
            for line in file:
                line = line.strip()
                start_list.append(line)
            for i in start_list:
                if i not in ip_unique_list:
                    ip_unique_list.append(i)
    return ip_unique_list


folder = input("Give me the path in quotes: ")
outout = get_unique(folder)
with open("{}/get_unique.txt".format(folder), 'w') as output:
    for item in outout:
        output.write("%s\n" % item)
print("Look for you get_unique.txt file here: {}".format(folder))
