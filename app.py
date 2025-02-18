from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

URL = "https://www.smh.com.au/"

def count_word_trump():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    text = ' '.join(soup.stripped_strings)
    trump_count = len(re.findall(r'\bTrump\b', text, re.IGNORECASE))

    return trump_count

@app.route('/')
def home():
    count = count_word_trump()
    if count is None:
        return jsonify({"error": "Failed to retrieve data"}), 500
    return jsonify({"Trump count": count})

if __name__ == '__main__':
    app.run(debug=True)
