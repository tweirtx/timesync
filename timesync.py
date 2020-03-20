#!/usr/bin/python3
import argparse
import dirsync
import os
import time

argsin = argparse.ArgumentParser()
argsin.add_argument("dir1")
argsin.add_argument("dir2")
args = argsin.parse_args()

now = time.time()

try:
    last = os.stat("syncdummy.test").st_mtime
except FileNotFoundError:
    open("syncdummy.test", 'x').close()
    last = 0

print(last)

for file in os.listdir(args.dir1):
    if os.stat(args.dir1 + "/" + file).st_mtime > last:
        dirsync.run.sync(args.dir1, args.dir2, "sync")
        break

with open("syncdummy.test", 'w') as f:
    f.write(str(now))
print("Finished!")
