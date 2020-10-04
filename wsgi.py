from flask import Flask
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
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

@app.route('/test', methods=['GET', 'POST'])
def test():
    return 'Hello', 200

if __name__ == "__main__":
    app.run()
