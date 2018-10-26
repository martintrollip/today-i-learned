# encoding: utf-8
#!/bin/env/python
import os
import re
import codecs
import json
from datetime import datetime


TIL_FOLDER = '../khanhicetea.com/content/til'
DOC_CONTENT = u'''+++
date = "{post_date}"
title = "#TIL : {title}"
description = "I learned on {learn_date} about {topics}"
categories = {categories}
tags = {tags}
image = "/images/never_stop_learning.jpg"
+++

'''


def read_entire_file(file_path):
    with codecs.open(file_path, 'r') as content_file:
        return content_file.read()


def write_entire_file(file_path, content):
    with codecs.open(file_path, 'w', encoding='utf=8') as content_file:
        return content_file.write(content)


def parse_article(content, category):
    pos1 = content.find('- Date : ')
    pos2 = content.find('- Tags : ', pos1)
    pos3 = content.find("\n", pos2)
    pos4 = content.find("##", pos3)
    pos5 = content.find("\n", pos4)
    post = {
        "date": datetime.strptime(content[pos1+9:pos2].strip(), "%Y-%m-%d"),
        "category": category,
        "tags": [t[1:] for t in content[pos2+9:pos3].strip().split(' ')],
        "content": content[pos3:].strip(),
        "title": content[pos4+3:pos5].strip(),
    }

    return post


def slugify(s):
    s = s.lower()
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')
    s = re.sub('\W', '', s)
    s = s.replace('_', ' ')
    s = re.sub('\s+', ' ', s)
    s = s.strip()
    s = s.replace(' ', '-')
    return s


def convert_til_2_hugo(source, dest):
    excluded_folders = [".git", TIL_FOLDER]
    categories = [f for f in os.listdir(source) if os.path.isdir(f) and f not in excluded_folders]

    data = dict()

    for cat in categories:
        for file in os.listdir(os.path.join(source, cat)):
            raw = read_entire_file(os.path.join(source, cat, file))
            parts = raw.split('/--------------------/')
            for part in parts:
                article = parse_article(part.strip(), cat)
                title = article['title'].decode('utf-8')
                article_date = article['date']
                post_date = article_date.replace(hour=23, minute=59, second=59)
                article_categories = ['Today I learned']
                tags = []

                content = "\n\n" + article['content'] + "\n"
                
                article_categories.append(article['category'])
                for tag in article['tags']:
                    tags.append(tag)

                raw_file = DOC_CONTENT.format(
                    title=title,
                    learn_date=article_date.date().isoformat(),
                    post_date=post_date.strftime('%Y-%m-%dT%H:%M:%S'),
                    topics=", ".join(set(tags)),
                    categories=json.dumps(list(set(article_categories))),
                    tags=json.dumps(list(set(tags)))
                )

                write_entire_file(
                    os.path.join(dest, "{date}-{title}.md".format(
                        date=article_date.date().isoformat(),
                        title=slugify(title)
                    )),
                    raw_file + content.decode('utf-8')
                )


if __name__ == '__main__':
    cwd = os.getcwd()
    convert_til_2_hugo(cwd, os.path.join(cwd, TIL_FOLDER))
    print("Converted !")
