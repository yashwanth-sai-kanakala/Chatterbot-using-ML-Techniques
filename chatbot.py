import nltk
import numpy as np
import random
import string 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f=open('Dataset.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw) 
word_tokens = nltk.word_tokenize(raw)


lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



GREETING_INPUTS = ("hello", "hi", "greetings", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        
        
        



def response(user_response):
    Turtlebot_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    id1=vals.argsort()[0][-2]
    fl = vals.flatten()
    fl.sort()
    req_tfidf = fl[-2]
    if(req_tfidf==0):
        Turtlebot_response= Turtlebot_response+"I am sorry! Can you please repeat"
        return Turtlebot_response
    else:
        Turtlebot_response = Turtlebot_response+sent_tokens[id1]
        return Turtlebot_response,i
    
    
    
    
flag=True
print("Turtlebot: My name is Turtlebot. I will answer your queries about objectss. If you want to exit, type 'bye' ")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    xy = user_response
    xy=nltk.word_tokenize(xy)
    objects = ["person","bicycle","car","motorbike","aeroplane","bus","train","truck",
               "boat","traffic light","fire hydrant","stop sign","parking meter","bench",
               "bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe",
               "backpack","umbrella","handbag","tie","suitcase","frisbee","skis","snowboard",
               "sports ball","kite","baseball bat","baseball glove","skateboard","surfboard",
               "tennis racket","bottle","wine glass","cup","fork","knife","spoon","bowl","banana",
               "apple","sandwich","orange","broccoli","carrot","hot dog","pizza","donut","cake",
               "chair","sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse",
               "remote","keyboard","cell phone","microwave","oven","toaster","sink","refrigerator",
               "book","clock","vase","scissors","teddy bear","hair drier","toothbrush"]        
    
    for i in xy:
    	#print(i)
    	for j in objects:
    		if i==j:
    			print(i)
   			





    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Turtlebot: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("Turtlebot: "+greeting(user_response))
            else:
                print("Turtlebot: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Turtlebot: Bye! take care..")
       
  

