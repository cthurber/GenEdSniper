from flask import Flask
from flask import render_template
from forms import Requirement_Lookup_Form
from gen_sniper import gather_courses

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = Requirement_Lookup_Form()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
