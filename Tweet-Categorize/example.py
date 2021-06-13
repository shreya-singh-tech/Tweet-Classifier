from twc import Tweetifier
import io

ques=input('Enter the Handle ')
with io.open("twc/handle_name.txt","w+") as f:
	f.write(ques)

#initialize the object
T = Tweetifier(ques, 100)

#crawl or fetch the tweets max: 3200
T.crawl()
crawled_tweets = T.tweets

#classify the tweets topic wise 
#(Multinomial Naive Bayes Classifier accuracy: 78%)
T.classify()
tweets_topic = T.topic_bucket
