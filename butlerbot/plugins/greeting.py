# coding: UTF-8
from random import choice
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from ..botmessage import botreply


@listen_to('おはよう|お早う')
def morning(message):
    replies = (
        'おはようございます！ :smiley:',
        '気持ちのいい朝ですね！ :sunny:',
        'Good morning!',
    )
    botreply(message, choice(replies))


@listen_to('こんにち[はわ]')
def noon(message):
    replies = (
        'こんにちは！ :smiley:',
        'こんにちは、調子はどうかな :smiley:',
        'Hi!',
    )
    botreply(message, choice(replies))


@listen_to('いってきま|行ってきま|行ってくる')
def go(message):
    replies = (
        'はい、お気をつけて！ :wave:',
        'いってらっしゃい！ :wave:',
        'Have a good day!',
    )
    botreply(message, choice(replies))


@listen_to('眠た?い|ねむた?い|寝る|寝ます|おやすみ')
def night(message):
    replies = (
        'おやすみなさい :crescent_moon:',
        'それでは良い夢を :sheep:',
        'Have a good night!',
    )
    botreply(message, choice(replies))


@listen_to('帰る[よね]|帰りま|帰ってる')
def goback(message):
    replies = (
        'お疲れさま、お気をつけて :wave:',
        'お帰りをお待ちしてます :smiley:',
        'Watch your step going home!',
    )
    botreply(message, choice(replies))


@respond_to('ありがと|さんきゅ|サンキュ|どうも')
def thanks(message):
    replies = (
        'どういたしまして！',
        'お役に立てたのなら何よりです :smiley:',
        'It\'s my pleasure!',
    )
    botreply(message, choice(replies))
