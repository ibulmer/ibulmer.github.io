import os

rootdir = '../ibulmer.github.io'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".html"):
            print (filepath)
            with open('../'+filepath, 'r+') as file:
                content = file.read()
                file.seek(0)
                file.truncate()
                file.write(content.replace("<sidebar></sidebar>", "<div>Here is my header</div>"))



