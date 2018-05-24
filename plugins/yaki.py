import yaml
import random
from slackbot.bot import listen_to


@listen_to('ひよわ焼き')
def yaki(message):
    with open("dic/yaki.yml", "r+") as data_list:
        data = yaml.load(data_list)
    message.reply(random.choice(data))
