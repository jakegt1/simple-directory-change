import os
import re

class DirSearch():

    def __init__(self, dir_string):
        split = dir_string.split("/")
        self.search_string = split.pop()
        self.workdir = self.get_workdir(split)
        self.regex = re.compile(self.search_string)

    def problematic_search_string(self):
        curr_path = os.getcwd() + "/" + self.search_string
        resolved_path = os.path.realpath(self.search_string)
        return (curr_path != resolved_path)

    def get_workdir(self, split):
        workdir = os.getcwd()
        if(split):
            full_path = "/".join(split)
            workdir = full_path
            workdir = os.path.expanduser(workdir)
            workdir = os.path.realpath(workdir)
        return workdir

    def return_first_match(self):
        matched_dir = ""
        if(not self.problematic_search_string() and self.search_string):
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
            if(self.problematic_search_string()):
                matched_dir = self.workdir + "/" + self.search_string
                matched_dir = os.path.expanduser(matched_dir)
                matched_dir = os.path.realpath(matched_dir)
            else:
                matched_dir = self.workdir
        return matched_dir
