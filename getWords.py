#!/usr/bin/env python3

# source form http://www.v5jp.com/html/japan/syhz01.html
# index is range [01..531]

from urllib import request
import re
import json
import os

PATH = 'http://www.v5jp.com/html/japan/syhz%s.html'

for idx in range(129,532):
    if idx < 10:
        idx = '0' + str(idx)
    path = PATH % idx
    content = request.urlopen(path).read().decode('utf-8')
    items = re.findall(r'<ul\s*class="fw">\s*((?:.*\s*)*?)\s*</ul>', content)
    items = re.findall(r'<li>(.*?)</li>', items[0])
    if not os.path.exists('./data'):
        os.mkdir('./data', 755)
    f = open('./data/%s.json' % idx, 'w')
    f.write(json.dumps(items))
    f.close()
    print('create data ./data/%s.json' % idx)
