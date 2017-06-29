import tweepy
import datetime

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  cfg = {
    "consumer_key"        : "ShawxVmB0hePPnmbHgad6XoJg",
    "consumer_secret"     : "1f98GRgiTp9jEa22A0Cp5upzfOEzNQuaF0PCpV3rra23FEZKvb",
    "access_token"        : "1526347196-K8VfPLTF4Ljwe7bSo2XoXCJ0rrR9jRSP0IdvkyI",
    "access_token_secret" : "XBqONCSdZV9SCwlvSPthQPYuPIq8dWxrvVXjbLdWzq1MH"
    }

  api = get_api(cfg)
  today = datetime.date.today()
  tweet = "Twiteado via tweepy "+str(today)
  status = api.update_status(status=tweet)

if __name__ == "__main__":
  main()