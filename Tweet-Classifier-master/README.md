# Tweet-Classifier
---

Python Library to fetch tweets from any twitter handler and classify those fetched tweets into 6 different topics.

## Dependencies:

- nltk
- tweepy
- scikit-learn

## Usage:

First add your twitter api keys in the twc/Tweetifier.py file.

```python
from twc import Tweetifier

#initialize the object
T = Tweetifier("paraazz", 100)

#crawl or fetch the tweets max: 3200
T.crawl()
crawled_tweets = T.tweets

#classify the tweets topic wise 
#(Multinomial Naive Bayes Classifier accuracy: 78%)
T.classify()
tweets_topic = T.topic_bucket
```

## Training Dataset and Model:

Dataset was created by fetching titles of different **subreddit** relating to 6 main following categories.

- business
- politics
- entertainment


---
To refresh the dataset with new headlines, run the script in dir ``twc/data/``:
``` bash
$ python3 fetch_data.py

```
and train the model again in ``twc/``
```bash
$ python3 model_train.py
```

The classifier being used here is **Multinomial Naive Bayes Classifier** with accuracy of 92%.

**Other classifiers Accuracy (On this dataset)**:
- Naive Bayes Classifier
- SVC

    
    
    
    
    
