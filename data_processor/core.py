import pandas as pd
from pandas import DataFrame
import spacy
from collections import Counter
import plotly.graph_objects as go

#Importing spacy models
nlp=spacy.load('fr_core_news_md')
stopwords = nlp.Defaults.stop_words

print("Getting staged data")
staged_data = pd.read_csv("../staged_data.csv", sep=",", header=0, skipinitialspace = True)

print("Preparing data for wordCloud data vizualisation")
text_wc = ' '.join(staged_data['q1'].tolist())

print("Writing data for wordCloud data vizualisation")
to_write: DataFrame = pd.DataFrame({'wc': [text_wc] })
to_write.to_csv(path_or_buf = "../app_data_wc.csv")
print("Data for wordCloud vizualisation written")

print("Preparing data for wordCloud data chart")
staged_data_bbl=staged_data[['q2']]

print("Dropping NAs")
lem=staged_data_bbl.dropna()

print("Normalizing data")
lem['q2'] = lem['q2'] \
    .map(str.lower) \
    .replace(r'\n', '', regex=True) \
    .replace(r'[(),.!?\\-]', '', regex=True) \
    .str.strip()

#Building corpus
print("Building corpus for lemmatization")
text= ' '.join(lem['q2'].tolist())
doc=nlp(text)

print("Processing lemmatization")
lemmas=[token.lemma_ for token in doc if not token.is_stop]

print("Processing word count")
lists=Counter(lemmas).most_common()
res= list(filter(lambda x: x[1] > 2, lists))

to_write_lem: DataFrame = pd.DataFrame(res, columns = ['lem', 'wc'])
to_write_lem.to_csv(path_or_buf = "../app_data_lem.csv")