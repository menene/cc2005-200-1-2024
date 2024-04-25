import os

for f in os.listdir():
    if os.path.isfile(f):
        ext = f.split('.')
        if (ext[1] == 'csv'):
            print(f)
