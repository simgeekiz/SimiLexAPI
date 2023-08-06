from flask import Flask, request, jsonify
from gensim.models import KeyedVectors
import gensim.downloader
import os

app = Flask(__name__)

# Load your word2vec model here
if os.path.isdir(gensim.downloader.BASE_DIR) and \
  os.path.isdir(gensim.downloader.BASE_DIR + '/word2vec-google-news-300') and \
  os.path.exists(gensim.downloader.BASE_DIR + '/word2vec-google-news-300/word2vec-google-news-300.gz'):
  model = KeyedVectors.load_word2vec_format(gensim.downloader.BASE_DIR + '/word2vec-google-news-300/word2vec-google-news-300.gz', binary=True)
else: 
  model = gensim.downloader.load('word2vec-google-news-300')

@app.route('/similar_words', methods=['GET'])
def similar_words():
  word = request.args.get('word')
  if word not in model.key_to_index:
    return jsonify({'error': 'Missing or invalid word'})
  else:
    similar = model.most_similar(word)
    return jsonify(similar)
    

@app.route('/find_similar_words', methods=['GET'])
def find_similar_words():
  threshold = float(request.args.get('similarity'))
  target_word = request.args.get('word')
  precision=4
  if not target_word:
    return jsonify({'error': 'Missing target word'})
  
  if target_word not in model.key_to_index:
    return jsonify({'error': 'Missing or invalid word'})
  
  try:
    similar_words = model.most_similar(target_word, topn=10000)
  except KeyError:
    return jsonify({'error': 'Target word not found in the model'})

  threshold = round(threshold, precision)

  filtered_words = [
    (word, similarity) for word, similarity in similar_words 
    if round(similarity, precision) == threshold
  ]

  if not filtered_words:
    filtered_words = [
      (word, model.similarity(word, target_word))
      for word, index in model.key_to_index.items()
      if round(model.similarity(word, target_word), precision) == threshold
    ]
    if not filtered_words:
      return jsonify({'error': 'No word found in the model. Please check the values'})
    
  return jsonify(filtered_words)

if __name__ == '__main__':
  app.run(debug=False)