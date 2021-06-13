import re
from sys import argv
script,file_name=argv
import io

tags = []

with io.open(file_name,'r') as f:
    for line in f.readline():
        tags += re.findall(r'[#@][^\s#@]+', line)

for tag in tags:
	print(tag)
