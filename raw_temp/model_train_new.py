import os
import io
import re
import nltk
import glob
import random
import pickle
import sklearn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

raw_data_path = "data/raw"
os.chdir(raw_data_path)
raw_files = glob.glob("*.txt")
print(raw_files)


documents= []
all_words  = []
stp = stopwords.words('english')
indata=[]
for f in raw_files:
	with io.open(f,"r",encoding="UTF-8") as t:
		try:
			indata=t.read()		
			temp=indata.splitlines()
			for p in temp:
				p = re.sub(r'[^\w\s]','',p)
				p = re.sub(" \d+", " ", p)
				p = p.replace("#", "")
				p = p.replace("@", "")
				p = p.replace("RT","")
				p = [i.lower() for i in list(set(nltk.word_tokenize(p)) - set(stp))]
				all_words+=p
				documents.append((p, f[:-4]))
		except UnicodeDecodeError:
			continue
random.shuffle(documents)

word_features = list(all_words)

print("Sample:")
print(documents[1])
print(word_features[1])


#count_vect = CountVectorizer()
#X_train_counts = count_vect.fit_transform(documents)
#X_train_counts.shape

#tfidf_transformer = TfidfTransformer()
#X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
#X_train_tfidf.shape


#text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB()),])

#text_clf = text_clf.fit(documents,)

features = tfidf.fit_transform(documents).toarray()
labels = [for f[:-4] in raw_files]
features.shape
