import tweepy

CONSUMER_KEY = "Hoge"
CONSUMER_SECRET = "Fuga"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

ACCESS_TOKEN = "Foo"
ACCESS_SECRET = "Bar"
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
def tweet(tweetcontent):
	api.update_status(status=tweetcontent)
def zero():
	tweet("0時だよー")
def one():
	tweet("1時だよー")
def two():
	tweet("2時だよー")
def three():
	tweet("3時だよー")
def four():
	tweet("4時だよー")
def five():
	tweet("5時だよー")
def six():
	tweet("6時だよー")
def seven():
	tweet("7時だよー")
def eight():
	tweet("8時だよー")
def nine():
	tweet("9時だよー")
def ten():
	tweet("10時だよー")
def eleven():
	tweet("11時だよー")
def twelve():
	tweet("12時だよー")
#コピペに飽きたのでまだ続けるなら上の関数たちを名前変えてコピペどうぞ。 by raspi0124

schedule.every().day.at("0:00").do(zero)
schedule.every().day.at("1:00").do(one)
schedule.every().day.at("2:00").do(two)
schedule.every().day.at("3:00").do(three)
schedule.every().day.at("4:00").do(four)
schedule.every().day.at("5:00").do(five)
schedule.every().day.at("6:00").do(six)
schedule.every().day.at("7:00").do(seven)
schedule.every().day.at("8:00").do(eight)
schedule.every().day.at("9:00").do(nine)
schedule.every().day.at("10:00").do(ten)
schedule.every().day.at("11:00").do(eleven)
schedule.every().day.at("12:00").do(twelve)

while True:
	schedule.run_pending()
	time.sleep(1)
