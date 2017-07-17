
import json
import pandas as pd
import csv

tweets_data_path = 'data/twitter_testing_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

# Open/create a file to append data to
csvFile = open('data/testData.tsv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile,delimiter='\t', quoting=csv.QUOTE_ALL)

count = 0

csvWriter.writerow(["id","text"])

for tweet in tweets['text']:
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([count + 1,tweet.encode('utf-8')])
    #print tweet.encode('utf-8')
    #print "\n"
    count += 1
csvFile.close()