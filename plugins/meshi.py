import json
import yaml
import random
from slackbot.bot import listen_to
from slackbot.bot import respond_to
from urllib.parse import urlparse
from http.client import HTTPConnection

# https://gist.github.com/gin0606/5788744
# から引用

meshi_terro = True

def expandURL(url):
    """
    短縮URLを展開する
    Arguments:
    - `url`: 展開したいURL
    """
    o = urlparse(url)
    con = HTTPConnection(o.netloc)
    con.request('HEAD', o.path)
    res = con.getresponse()
    if res.getheader('location') == None:
        return url
    return res.getheader('location')

@respond_to('飯テロON')
def meshi_on(message):
    global meshi_terro
    meshi_terro = True
    message.reply('飯テロ機能をオンにしました。')

@respond_to('飯テロOFF')
def meshi_off(message):
    global meshi_terro
    meshi_terro = False
    message.reply('飯テロ機能をオフにしました。')

@listen_to('腹減っ')
@listen_to('はらへ')
@listen_to('おなかすい')
@listen_to('おなかへっ')
@listen_to('はらぺこ')
def meshi(message):
    global meshi_terro
    if meshi_terro == False:
        message.send('飯テロ機能はオフです。命拾いしたな?')
        return
    with open("dic/meshi.yml", "r+") as data_list:
        data = yaml.load(data_list)

    datum = random.choice(data).split()
    for i in range(10):
        try:
            meshi_url = expandURL("http://" + datum[i])
            break
        except:
            continue
    message.reply(meshi_url)
