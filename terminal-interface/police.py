from sklearn import metrics
from sklearn import svm
from credentials import *
from tweepy import *
import pickle
import pandas

auth = OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

tweet_link = input("Enter the link to Tweet: " )

labels = {"action":0,"help":1,"other":2,"praise":3,"question":4,"report":5}
plabel = labels[input("How would you best describe the tweet? (action / help / other/ praise / question / report): ")]

tweet_id = tweet_link[tweet_link.rfind('/')+1:]

tweet = api.get_status(tweet_id)
user = tweet.user

# generate X

# text sentiment
from textblob import TextBlob
import re
text = tweet.text
text =  ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(text)).split())
polarity = TextBlob(text).sentiment.polarity

# likes, retweets, replies
likes = tweet.favorite_count
RTs = tweet.retweet_count
replies = (likes+RTs)//2

# followers, following count
followers = user.followers_count
following = user.friends_count

# verified status
verified = int(user.verified)

# account age
from datetime import datetime
age = (datetime.now() - user.created_at).days

X = [followers,following,likes,RTs,replies,verified,age,polarity,plabel]

# normalize the vector
from sklearn import preprocessing
import numpy as np
scaler = preprocessing.StandardScaler()
X = np.array([X])
x = X.reshape(1,-1)
X = scaler.fit_transform(X)

# load model and predict label
from sklearn import svm
clf = pickle.load(open("SVM.sav", 'rb'))
y_pred = clf.predict(X)
labels = {0:"chaos",1:"fact",2:"rumour"}
print("The Tweet is a", labels[y_pred[0]])

# print all likelihood values
chaos_pred = clf.predict_proba(X)[0][0]
fact_pred = clf.predict_proba(X)[0][1]
rumour_pred = clf.predict_proba(X)[0][2]
print("LIKELIHOOD")
print("CHAOS:",chaos_pred)
print("FACT:",fact_pred)
print("RUMOUR:",rumour_pred)