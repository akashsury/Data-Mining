# Data-Mining

  I have used placed the documents in three folders - Text file set1, Text file set2 and Text file set3. Since, I am not able to place all the documents in the single folder(only 101 files are allowed in the folder). I mentioned this point just for the clarification because I retrieved the text files from the single folder while creating the code. The goal of this project is to find the similarities between the collection of documents. There are many applications which require to
  arrange the similar set of documents together. In google search engine, the similar kinds of articles will be put together based on 
  relevance of the documents. Due to the collection of large set of data and documents, the documents can not be analyzed and arranged 
  manually. To tackle this, data mining can be used. In this project, we are having collection of 249 documents. I have created a python 
  code using various libraries like Sklearn and Nltk to identify the similar group of documents. Using TF-IDF(Term Frequency and Inverse 
  Document Frequency), Cosine similarity, the matrix can be created with values(between 0 to 1) for each and every documents as rows and 
  words present in documents as columns. After the creation of cosine similarity matrix, if you pass any query to the document, then the 
  top 10 similar set of documents will be retrieved with values of cosine similarity.Before the creation of matrix, the preprocessing 
  operations like convertion to lowercase, Removal of Single characters, Removal of punctuations, Stemming and Lemmatization are 
  performed on the collection of documents. If you look at the code, you can see the comments to guide through it. 
  
  Finally, I have used two queries to check the working of the code
  1) "Once upon a time...there were three little pigs, who left their mummy and daddy to see the world."
  2) "There once lived a poor tailor, who had a son called Aladdin, a careless, idle boy who would do 
      nothing but play all day long in the streets with little idle boys like himself."

  I have retrieved the top 10 files which are highly similar to the queries above with the cosine similarity values.
      
 
