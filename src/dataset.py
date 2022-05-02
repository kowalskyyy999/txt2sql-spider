#!/usr/bin/python3

import os 
import sys
import json

from dotenv import load_dotenv

load_dotenv()

path = os.environ.get('PATH_SPIDER')

with open(os.path.join(path, 'dev_gold.sql'), 'r') as f:
    lines = f.readlines()

print(lines[-1])
