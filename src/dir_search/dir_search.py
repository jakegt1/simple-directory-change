import os
import re

class DirSearch():

    def __init__(self, dir_string):
        split = dir_string.split("/")
        self.search_string = split.pop()
        self.workdir = self.get_workdir(split)
        self.regex = re.compile(re.escape(self.search_string))

    def get_workdir(self, split):
        workdir = os.getcwd()
        if(split):
            full_path = "/".join(split)
            workdir = full_path
            workdir = os.path.expanduser(full_path)
            workdir = os.path.realpath(full_path)
        return workdir

    def return_first_match(self):
        matched_dir = ""
        if(self.search_string):
            for root, dirs, files in os.walk(self.workdir):
                found = False
                if(root[-1] != "/"):
                    root += "/"
                for dir in dirs:
                    if(self.regex.match(dir)):
                        matched_dir = root+dir
                        found = True
                        break
                if(found):
                    break
        else:
            matched_dir = self.workdir
        if(not matched_dir):
            matched_dir = self.search_string
            matched_dir = os.path.expanduser(matched_dir)
            matched_dir = os.path.realpath(matched_dir)
        return matched_dir
