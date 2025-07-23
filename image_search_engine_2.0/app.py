from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

app = Flask(__name__)

# Load variables from .env
API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ID")

@app.route('/', methods=['GET', 'POST'])
def index():
    query = ""
    results = []
    if request.method == 'POST':
        query = request.form['query']
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&searchType=image"
        try:
            response = requests.get(url)
            print("Status Code:", response.status_code)
            results = response.json()
            if 'items' in results:
                return render_template('index.html', results=results['items'], query=query)
            else:
                return render_template('index.html', results=[], query=query)
        except Exception as e:
            print("Error:", e)
            return render_template('index.html', results=[], query=query)

    return render_template('index.html', results=[], query=query)

if __name__ == '__main__':
    app.run(debug=True)
