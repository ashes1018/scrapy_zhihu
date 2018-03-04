# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class UserItem(Item):
    # 答题数
    answer_count = Field()
    # 文章数
    articles_count = Field()
    # 头像
    avatar_url = Field()
    # 简介
    description = Field()
    # 教育
    school = Field()
    # 专业
    major = Field()
    # 地域
    location = Field()
    # 职业
    job = Field()
    # 获得收藏数
    favorited_count = Field()


    # 关注者数
    follower_count = Field()
    # 关注的人数
    following_count = Field()
    gender = Field()
    # 头条新闻
    headline = Field()
    # id = Field()
    # 地域
    locations = Field()
    # 知乎收录的回答数
    marked_answers_count = Field()
    name = Field()
    # 提问数
    question_count = Field()
    # 获得感谢数
    thanked_count = Field()
    # 获得感谢数
    voteup_count = Field()
    # 是否是官方组织
    is_org =Field()
    # 提问数
    pins_count = Field()

