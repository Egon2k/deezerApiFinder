from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = 'https://api.deezer.com/search/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # data requested from form
        search_query = request.form['search_query']
        search_radio = request.form['type']

        params = {
            'q': search_query,
        }
        
        try:
            response = requests.get(API_URL + search_radio, params=params)
            results = response.json()
            
            # render template with some parameter
            return render_template(search_radio + '.html', 
                                   result_query=search_query, 
                                   result_radio=search_radio,
                                   results=results)
        
        except requests.RequestException as e:
            return render_template('error.html', error=f'Error fetching data from API: {e}')

    else:
        # in case of no POST request (initial page load) render index.html with radio 
        # button "track" selected by default
        return render_template('index.html', result_radio='track')

if __name__ == '__main__':
    app.run(debug=True)
