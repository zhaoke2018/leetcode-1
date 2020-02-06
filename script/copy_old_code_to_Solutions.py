'''
- 本文件用来合并同名 markdown 文件, 一次性使用.
- 之后可以用来学习或者代码参考
- 这里用到的 fuzzyfinder 值得学习一下
'''

import os
import re
import logging


class TransferCode():
    def __init__(self):
        self.sols = []
        self.path_solution = os.path.join(os.getcwd(), 'Solutions') # getcwd() 是运行目录
        self.path_old_code = os.path.join(os.getcwd(), 'old_code')

        for sol in os.listdir(self.path_solution): # 缓存 /Solutions 的所有文件名, 方便之后查找
            self.sols.append(sol)

        # logger 相关配置
        self.logger = logging.getLogger('myapp')
        logger_handler = logging.FileHandler(os.path.join(os.getcwd(), "tranfer.log"))
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        logger_handler.setFormatter(formatter)
        self.logger.addHandler(logger_handler)
        self.logger.setLevel(logging.INFO) # 表示只有比 Info 更严重的才记录. 如果不设置的话, 默认是只有比 warning 更严重才记录


    def move_same_name_file(self):

        for oldi in os.listdir(self.path_old_code):
            if oldi.endswith(".md"):
                match_gen = self.fuzzyfinder(oldi, self.sols)
                try:
                    match_sol = next(match_gen)
                    self.logger.info(oldi + ' ----> ' + match_sol)
                    path_oldi = os.path.join(self.path_old_code, oldi)
                    with open(path_oldi, 'r',) as oldf:
                        oldf_content = oldf.read()
                        path_sol = os.path.join(self.path_solution, match_sol)
                        with open(path_sol, 'a') as newf:
                            newf.write(oldf_content)
                except:
                    self.logger.error(oldi)
                    continue

    def fuzzyfinder(self, input, collection, accessor=lambda x: x, sort_results=True):
        """
        credit: https://github.com/amjith/fuzzyfinder/blob/master/fuzzyfinder/main.py
        """
        suggestions = []
        input = str(input) if not isinstance(input, str) else input
        pat = '.*?'.join(map(re.escape, input))
        pat = '(?=({0}))'.format(pat)   # lookahead regex to manage overlapping matches
        regex = re.compile(pat, re.IGNORECASE)
        for item in collection:
            r = list(regex.finditer(accessor(item)))
            if r:
                best = min(r, key=lambda x: len(x.group(1))) # find shortest match
                suggestions.append((len(best.group(1)), best.start(), accessor(item), item))

        if sort_results:
            return (z[-1] for z in sorted(suggestions))
        else:
            return (z[-1] for z in sorted(suggestions, key=lambda x: x[:2]))


TransferCode().move_same_name_file()