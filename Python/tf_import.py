import re
import glob
for filepath in glob.iglob('.terragrunt-cache/**/.terraform/**/*.tf', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = re.sub(r'region  = .*', 'region  = "us-east-1"', s)
    with open(filepath, 'w') as file:
        file.write(s)