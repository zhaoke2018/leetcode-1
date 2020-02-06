"""
- 列举 Solutions/ 里面所有涉及过的tag, 并统计出现的次数.
- 由于文件系统无法像网站那样直接搜索已有tag, 因此用本文件来做tag修正.
"""

import os, re

class CountTags:
    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'Solutions') # os.getcwd() 是运行命令时的目录.
        # eg 如果直接在项目根目录下运行, 那后面就要补上 solutions 之类的
    def find_all_tags_and_count(self):
        for md in os.listdir(self.path):
            if not md.endswith('md'):
                return
            
            md_path = os.path.join(self.path, md)
            with open(md_path, 'r') as f:
                content = f.read()

                tags = re.findall(r'## Topics\s*', content)


CountTags()