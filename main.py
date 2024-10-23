
# main.py

from flask import Flask, request, redirect, url_for, render_template
import gemini

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        heading = gemini.generate_heading(image)
        return redirect(url_for('result', heading=heading))
    return render_template('index.html')

@app.route('/result')
def result():
    heading = request.args.get('heading')
    return render_template('result.html', heading=heading)

if __name__ == '__main__':
    app.run()
