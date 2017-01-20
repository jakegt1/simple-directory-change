#!/usr/bin/python3
import sys
import argparse
import subprocess
import os
from .dir_search import DirSearch
parser = argparse.ArgumentParser()
parser.add_argument(
    "dir_string",
    help="directory for search",
    nargs="+"
)
args = parser.parse_args()
dir_string = ''.join(args.dir_string)
if(os.path.isdir(os.path.expanduser(dir_string))):
    print(dir_string)
else:
    dir_search = DirSearch(dir_string)
    match = dir_search.return_first_match_multi()
    if(match):
        print(match)
