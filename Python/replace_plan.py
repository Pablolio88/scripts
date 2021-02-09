# Read in the file
file_name = str(input("File name:"))
print(file_name)
with open(file_name, 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('[0m[1m', '')
filedata = filedata.replace('[0m', '')
filedata = filedata.replace('[32m+[0m', '+')
filedata = filedata.replace('[33m~[0m', '~')
filedata = filedata.replace('[32m+', '+')
filedata = filedata.replace('[1m', '')
filedata = filedata.replace('[33m~', '~')
filedata = filedata.replace('[32m-', '-')
filedata = filedata.replace('[90m', '')
filedata = filedata.replace('[33m', '')
filedata = filedata.replace('[31m', '')



# Write the file out again
with open(file_name, 'w') as file:
    file.write(filedata)