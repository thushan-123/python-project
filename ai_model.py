import numpy as np
import pandas as pd
import re
import string
import pickle
from nltk.stem import PorterStemmer

# create object Porterstammer
ps = PorterStemmer()

# open pickle file //load module
with open ('static/model/model.pickle','rb') as f:
    model = pickle.load(f)


# open vocabluary.txt : set into token list 
vocab = pd.read_csv('static/model/vocabulary.txt',header=None)
tokens = vocab[0].tolist()

# open english stopwords sw is a list   use to preprocess input txt
with open('static/model/corpora/stopwords/english','r') as file:
    sw=file.read().splitlines()

# user inputs remove the punthuation : use to preprocess function
def remove_punct(text):
    for punct in string.punctuation:
        text=text.replace(punct,'')
    return text

def preprocessing(text):
    data = pd.DataFrame([text],columns=["tweet"])
    data["tweet"] = data["tweet"].apply(lambda x: " ".join(x.lower() for x in x.split()))
    data["tweet"] = data["tweet"].apply(lambda x :" ".join(re.sub(r'^https?:\/\/.*[\r\n]*','',x,flags=re.MULTILINE) for x in x.split()))
    data["tweet"] = data["tweet"].apply(remove_punct)
    data["tweet"] =data["tweet"].str.replace(r'\d+','',regex=True)
    data["tweet"] = data["tweet"].apply(lambda x : " " .join(x for x in x.split() if x not in sw))
    data["tweet"] = data["tweet"].apply(lambda x : " " .join(ps.stem(x) for x in x.split()))
    return data["tweet"]

def vectorizer(ds,vocabluary):
    vectorized_list =[]
    for sentence in ds:
        sentence_lst=np.zeros(len(vocabluary))

        for i in range(len(vocabluary)):
            if vocabluary[i] in sentence.split():
                sentence_lst[i] = 1

        vectorized_list.append(sentence_lst)
    vectorized_list_new = np.asarray(vectorized_list, dtype=np.float32)
    return vectorized_list_new

def get_predection(vectorized_txt):
    predection = model.predict(vectorized_txt)
    if predection == 1 :
        return 'negative'
    else :
        return 'positive'
    
def get_into_predicition(user_txt):
    preprocess_user_txt = preprocessing(user_txt)
    vectorized_user_txt = vectorizer(preprocess_user_txt,tokens)
    get_predect = get_predection(vectorized_user_txt)
    return get_predect

print(get_into_predicition("i hate this product"))