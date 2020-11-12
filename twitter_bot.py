import tweepy
import time

#cred
auth = tweepy.OAuthHandler('API key goes here', 'API secret key goes here') #replace this with tht info found in your twitter developer page
auth.set_access_token('access token key goes here','access secret token goes here') #replace this with tht info found in your twitter developer page

api = tweepy.API(auth)

#unmark comment to print our your user information
user= api.me()
#print(user)

#makes a post to your twitter page
api.update_status("Hey this is a CSGirls Meeting")

#prints out a list of people you follow
#if you want to get a list a of people that follow you instead change api.friends() to api.followers()
for follower in tweepy.Cursor(api.friends).items():
    print(follower.name)

#this part of the codes likes/ retweets tweets based on a key word
search = 'NCT' #replace word if you want to like a different post
num_tweets= 4 #controlls how many tweets you want to like

for tweet in tweepy.Cursor(api.search,search).items(num_tweets):
    try:
        print("tweet liked")
        tweet.favorite() #likes the tweet, if you want to retweet instead change to tweet.retweets()
        time.sleep(1)
    except tweepy.TweepError as e:
        print(e.reason)
    except  StopIteration:
        break

#like all the post on a user's account
tweet_account = api.user_timeline(screen_name="replace to an account you want to like/retweet") #you don't need the @. just the name of thr account is fine.
for tweet in tweet_account:
    if tweet.text[0:2] != "RT": #prevents you from likeing retweets under the post
        tweet.favorite()
        print("liked my own tweet")
