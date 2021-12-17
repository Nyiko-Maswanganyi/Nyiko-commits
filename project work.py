#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df=pd.read_csv (r'C:\Users\Dell\Pictures\Video Projects\Reviews.csv\Reviews.csv')
df.head()
print(df)

# Imports
import numpy as np
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# Product Scores
fig = px.histogram(df, x="Score")
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=2)
fig.update_layout(title_text='Product Review Score')
fig.show()


 
 
 
stopwords = set(STOPWORDS)
stopwords.update(["br", "href"])

#the variables I'll use to update and store text data  
store=""
store1=""
store2=""
# iterate through the csv file
for val in df.Text:
     
    # typecaste each val to string
    store+= str(val)
 
    # split the value
tokens = store.split()
    # Converts each token into lowercase
for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
comment_words= " ".join(tokens) 
wordcloud = WordCloud(
                stopwords = stopwords).generate(comment_words)
 
# plot the WordCloud image                      
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud11.png')
plt.show()

# assign reviews with score > 3 as positive sentiment
# score < 3 negative sentiment
# remove score = 3
df = df[df['Score'] != 3]
df
df['sentiment'] = df['Score'].apply(lambda rating : +1 if rating > 3 else -1)
df
# split df - positive and negative sentiment:
positive = df[df['sentiment'] == 1]
negative = df[df['sentiment'] == -1]
df
 
#always start off with positive sentiment for the wordcloud

for val in positive.Summary:
     
    # typecaste each val to string
    store1+= str(val)
 
    # split the value
tokens1 = store1.split()
    # Converts each token into lowercase
for i in range(len(tokens1)):
        tokens1[i] = tokens1[i].lower()
     
comment_words1= " ".join(tokens1) 
wordcloud = WordCloud(
                stopwords = stopwords).generate(comment_words1)
 
# plot the WordCloud image                      
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud11.png')
plt.show()

## good and great removed because they were included in negative sentiment such as 'not great' or 'not good'
stopwords.update(["br", "href","good","great"]) 

#now we do the negative sentiment

for val in negative.Summary:
     
    # typecaste each val to string
    store2+= str(val)
 
    # split the value
tokens2 = store2.split()
    # Converts each token into lowercase
for i in range(len(tokens2)):
        tokens2[i] = tokens2[i].lower()
     
comment_words2= " ".join(tokens2) 
wordcloud = WordCloud(
                stopwords = stopwords).generate(comment_words2)
 
# plot the WordCloud image                      
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud11.png')
plt.show()

#now we plot the neagtive and positive sentiment together
df['sentimentt'] = df['sentiment'].replace({-1 : 'negative'})
df['sentimentt'] = df['sentimentt'].replace({1 : 'positive'})
fig = px.histogram(df, x="sentimentt")
fig.update_traces(marker_color="indianred",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Product Sentiment')
fig.show()

#next we remove punctuation marks since they are not relevant in building our model.
df['Text'] = df['Text'].str.replace("[^a-zA-Z#]", " ")
df = df.dropna(subset=['Summary'])
df['Summary'] = df['Summary'].str.replace("[^a-zA-Z#]", " ")

#now we replace short words that are meaning less and have at most 2 letters
df['Summary'] = df['Summary'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>2]))

#now we begin splitting the data for processing
dfTest = df[['Summary','sentiment']]
dfTest.head()

# split the data into train and test set
index = df.index
df['random_number'] = np.random.randn(len(index))
train = df[df['random_number'] <= 0.8]
test = df[df['random_number'] > 0.8]

# count vectorizer:
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
train_matrix = vectorizer.fit_transform(train['Summary'])
test_matrix = vectorizer.transform(test['Summary'])

# import Logistic Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

#Split target and independent variables

X_train = train_matrix
X_test = test_matrix
y_train = train['sentiment']
y_test = test['sentiment']

#fit the model
lr.fit(X_train,y_train)

#Make predictions
predictions = lr.predict(X_test)

# find accuracy, precision, recall:
from sklearn.metrics import confusion_matrix,classification_report
new = np.asarray(y_test)
confusion_matrix(predictions,y_test)
print(classification_report(predictions,y_test))


# In[ ]:




