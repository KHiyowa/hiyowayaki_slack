from slackbot.bot import respond_to
from slackbot.bot import listen_to


@listen_to('めもり')
def memori(message):
    message.send('こんにちは、めもりです。')

@respond_to('君は誰')
def hello(message):
    message.reply('私はめもりです。なんでもお手伝いします。')

@respond_to('コルタナ')
@respond_to('Cortana')
def cortana(message):
    message.reply('Bingで探しますか?')

@respond_to('Siri')
def siri(message):
    message.reply('尊敬すべき先輩です。')

@respond_to('しゃべってコンシェル')
def concier(message):
    message.reply('うさぎの執事です。')

@respond_to('ひよわ')
def hiyowa(message):
    message.reply('ひよわは私を作ったやつ')

@respond_to('ナナチ')
def concier(message):
    message.reply('んなぁ〜うるせえなぁ〜')

@respond_to('サーバル')
def concier(message):
    message.reply('すっごーい!!')

@respond_to('ハム太郎')
def concier(message):
    message.reply('へけっ')

@respond_to('愛してる')
def love(message):
    message.reply('それSiriさんも言われたって言ってましたよ?')

@listen_to('なんでも')
def nandemo(message):
    message.reply('ん?いまなんでもって')
