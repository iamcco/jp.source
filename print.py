#!/usr/bin/env python3

import json
import sys
import os

argv = sys.argv

if len(argv) > 1:
    fileName = './data/%s.json' % argv[1]
    if os.path.exists(fileName):
        data = open(fileName, 'r').read()
        data = json.loads(data)
        for item in data:
            print(item)
    else:
        print(fileName + 'is not exists')
else:
    print('one argument is need')
