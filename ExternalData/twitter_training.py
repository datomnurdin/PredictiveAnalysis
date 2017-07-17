import json
import pandas as pd
from pprint import pprint

tweets_data_path = 'data/twitter_training_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        print tweet["text"]
        tweet["sentiment"] = str(raw_input('provide input (sentiment): '))
        tweets_data.append(tweet)
    except:
        continue

pprint(json.dumps(tweets_data))

file = open("data/twitter_final_data.txt","w") 
file.write(str(json.dumps(tweets_data)))
file.close()