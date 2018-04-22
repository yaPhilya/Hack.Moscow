from flask_script import Manager, Server

from server.application import create_app

manager = Manager(create_app)
manager.add_command('runserver', Server(host='0.0.0.0', port=5000))

if __name__ == '__main__':
    manager.run()
