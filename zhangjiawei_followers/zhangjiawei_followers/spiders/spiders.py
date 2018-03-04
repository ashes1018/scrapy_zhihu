# -*- coding: utf-8 -*-
import scrapy
import json
from zhangjiawei_followers.items import UserItem
from bs4 import BeautifulSoup
from scrapy import Spider,Request
import pymysql




class zhangjiawei_followers(scrapy.spiders.Spider):
    # handle_httpstatus_list = [401]
    id = 1
    allowed_domain = ["www.zhihu.com"]
    name = 'zjw_followers'
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&amp;offset={offset}&amp;limit={limit}'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    start_user = 'gejinyuban'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    db = pymysql.connect(host="localhost", user="root",
                         password="ashes", db="yulan", port=3306)

    # db.set_character_set('utf8')



    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
        # yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, limit=20, offset=0),
        #               self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, limit=20, offset=0),
                      self.parse_followers)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()
        # print(result)
        for field in item.fields:

            if len(str(result.get('educations'))) > 2:
                # print(str(result.get('educations')).split(',')[2])
                School = str(result.get('educations')).split(',')[2]
                item['school'] = School[10:len(School)-1]
                if len(str(result.get('educations'))) > 9:
                    Major = str(result.get('educations')).split(',')[9]
                    item['major'] = Major[10:len(School) - 2]
            if len(str(result.get('employments'))) > 2:
                # print(result.get('employments'))
                Job = str(result.get('employments')).split(',')[2]
                item['job'] = Job[10:len(Job)-1]

            if len(str(result.get('locations'))) > 2:
                Locate = str(result.get('locations')).split(',')[2]
                item['location'] = Locate[9:len(Locate)-1]
                # print(Locate[10:len(Locate)-1])
            item[field] = result.get(field)

        sql_1 = """INSERT INTO t(id,name,avatar_url,answer_count,articles_count,description,school,major,
location,job,favorited_count,follower_count,following_count,gender,headline,marked_answers_count,
question_count,thanked_count,voteup_count,is_org,pins_count)
VALUES (%s, %s,%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s, %s,%s, %s,%s, %s,%s, %s,%s)"""
        cur = self.db.cursor()

        cur.execute(sql_1,(
                           self.id,
                           str(item['name']).encode('utf-8'),
                           str(item['avatar_url']).encode('utf-8'),
                           str(item['answer_count']).encode('utf-8'),
                           str(item['articles_count']).encode('utf-8'),
                           str(item['description']).encode('utf-8'),
                           str(item['school']).encode('utf-8'),
                           str(item['major']).encode('utf-8'),
                           str(item['location']).encode('utf-8'),
                           str(item['job']).encode('utf-8'),
                           str(item['favorited_count']).encode('utf-8'),
                           str(item['follower_count']).encode('utf-8'),
                           str(item['following_count']).encode('utf-8'),
                           str(item['gender']).encode('utf-8'),
                           str(item['headline']).encode('utf-8'),
                           str(item['marked_answers_count']).encode('utf-8'),
                           str(item['question_count']).encode('utf-8'),
                           str(item['thanked_count']).encode('utf-8'),
                           str(item['voteup_count']).encode('utf-8'),
                           str(item['is_org']).encode('utf-8'),
                           str(item['pins_count']).encode('utf-8')
                           ))
        self.id = self.id + 1
        self.db.commit()
        # self.db.close()
        # yield item

        # yield Request(
        #     self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0),
        #     self.parse_follows)

        yield Request(
            self.followers_url.format(user=result.get('url_token'), include=self.followers_query, limit=20, offset=0),
            self.parse_followers)

    # def parse_follows(self, response):
    #     print(response.text)
    #     results = json.loads(response.text)
    #     print(results)
    #     if'data' in results.keys():
    #         for result in results.get('data'):
    #             yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
    #                           self.parse_user)
    #
    #     if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
    #         next_page = results.get('paging').get('next')
    #         yield Request(next_page,
    #                       self.parse_follows)

    def parse_followers(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,
                          self.parse_followers)