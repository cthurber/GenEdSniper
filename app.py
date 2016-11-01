from flask import Flask
from flask import render_template
from forms import ContactForm
from gen_sniper import gather_courses

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lookup', methods = ['GET', 'POST'])
def lookup():
    form = ContactForm()
    return render_template('lookup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
