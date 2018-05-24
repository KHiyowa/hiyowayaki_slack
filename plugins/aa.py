from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('gomi .+')
def hello(message):
    text = message.body['text']
    text = text.split()
    text = text[1]
    aa = 'ところでこのゴミどこに捨てればいい？\n　　∧＿∧\n　 (´∀｀   )\n　/⌒　　ヽ\n./ /　　 ﾉ ＼＿_M\n( /ヽ　　|＼＿＿E)\n.＼/　　 |　 ／　 ＼\n　(　 _ﾉ |　/ ' + text + '\n　｜　/ /　               │'
    message.send(aa)

@respond_to('boko .+')
def hello(message):
    text = message.body['text']
    text = text.split()
    text = text[1]
    aa = text +'？なにそれ\nぼこぼこにしてやんよ\n∧__∧\n(#･ω･)＝つ≡つ\n(っ　≡つ＝つ\n/　   )ﾊﾞﾊﾞﾊﾞﾊﾞ\n( /￣∪'
    message.send(aa)
