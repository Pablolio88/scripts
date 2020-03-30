from os import listdir
import os
import subprocess
import csv


def get_unique(folder):
    ip_unique_list = set([])
    for f in listdir(folder):
        f = os.path.join(folder, f)
        with open(f) as file:
            for line in file:
                line = line.strip()
                ip_unique_list.add(line)
    return ip_unique_list


def whois(input):
    ip_and_name = {}
    for item in filter(None, input):
        cmd = "whois {0}".format(item)
        proc = subprocess.check_output(cmd.split())
        start = proc.find('netname:')
        end = proc.find('country:')
        if start:
            org_name = (proc[start:end]).strip()
            ip_and_name[item] = org_name
    return ip_and_name


folder = input("Give me the path in quotes: ")
outout = get_unique(folder)
print(outout)
whois_output = whois(outout)
print(whois_output)
ip_and_name_list = "{}/ip_and_name_list.txt".format(folder)
w = csv.writer(open(ip_and_name_list, "w"))
for key, val in whois_output.items():
    w.writerow([key, val])
print("Look for you file here: {}".format(folder))