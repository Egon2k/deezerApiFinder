from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'YOUR_API_KEY'
API_URL = 'https://api.deezer.com/search/track'

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']

        if not search_query:
            return render_template('index.html', error='Please enter a search query.')

        params = {
            'q': search_query,
        #    'appid': API_KEY
        }
        
        try:
            response = requests.get(API_URL, params=params)
            data = response.json()
            
            # For demonstration, just passing raw data to the template
            return render_template('results.html', search_query=search_query, data=data)
        
        except requests.RequestException as e:
            return render_template('index.html', error=f'Error fetching data from API: {e}')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
