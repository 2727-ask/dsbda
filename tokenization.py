import nltk

german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens=german_tokenizer.tokenize('Wie geht es Ihnen?  Gut, danke.')
print(german_tokens)



from nltk.corpus import stopwords
stopwords.words('english')
print stopwords.words() [620:680]
