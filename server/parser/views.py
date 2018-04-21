from flask import Blueprint, request

from .parser import TextParser

parser_blueprint = Blueprint('parser', __name__)


@parser_blueprint.route('/parse', methods=['POST'])
def parse():
    text = request.get_json()['text']
    parser = TextParser()
    return parser.get_real_synonymous(text)
