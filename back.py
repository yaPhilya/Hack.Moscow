from flask import Flask, request
import TextParser

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    text = request.json['text']
    parser = TextParser()
    return parser.get_real_synonymous(text)