### Understanding data set
import pandas as pd
import numpy as np
import spacy


nlp = spacy.load('en_core_web_sm')


data = pd.read_csv('spam.csv',encoding='cp1252')


data.head()


data = data[['v1','v2']]


data['v1'] = data['v1'].apply(lambda x:0 if x=='ham' else 1)


data



### Demo 2 - Text Pre-Processing
def process(x):
    temp = []
    document = nlp(x.lower())
    print(document)
    for i in document:
        if i.is_stop!=True and i.is_punct!= True:
            print(i)
            temp.append(i.lemma_)
            print(temp)
        else:
            pass
        
    return (' '.join(temp))
##




data['v2'] = data['v2'].apply(lambda x: process(x))


data.head()


from sklearn.feature_extraction.text import TfidfVectorizer


vectorizer = TfidfVectorizer(analyzer='word',stop_words='english')


text_vector = vectorizer.fit_transform(data['v2'].values.tolist())


print(text_vector)


######Demo 3 - Splitting Data set


from sklearn.model_selection import train_test_split


x_train, x_test, y_train, y_test = train_test_split(text_vector.toarray(),data['v1'],test_size=0.2,random_state=20)


len(x_test)


####Demo 4 - Model Building

from sklearn.naive_bayes import BernoulliNB


modelB = BernoulliNB()
modelB.fit(x_train,y_train)
print(modelB.score(x_train,y_train))


y_predictedB = modelB.predict(x_test)


from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,y_predictedB))
