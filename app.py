from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']

    # Perform regex matching
    matches = re.findall(regex_pattern, test_string)

    return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid_email = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in)$', email) is not None

    return render_template('index.html', email=email, is_valid_email=is_valid_email)

if __name__ == '__main__':
    app.run(debug=True)
