


#!/usr/bin/python
# coding:utf-8

import os
import json
import bs4
import requests

USER_AGENT = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

class Spider(object):
    def __init__(self, path):
        self.base_url = 'https://leetcode.com/'
        self.path = path
        self.session = requests.Session()
    
    def login(self, username, password):
        url = self.base_url
        cookies = self.session.get(url).cookies
        for cookie in cookies:
            if cookie.name == 'csrftoken':
                csrftoken = cookie.value
        
        url = url + 'accounts/login'
        headers = {
            'User-Agent': USER_AGENT,
            'Connection': 'keep-alive',
            'Referer': 'https://leetcode.com/accounts/login/',
            "origin": "https://leetcode.com",
            'Content-Type': 'application/json'
        }
        param_data = {
            'csrfmiddlewaretoken': csrftoken,
            'login': username,
            'password': password,
            'recaptcha_token': '', # Leetcode 新增了这个参数, 导致本login函数不再有效
            'next': 'problems'
        }
        self.session.post(url, headers=headers, data=param_data, timeout=10, allow_redirects = False)
        is_login = self.session.cookies.get('LEETCODE_SESSION') != None
        return is_login

    
    def get_problems(self):
        url = self.base_url + 'api/problems/algorithms'
        html = requests.get(url).content
        soup = bs4.BeautifulSoup(html, 'html.parser')
        problem_str = soup.prettify()
        problem_dic = json.loads(problem_str) # json 处理
        problem_list = problem_dic['stat_status_pairs']

        for problem in reversed(problem_list):
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
        self.generate_problem_markdown(question, paid_only)
        self.generate_readme_form(question)

    def generate_problem_markdown(self, question, paid_only):
        # save_path = os.path.join(self.path, "{:0>3d}-{}".format(int(question['questionFrontendId']), question['questionTitleSlug']))
        save_path = os.path.join(self.path, 'Solutions', "{}-{}".format(int(question['questionFrontendId']), question['questionTitleSlug']) + ".md")
        
        print('New file ', save_path)
        with open(save_path, 'w+') as f:
            f.write('- [Intro](#intro)\n\n## Intro\n\n- {}\n\n'.format(self.base_url+'problems/'+question['questionTitleSlug']))
            
            if not paid_only: # 付费的题就不用获取内容了
                # print('本题免费', question['questionId'])
                html_content = question['content']
                txt = bs4.BeautifulSoup(html_content, features="lxml").getText()
                f.write(txt)

    def generate_readme_form(self, question):
        readme_path = os.path.join(self.path, "readme.md")
        local_file = "./Solutions/{}-{}".format(int(question['questionFrontendId']), question['questionTitleSlug'])
        with open(readme_path, 'a+') as f:
            f.write('[{}]({})\n'.format(question['questionTitle'], local_file)) # 添加表格内容

    def run(self):
        self.get_problems()


if __name__ == '__main__':
    S = Spider('/Users/yjatt/Projects/leetcode/script')
    S.run()


