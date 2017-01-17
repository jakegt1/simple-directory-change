import os
import re

class DirSearch():

    def __init__(self, dir_string):
        self.workdir = os.getcwd()
        self.search_string = dir_string
        if(dir_string[0] == "/" or dir_string[0] == "~"):
            self.workdir = ""
        split = dir_string.split("/")
        if(split[-1] == ''):
            split.pop()
        if(len(split) > 1):
            self.search_string = split.pop();
            self.workdir = self.workdir+"/"+'/'.join(split)
            os.chdir(self.workdir)
        else:
            self.search_string = split[0]
        self.regex = re.compile(self.search_string)


    def return_matching_dirs(self):
        matching_dirs = []
        for root, dirs, files in os.walk(self.workdir):
            found = False
            if(root[-1] != "/"):
                root += "/"
            for dir in dirs:
                if(self.regex.match(dir)):
                    matching_dirs.append(root+dir)
                    found = True
                    break
            if(found):
                break
        return matching_dirs
