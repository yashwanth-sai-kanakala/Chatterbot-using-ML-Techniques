# Chatterbot-using-ML-Techniques

A chatterbot is an application which communicates with the user to respond or answer their queries through verbal or textual medium of communication. It is also known as talk bot, chatterbox and artificial conversational entity. Such an application is provided with the additional information and knowledge of phonology to avoid future ambiguities in the conversations. 
A chatterbot can be built with two techniques one is via machine learning and second is via deep learning. The deep learning chatterbot requires a greater amount of data to train itself as for the machine learning chatterbot requires no training. The deep learning chatterbot is used for heavy purposes where it can provide response for any type of query. In the case of machine learning chatterbot, it requires a database to match the similarities between the user query and the data in the database for the chatterbot response.

### Text pre-processing using NLTK:
The NLP will start the pre-process of the text in vectors format because the machine learning algorithm requires the data in some sort of numerical format in order to perform the required task. The issue here is the data type of the text which is provided in a string format before pre-processing, the algorithm needs to convert the data type into vectors or some numerical form.

**Basic text pre-processing includes some functions:**

1. Converting the entire input text into lowercase, therefore the algorithm shouldn’t make any mistake with different cases of letters.

2. “ Tokenization ” is a process which converts the string of words into tokens by dividing the string into words.

The NLTK package also contains a pre-trained punkt tokenizer for English for basic operations such as:

1.  “ Noise Removal ” is the process that words other than special characters or symbols are considered as noise . These noises are removed by this function.

2.  “ Stopwords Removal ” The words which doesn’t have any meaning or extremely used common words are considered as stopwords. These stopwords will be removed by punkt tokenizer.

3. “ Stemming ” is a process of converting the inflected words into their stem or root base form(general word form). If the word is converted to base form, the meaning of the word will not change. But for some words the meaning will not exist in the dictionary as well.

4. “ Lemmatization ” is nothing but a slight variation of the stemming. The major difference is that Stemming can create a non-existent word. Whereas the lemmas is an actual word and it will overcome the stemming problem.

#### Bag of Words:

After the pre-processing stage, the algorithm should transform the words into vectors for further processing. The bag of words is a representation of text occurrence within the whole document.

It contains two things:

1.  Known words Vocabulary

2. Measure of presence of known words.


The algorithm only considers whether the words occur in the document, not where the words occur in the document. The main function of bag of words is to check whether same words occurs in the document.


### Term frequency- inverse document frequency:

The main problem of the bag of words approach is gives more score to larger documents where the term appear so many times in the document and the content of the document also not that informative.

The TF-IDF approach will overcome this issue by rescaling the frequency of the term how often came across all the documents. So that the frequent words in all documents can be penalized. This approach is known as term frequency- inverse document frequency or TF-IDF for short. The TF-IDF approach will be applied to documents or texts to obtain two real valued vectors. where

**Term-frequency:**
It is the scoring of frequency of word or term which will appear across the document.

**Inverese Document frequency:**
It is the scoring of how rare the term or word appear across all the documents. It is the inverse of term frequency.

####                                                             IDF = 1 + log(N/n)

Where, **n** is the number of documents, **t** is number of times term appeared and **N** is the number of documents.

The TF-IDF approach is often used in data mining and information retrieval. It is the measure of word or term how important and often appear in the documents.

### Cosine Similarity:

Cosine similarity is a measure of similarities between two non-zero vectors. It can be taken by the dot product of two vectors divided by their product of normalized. This will contain the cosine angle between the two non-zero vectors. Using cosine similarity, similarity between two documents can be found.

#### Cosine Similarity (d1,d2) = (d1·d2)/|d1|×|d1|








