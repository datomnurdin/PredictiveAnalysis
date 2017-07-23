# Sentiment Analysis Tool

## Step 1

Open twitter_streaming.py, set TWITTER API credentials and setup the keyword(s) want to be stream on line 33. Run this command to stream the specific tweets.
```
python twitter_streaming.py > data/twitter_data.txt
```

![twitter streaming](https://raw.githubusercontent.com/datomnurdin/PredictiveAnalysis/master/ExternalData/image/image_1.png?token=AFKlMvFiJiV5w16jCDDAzG_tWSHexSSKks5ZfXrzwA%3D%3D)

## Step 2

Split 70:30 for data training (twitter_training_data.txt and testing (twitter_testing_data.txt) and save both into data folder.

## Step 3

Run this command to train the data. Enter 1 for positive, -1 for negative and 0 for neutral.
```
python twitter_training.py
```

![twitter training](https://raw.githubusercontent.com/datomnurdin/PredictiveAnalysis/master/ExternalData/image/image_2.png)

## Step 4

Run this command to create testing data in CSV format.
```
python twitter_testing.py
```

![twitter testing](https://raw.githubusercontent.com/datomnurdin/PredictiveAnalysis/master/ExternalData/image/image_3.png)

## Step 5

Run this command to predict the result. We are using Random Forest classifier for this case study.
```
python twitter_mining.py
```

![twitter mining](https://raw.githubusercontent.com/datomnurdin/PredictiveAnalysis/master/ExternalData/image/image_4.png)

## Step 6

Open https://predictive-analysis.herokuapp.com/ to see the result.

![data visualization](https://raw.githubusercontent.com/datomnurdin/PredictiveAnalysis/master/image/image_2.png)
