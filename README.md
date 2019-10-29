# Data-Mining

  The goal of this project is to find the similarities between the collection of documents. There are many applications which require to
  arrange the similar set of documents together. In google search engine, the similar kinds of articles will be put together based on 
  relevance of the documents. Due to the collection of large set of data and documents, the documents can not be analyzed and arranged 
  manually. To tackle this, data mining can be used. In this project, we are having collection of 249 documents. I have created a python 
  code using various libraries like Sklearn and Nltk to identify the similar group of documents. Using TF-IDF(Term Frequency and Inverse 
  Document Frequency), Cosine similarity, the matrix can be created with values(between 0 to 1) for each and every documents as rows and 
  words present in documents as columns. After the creation of cosine similarity matrix, if you pass any query to the document, then the 
  top 10 similar set of documents will be retrieved with values of cosine similarity.Before the creation of matrix, the preprocessing 
  operations like convertion to lowercase, Removal of Single characters, Removal of punctuations, Stemming and Lemmatization are 
  performed on the collection of documents. If you look at the code, you can see the comments to guide through it.
