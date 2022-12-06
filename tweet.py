#############################################
# SMOKE DETECTOR V1.0 "SMOKY"
#
# Author: Daniel Eldan R.
# Date  : 05-12-2022
# Mail  : deldanr@gmail.com
# Name  : Tweet
# Desc  : Login the Twiteer API
############################################

#
# IMPORT BASE LIBRARIES
#
import tweepy
 
twitter_auth_keys = {
        "consumer_key"        : "9BhQl4SvIFdhXqvNKWhHoyqqj",
        "consumer_secret"     : "jYVlIFnih3xbBh02eTZd8tBTDntD4J6rnpuRU54LGVr2apUMb7",
        "access_token"        : "1598320269243961346-lZGQFDaY2NWjwR6epGS0N0ytWeo7rd",
        "access_token_secret" : "RrjREPzVc5uOPmBiSWrVvgURHwGg2dpOkJ3VdzrWR6di4"
    }
 
auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
api = tweepy.API(auth)
