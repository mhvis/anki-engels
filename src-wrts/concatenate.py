
import os
import os.path

dirs = [x for x in os.listdir() if os.path.isdir(x)]
#print(dirs)

for dirname in dirs:
    files = os.listdir(dirname)
    for filename in files:
        if not filename.endswith('.txt'):
            continue
        path = dirname + "/" + filename
        chapter = filename[:-4]
        #print(path)
        with open(path) as f:
            for line in f.readlines():
                out = '{},"{}"'.format(line.strip(), chapter)
                print(out)
