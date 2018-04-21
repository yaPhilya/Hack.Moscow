from flask import Flask, request, jsonify
from flask_cors import CORS

cors = CORS()


def create_app() -> Flask:
    app = Flask(__name__)

    # Set pre- and post- routes
    @app.before_request
    def check_content_type():
        if (request.method == 'POST') and (not request.is_json):
            return jsonify(errors=dict(content_type='invalid')), 400

    _init_extensions(app)
    _load_blueprints(app)

    return app


def _load_blueprints(app: Flask):
    from .parser.views import parser_blueprint

    app.register_blueprint(parser_blueprint)


def _init_extensions(app: Flask):
    cors.init_app(app)
