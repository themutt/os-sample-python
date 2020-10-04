from flask import Flask
application = Flask(__name__)
from time import time
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=Path('/configs/.env'))

@application.route('/upload', methods=['POST'])
def upload():
    print('Got request')
    CODE = os.getenv('CODE')
    file = request.data
    code = request.headers['Code']
    if code == os.getenv('CODE'):
        filepath = Path(os.getenv('FOLDER')) / f'{round(time() * 1000)}.jpeg'
        with open(filepath, 'wb+') as f:
            f.write(file)
        print(f'Saved as {file}')
        return '', 200

    print(f'Request not matching code: received: {CODE} set: {code}')
    return '', 401

@application.route('/test', methods=['GET', 'POST'])
def test():
    return 'Hello', 200

if __name__ == "__main__":
    application.run()
