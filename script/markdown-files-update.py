"""
Author: John
Description: Add new Markdown file to ./Sulutions
"""

import os
import json
import bs4
import requests
import re

USER_AGENT = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

class Spider(object):
    def __init__(self, path):
        self.base_url = 'https://leetcode.com/'
        self.path = path
        self.session = requests.Session()
        
        self.sols = []
        self.path_solution = os.path.join(os.getcwd(), 'Solutions') # getcwd() 是运行目录
        for sol in os.listdir(self.path_solution): # 缓存 /Solutions 的所有文件名, 方便之后查找
            self.sols.append(sol)
    
    def get_problem_list(self):
        url = self.base_url + 'api/problems/algorithms'
        html = requests.get(url).content
        soup = bs4.BeautifulSoup(html, 'html.parser')
        problem_str = soup.prettify()
        problem_dic = json.loads(problem_str) # json 处理
        problem_list = problem_dic['stat_status_pairs']

        for problem in reversed(problem_list):
            # 去掉这个if判断, 就可以生成所有的文件了.
            if problem['stat']['question__title_slug'] not in self.sols: # TODO 需要把标题拼接一下
                self.get_problem_by_slug(problem['stat']['question__title_slug'], problem['paid_only'])

    def get_problem_by_slug(self, slug, paid_only):
        url = self.base_url + 'graphql'
        params = {
            'operationName': "getQuestionDetail",
            'variables': {'titleSlug': slug},
            'query': '''query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    questionTitle
                    questionTitleSlug
                    content
                    difficulty
                    stats
                    similarQuestions
                    categoryTitle
                    topicTags {
                            name
                            slug
                    }
                }
            }'''
        }
        json_data = json.dumps(params).encode('utf8')
        headers = {
            'User-Agent': USER_AGENT, 
            'Connection': 'keep-alive', 
            'Content-Type': 'application/json',
            'Referer': 'https://leetcode.com/problems/' + slug
        }
        resp = self.session.post(url, data=json_data, headers=headers, timeout=10)
        content = resp.json()
        question = content['data']['question']

        self.generate_new_markdown_files(question, paid_only)
        self.append_readme_form(question)


    def generate_new_markdown_files(self, question, paid_only):
        if paid_only: # 付费的题就不用获取内容了
            return

        save_path = os.path.join(self.path, 'Solutions', "{}-{}".format(int(question['questionFrontendId']), question['questionTitleSlug']) + ".md")
        print('New file ', save_path)
        
        with open(save_path, 'w+') as f:

            # 目录
            toc = '- [Intro](#intro)\n\n'
            # Intro 标题
            intro_title = '## Intro\n\n'
            # 问题链接拼接
            problem_link = '- {}\n\n'.format(self.base_url+'problems/'+question['questionTitleSlug'])'
            # Intro 细节
            intro_content = bs4.BeautifulSoup(question['content'], features="lxml").getText()
            # Topics
            topics = '\n\n## Topics\n\n'
            for tag in question['topicTags']:
                topics += '- `{}`\n'.format(tag['name'])
            topics += '\n\n'

            f.write(toc + intro_title + problem_link + intro_content + topics)


    def append_readme_form(self, question):
        readme_path = os.path.join(self.path, "readme.md")
        local_file_link = "./Solutions/{}-{}".format(int(question['questionFrontendId']), question['questionTitleSlug'])
        with open(readme_path, 'a+') as f:
            f.write('[{}]({})\n'.format(question['questionTitle'], local_file_link)) # 添加表格内容

    def run(self):
        self.get_problem_list()


if __name__ == '__main__':
    S = Spider('/Users/yjatt/Projects/leetcode/')
    S.run()


