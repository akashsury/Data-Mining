from os import listdir
from os.path import isfile,join
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


#from sklearn
import inflect
import string

def preprocess_1(contents):
    #Convertion to lowercase and Removal of punctuation marks,stop words,whitespaces
    con_num = inflect.engine() #For converting numbers to words
    trans = str.maketrans('','',string.punctuation)
    for i in range(len(contents)):
        contents[i] = contents[i].lower()
        contents[i] = contents[i].translate(trans)
        try:
            if(contents[i].isnumeric()):
                contents[i] = con_num.number_to_words(contents[i])
        except:
            pass
        contents[i] = contents[i].translate(trans)
#    print("Before Removing stopwords",len(contents))
    stwords = stopwords.words('english')
    contents = [i for i in contents if i not in stwords]
#    print("After Removing stopwords",len(contents))
#    print(contents)

    #Removal of single characters
    contents = [i for i in contents if(len(i)>1)]

    con = []
    #Stemming
    port = PorterStemmer()
    for i in contents:
        con.append(port.stem(i))
#    print("PorterStemmer",con)

    #Lemmatization
    lemma = WordNetLemmatizer()
    con = [lemma.lemmatize(i,pos="v") for i in con ]
#    print("Lemmatization",con)
    st = ""
    for i in con:
        st = st + " " +i
    return(st)

#TF-IDF
def TF_IDF(Docs):
    tfidf_vec = TfidfVectorizer()
    tfidf_matrix = tfidf_vec.fit_transform(Docs)
    print("TFIDF scores matrix with documents as rows and words as columns",tfidf_matrix.shape)
    return(tfidf_matrix)

def cos_similarity(mat):
    print("Inside Cosine similarity function",mat.shape)
    print("First row shape",mat[0:1].shape)
    res = mat * mat.T
    return(res)


path = r"C:\Users\akash\OneDrive\Desktop\Advanced Data Mining\Assignment\Data\Data"
files = [f for f in listdir(path) if isfile(join(path, f))]
print("Number of files", len(files))
Num_doc = len(files)
Preprocessed_docs = []
cnt = 0
for i in files:
    ch = path + "\\" + i
    f = open(ch,encoding="ascii",errors="ignore",mode='r')
    contents = f.read()
    contents = contents.split()
    con = preprocess_1(contents)
    Preprocessed_docs.append(con)
    f.close()

cs = TF_IDF(Preprocessed_docs)
result = cosine_similarity(cs,cs)
result = np.matrix(result)
with open('Cosine Similarity matrix.txt','wb') as f:
    for line in result:
        np.savetxt(f, line, fmt='%.2f')
f.close()

query = ["Once upon a time...there were three little pigs, who left their mummy and daddy to see the world.",
         "There once lived a poor tailor, who had a son called Aladdin, a careless, idle boy who would do "
         "nothing but play all day long in the streets with little idle boys like himself."]

for i in range(len(query)):
    con = query[i].split()
    con = preprocess_1(con)
    Preprocessed_docs.append(con)
    mat = TF_IDF(Preprocessed_docs)
    cos1 = cosine_similarity(mat, mat)
    print("cos1", cos1.shape)

mx = [[0,0]]*10
st,lt,resind = 249,251,[]
for j in range(st,lt):
    L = cos1[j,:]
    s = sorted(L,reverse=True)
    s = s[1:11]
    for i in range(len(L)):
        if(L[i] in s):
            resind.append([i,L[i]])


for j in range(len(resind)):
    for i in range(len(files)):
        if(resind[j][0]==i):
            resind[j][0] = files[i]
            break
First = resind[0:9]
Second = resind[10:]
First = sorted(First, key = lambda x:x[1], reverse=True)
Second = sorted(Second, key=lambda x:x[1], reverse=True)

print("Fourth Question")
print("First Query")
for i in First:
    print(i)
print("\n")
print("Second Query")
for i in Second:
    print(i)































