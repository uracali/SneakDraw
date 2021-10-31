from Nike.dailyRaffle import dailyRaffle as nikeRaffle
from Worksout.dailyRaffle import dailyRaffle as worksOutRaffle
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
import json

sched = BlockingScheduler()


class RaffleSwitcher:
    def __init__(self, field):
        """Dispatch method"""
        self.method_name = 'raffle_' + str(field)

    def getFunction(self, data={}):
        print("method_name : ", self.method_name)
        return getattr(self, self.method_name, lambda: "Invalid Field")

    def raffle_nike(self, data):
        return nikeRaffle(data)

    def raffle_worksOut(self, data):
        return worksOutRaffle(data)


def main(event):
    try:
        fieldName = event.get("field")
        data = event.get("arguments")
        switcher = RaffleSwitcher(fieldName)
        function = switcher.getFunction(data)
        return function(data)
    except Exception as ex:
        print('에러가 발생 했습니다', ex)
        return False

def run(userList, chatId):
    for user in userList:
        arguments = user
        nikeEvent = {"field": "nike", "arguments": arguments}
        result = main(nikeEvent)
        message = user["id"]+" "+str(result)
        bot.sendMessage(chatId, text= message)


if __name__ == "__main__":
    with open('./.env.json') as f:
        json_data = json.load(f)
        token = json_data['token']
        chatId = json_data['chatId']
    userList = json_data['user']
    bot = telegram.Bot(token=token)
    # run(userList, chatId)
    sched.add_job(lambda: run(userList, chatId),'cron',hour='10,11',minute='*/10',id='test')
    sched.start()
