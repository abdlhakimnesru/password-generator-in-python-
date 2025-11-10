from flask import Flask, render_template, request
import random
import string
import os

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def home():
    password = ''
    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_password(length)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's assigned port
    app.run(host='0.0.0.0', port=port, debug=True)
