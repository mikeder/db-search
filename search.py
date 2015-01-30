#!/usr/bin/python
# search.py
# Database search tool

import os
from os.path import join

lookfor = '.db'
searchdir = raw_input('Directory to search: ')
found = []
for root, dirs, files, in os.walk(searchdir):
#  print('Searching', root)
  for file in files:
    if file.endswith(lookfor):
      print('Found: %s' % join(root, file))
