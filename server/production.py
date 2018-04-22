from server.application import create_app

app = create_app(settings='server.config.Production')
