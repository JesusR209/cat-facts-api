from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

current_fact = ""

@app.route('/')
def index():
    global current_fact
    
    if not current_fact:
        current_fact = fetch_fact()
    
    return render_template('index.html', fact=current_fact)

@app.route('/next_fact')
def next_fact():
    global current_fact
    current_fact = fetch_fact()
    return jsonify({'fact': current_fact})

def fetch_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('fact', 'Failed to fetch cat fact')
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)

