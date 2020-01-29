from os import listdir
import os
import sys
import subprocess
from subprocess import check_output
from os.path import isfile, join
import json
import csv


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


def whois(input):
    ip_and_name = {}
    for item in filter(None, input):
        cmd = "whois {0}".format(item)
        proc = subprocess.check_output(cmd.split())
        start = proc.find('OrgName:')
        end = proc.find('OrgId:')
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