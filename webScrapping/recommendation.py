import pandas as pd
from konlpy.tag import Mecab #문장을 토큰화
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

id=4
df = pd.read_table('/content/recipe.csv', sep=',')
mecab = Mecab()
topn_number=5


df['token']=0
for i in range(0, len(df['cookstep'])):
  tmp = mecab.nouns(str(df['cookstep'][i]))
  df['token'][i] = tmp #토큰 단위로 나눠봄
documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(df['token'])]
model = Doc2Vec(documents, vector_size=100, window=3, epochs=10, min_count=0, workers=4)
inferred_doc_vec = model.infer_vector(df['token'][id])
most_similar_docs = model.docvecs.most_similar([inferred_doc_vec], topn=topn_number)
for index, similarity in most_similar_docs:
  print(f'{index}, similarity:{similarity}')
  print(documents[index])
