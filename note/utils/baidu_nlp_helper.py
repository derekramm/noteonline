#!/usr/bin/env python
# -*- coding:utf-8 -*-

from enum import Enum, unique

from aip import AipNlp

APP_ID = '17161330'
API_KEY = 'ygfGhfm96ujzEQ0mgH84AoCL'
SECRET_KEY = 'iMpvW3sCpX5PtzmOvNuQ2oNlzj3wXyVn'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def get_keyword(title=None, content=None):
    if not title:
        title = "iphone手机出现“白苹果”原因及解决办法，用苹果手机的可以看下"
    if not content:
        content = "如果下面的方法还是没有解决你的问题建议来我们门店看下成都市锦江区红星路三段99号银石广场24层01室。"
    items = client.keyword(title, content).get('items')
    return [item.get('tag') for item in items]


def get_topic(title=None, content=None):
    if not title:
        title = "欧洲冠军杯足球赛"
    if not content:
        content = "欧洲冠军联赛是欧洲足球协会联盟主办的年度足球比赛，代表欧洲俱乐部足球最高荣誉和水平，被认为是全世界最高素质、最具影响力以及最高水平的俱乐部赛事，亦是世界上奖金最高的足球赛事和体育赛事之一。"
    item = client.topic(title, content).get('item')
    lv1_tag_list = item.get('lv1_tag_list')
    lv2_tag_list = item.get('lv2_tag_list')
    return [t.get('tag') for t in lv1_tag_list], [t.get('tag') for t in lv2_tag_list]


def get_news_summary(content=None, max_summary_len=50):
    if not content:
        content = "麻省理工学院的研究团队为无人机在仓库中使用RFID技术进行库存查找等工作，创造了一种聪明的新方式。使用RFID标签更换仓库中的条形码，将帮助提升自动化并提高库存管理的准确性。几家公司已经解决了无人机读取RFID的技术问题。麻省理工学院的新解决方案，名为Rfly，允许无人机阅读RFID标签，而不用捆绑巨型读卡器。无人机接收从远程RFID读取器发送的信号，然后转发它读取附近的标签。"
    options = {"title": "标题"}
    """ 带参数调用新闻摘要接口 """
    return client.newsSummary(content, max_summary_len, options).get('summary')


@unique
class CommentType(Enum):
    HOTEL = 1
    KTV = 2
    BEAUTY = 3
    FOOD = 4
    TRAVEL = 5
    HEALTH = 6
    EDU = 7
    BUSINESS = 8
    HOUSE = 9
    CAR = 10
    LIFE = 11
    SHOPPING = 12
    W3C = 13


def get_comment_tag(text=None, comment_type=CommentType.W3C):
    if not text:
        text = "三星电脑电池不给力"
    options = {"type": comment_type.value}
    """ 带参数调用评论观点抽取 """
    items = client.commentTag(text, options).get('items')
    return items
