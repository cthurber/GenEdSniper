from flask import Flask
from flask import render_template,request
from forms import Requirement_Lookup_Form
from gen_sniper import gather_courses,filter_on_requirements

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = Requirement_Lookup_Form(request.form)
    if request.method == 'POST':

        form_data = []
        if form.diversity_us.data: form_data.append('diversity-us')
        if form.writing_intensive.data: form_data.append('writing-intensive')
        if form.humanities.data: form_data.append('breadth/humanities')
        if form.interdisc_breadth.data: form_data.append('breadth/interdisciplinary')
        if form.natural_sci.data: form_data.append('natural-sciences')
        if form.diversity_international.data: form_data.append('diversity-international')

        print(form_data)
        return render_template('selections.html', response_data=filter_on_requirements(form_data))
    else:
        return render_template('index.html', form=form)

@app.route('/selections')
def selections():
    return render_template('selections.html')

if __name__ == '__main__':
    app.run(debug=True)
