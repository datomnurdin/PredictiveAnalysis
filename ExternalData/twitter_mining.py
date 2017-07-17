import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import csv
import nltk
from nltk.corpus import stopwords # Import the stop word list
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np, pylab as pl
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from stemming.porter import stem

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


def review_to_words( raw_review ):  
    letters_only = re.sub("[^a-zA-Z]", " ", raw_review) 
    words = letters_only.lower().split()                             
    stops = set(stopwords.words("english"))    
    stops = set(['ada,inikah,sampai,adakah,inilah,sana,adakan,itu,sangat,adalah,itukah,sangatlah,adanya,itulah,saya,adapun,jadi,se,agak,jangan,seandainya,agar,janganlah,sebab,akan,jika,sebagai,aku,jikalau,sebagaimana,akulah,jua,sebanyak,akupun,juapun,sebelum,al,juga,sebelummu,alangkah,kalau,sebelumnya,allah,kami,sebenarnya,amat,kamikah,secara,antara,kamipun,sedang,antaramu,kamu,sedangkan,antaranya,kamukah,sedikit,apa,kamupun,sedikitpun,apa-apa,katakan,segala,apabila,ke,sehingga,apakah,kecuali,sejak,apapun,kelak,sekalian,atas,kembali,sekalipun,atasmu,kemudian,sekarang,atasnya,kepada,sekitar,atau,kepadaku,selain,ataukah,kepadakulah,selalu,ataupun,kepadamu,selama,bagaimana,kepadanya,selama-lamanya,bagaimanakah,kepadanyalah,seluruh,bagi,kerana,seluruhnya,bagimu,kerananya,sementara,baginya,kesan,semua,bahawa,ketika,semuanya,bahawasanya,kini,semula,bahkan,kita,senantiasa,bahwa,ku,sendiri,banyak,kurang,sentiasa,banyaknya,lagi,seolah,barangsiapa,lain,seolah-olah,bawah,lalu,seorangpun,beberapa,lamanya,separuh,begitu,langsung,sepatutnya,begitupun,lebih,seperti,belaka,maha,seraya,belum,mahu,sering,belumkah,mahukah,serta,berada,mahupun,seseorang,berapa,maka,sesiapa,berikan,malah,sesuatu,beriman,mana,sesudah,berkenaan,manakah,sesudahnya,berupa,manapun,sesungguhnya,beserta,masih,sesungguhnyakah,biarpun,masing,setelah,bila,masing-masing,setiap,bilakah,melainkan,siapa,bilamana,memang,siapakah,bisa,mempunyai,sini,boleh,mendapat,situ,bukan,mendapati,situlah,bukankah,mendapatkan,suatu,bukanlah,mengadakan,sudah,dahulu,mengapa,sudahkah,dalam,mengapakah,sungguh,dalamnya,mengenai,sungguhpun,dan,menjadi,supaya,dapat,menyebabkan,tadinya,dapati,menyebabkannya,tahukah,dapatkah,mereka,tak,dapatlah,merekalah,tanpa,dari,merekapun,tanya,daripada,meskipun,tanyakanlah,daripadaku,mu,tapi,daripadamu,nescaya,telah,daripadanya,niscaya,tentang,demi,nya,tentu,demikian,olah,terdapat,demikianlah,oleh,terhadap,dengan,orang,terhadapmu,dengannya,pada,termasuk,di,padahal,terpaksa,dia,padamu,tertentu,dialah,padanya,tetapi,didapat,paling,tiada,didapati,para,tiadakah,dimanakah,pasti,tiadalah,engkau,patut,tiap,engkaukah,patutkah,tiap-tiap,engkaulah,per,tidak,engkaupun,pergilah,tidakkah,hai,perkara,tidaklah,hampir,perkaranya,turut,hampir-hampir,perlu,untuk,hanya,pernah,untukmu,hanyalah,pertama,wahai,hendak,pula,walau,hendaklah,pun,walaupun,hingga,sahaja,ya,ia,saja,yaini,iaitu,saling,yaitu,ialah,sama,yakni,ianya,sama-sama,yang,inginkah,samakah,ini,sambil'])
    meaningful_words = [w for w in words if not w in stops]  
    filtered_words = [stem(word) for word in meaningful_words if word not in stops]
    return( " ".join( filtered_words ))

tweets_data_path = 'data/twitter_final_data.txt'
with open(tweets_data_path) as file:
    tweets_data = json.load(file)

print len(tweets_data)

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
tweets['sentiment'] = map(lambda tweet: tweet['sentiment'], tweets_data)

print tweets['text'][0]

print stopwords.words("english")

tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

tweets['maybank'] = tweets['text'].apply(lambda tweet: word_in_text('maybank', tweet))
tweets['cimb'] = tweets['text'].apply(lambda tweet: word_in_text('cimb', tweet))
tweets['hong leong'] = tweets['text'].apply(lambda tweet: word_in_text('hong leong', tweet))

print tweets['maybank'].value_counts()[True]
print tweets['cimb'].value_counts()[True]
print tweets['hong leong'].value_counts()[True]

prg_langs = ['maybank', 'cimb', 'hong leong']
tweets_by_prg_lang = [tweets['maybank'].value_counts()[True], tweets['cimb'].value_counts()[True], tweets['hong leong'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: maybank vs. cimb vs. hong leong (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()

clean_review = review_to_words( tweets["text"][0] )

print "Comparision..."
print tweets["text"][0]
print clean_review

num_texts = tweets["text"].size
clean_train_reviews = []

for i in xrange( 0, num_texts ):
    clean_train_reviews.append( review_to_words( tweets["text"][i] ) )

vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000) 

train_data_features = vectorizer.fit_transform(clean_train_reviews)
train_data_features = train_data_features.toarray()

print train_data_features.shape

vocab = vectorizer.get_feature_names()
print vocab

dist = np.sum(train_data_features, axis=0)

for tag, count in zip(vocab, dist):
    print count, tag

print "Training the random forest..."

forest = RandomForestClassifier(n_estimators = 100) 
forest = forest.fit( train_data_features, tweets["sentiment"] )

test = pd.read_csv("data/testData.tsv", header=0, delimiter="\t", \
                   quoting=3 )

print test.shape

num_texts = len(test["text"])
clean_test_reviews = [] 

print "Cleaning and parsing the test set...\n"
for i in xrange(0,num_texts):
    if( (i+1) % 1000 == 0 ):
        print "Text %d of %d\n" % (i+1, num_texts)
    clean_review = review_to_words( test["text"][i] )
    clean_test_reviews.append( clean_review )

test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

result = forest.predict(test_data_features)

output = pd.DataFrame( data={"id":test["id"], "sentiment":result} )
output.to_csv( "data/Bag_of_Words_model.csv", index=False, quoting=3 )