from dining import app

@app.route('/api/v1/')
def hello_world():
    return "Hello World"

@app.route('/')
def ligma():
    return "What is ligma?"
