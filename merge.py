import time
from os import listdir
from os.path import isfile, join
mypath = "./"

def find_str(s, char):
  index = 0
  if char in s:
    c = char[0]
    for ch in s:
      if ch == c:
        if s[index:index+len(char)] == char:
          return index
      index += 1
  return -1

def has_ext(f):
	cond = False
	cond = cond or find_str(f, ".mp4") == len(f) - 4
	cond = cond or find_str(f, ".avi") == len(f) - 4
	cond = cond or find_str(f, ".wmv") == len(f) - 4
	cond = cond or find_str(f, ".mkv") == len(f) - 4
	cond = cond or find_str(f, ".mpg") == len(f) - 4
	return cond
  
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and has_ext(f)]

from subprocess import call
counter = 0
listFile = open("list.txt", "w")

for file in onlyfiles:
	listFile.write("file "+file+"\n")

listFile.close()
call(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "list.txt", "-c", "copy", "output.wmv"])