import tweepy as twitter
import keys
import time
import datetime

auth = twitter.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)

api = twitter.API(auth)


def twitter_bot(hastag, delay):
    while True:
        print(f"\n{datetime.datetime.now()}\n")

        for tweet in twitter.Cursor(api.search, q=hastag, rpp=10).items(5):
            try:
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]

                print("id : " + str(tweet_id))
                print("text : " + str(tweet_text))

                api.retweet(tweet_id)

            except twitter.TweepError as error:
                print(error.reason)

        time.sleep(delay)


twitter_bot(
    ('#IndianFootball OR #WeAreBFC OR #ನಮ್ಮಬೆಂಗಳೂರು OR #ForcaGoa OR BengaluruFC OR FCGoa OR Kerala Blasters FC OR Hyderabad FC OR #HyderabadFC OR Mumbai City FC OR Odisha FC OR Jamshedpur FC OR Chennaiyin FC OR ATK Mohun Bagan FC OR #YennumYellow OR #WeAreSCEB'), 100)
