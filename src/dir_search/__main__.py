#!/usr/bin/python3
import sys
import argparse
from .dir_search import DirSearch
parser = argparse.ArgumentParser()
parser.add_argument(
    "dir_string",
    help="directory for search",
)
args = parser.parse_args()

dir_search = DirSearch(args.dir_string)
matches = dir_search.return_matching_dirs()
print(matches)
