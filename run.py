from flask import render_template, Flask
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversation')
def conversation():
    return render_template('convseration-ai.html')
if __name__ == '__main__':
    app.run(debug=True)
