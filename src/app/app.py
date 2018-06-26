from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import Flask
import gensim
from gensim.summarization import summarize
from gensim.summarization import keywords

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World! Try the endpoints /summary?text=yourtext or /keywords?text=yourtext'

#get embedding and return top N matches
@app.route('/summary', methods=['GET'])
def get_summary():
    try:
        input_string = request.args.get('text')
        
    except Exception as e:
        raise e

    if(not input_string):
        return(bad_request())
    else:
        summary = summarize(input_string)
        return jsonify( summary )

#get embedding and return top N matches
@app.route('/keywords', methods=['GET'])
def get_keywords():
    try:
        input_string = request.args.get('text')
        
    except Exception as e:
        raise e

    if(not input_string):
        return(bad_request())
    else:
        #return keywords
        keys = keywords(input_string, ratio=0.01)
        return jsonify( keys )

if __name__ == "__main__":
    app.run(host="0.0.0.0")

