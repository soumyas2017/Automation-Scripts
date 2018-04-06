import sys,tweepy,nltk
from retrying import retry
from textblob import TextBlob
from nltk.sentiment import vader
# ConsumerKey= "zNgeiYgPoA4v7sicWK9Rz91n4"
# ConsumerSecret="X6K9t0iqStsn55ysq7Zkc8UwPiQO6wXjm6lsh7FrczZ2kFIuEm"
# AccessToken="1522565335-OGovhhKCLrwll918El6782S0OCSkSmMDWRYDLoX"
# AccessTokenSecret= "jcE48mSGrIfN4Jfo3f2QudfJi950NDHJKk1jpAqMolyGF"
@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def twitterSenti():
    try:
        ConsumerKey= "zNgeiYgPoA4v7sicWK9Rz91n4"
        ConsumerSecret="X6K9t0iqStsn55ysq7Zkc8UwPiQO6wXjm6lsh7FrczZ2kFIuEm"
        AccessToken="1522565335-OGovhhKCLrwll918El6782S0OCSkSmMDWRYDLoX"
        AccessTokenSecret= "jcE48mSGrIfN4Jfo3f2QudfJi950NDHJKk1jpAqMolyGF"
        auth = tweepy.OAuthHandler(consumer_key=ConsumerKey,consumer_secret=ConsumerSecret)
        auth.set_access_token(AccessToken,AccessTokenSecret)
        api = tweepy.API(auth)
        tweets=tweepy.Cursor(api.search,q="#GC2018Weightlifting", since="2018-04-06",lang="en").items(50)
        weight = 0.00
        counter,pos,neut,neg,data = 0,0,0,0,0
        print (type(tweets))
        with open("C:\\Users\\Soumya\\testt.txt","w") as f:
            for tweet in tweets:
                counter = counter + 1
                blob = TextBlob(tweet.text)
                #print (blob)
                for sentence in blob.sentences:
                    data = data + 1
                    weight = weight + sentence.sentiment.polarity
                    if sentence.sentiment.polarity > 0:
                        pos = pos + 1
                    elif sentence.sentiment.polarity < 0:
                        neg = neg + 1
                    else:
                        neut = neut + 1
                #print(vadersentiment(tweet)+"\n")
                    #yw = tweet.text.encode("utf-8")
                    #f.write(str(yw)+"\n")
        print("Weight = {0} \nCounts = {1} \nPositive Tweets = {2} \nNegative Tweets = {3} \nNeutral Tweets = {4} \nSentences = {5}".format(weight,counter,pos,neg,neut,data))
    except tweepy.error.TweepError:
        raise

if __name__ == "__main__":
    twitterSenti()