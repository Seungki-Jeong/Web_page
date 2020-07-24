from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('01_home.html')

@app.route('/table', methods = ['GET', 'POST'])
def table():
    if request.method == 'GET':
        return render_template('05_table.html')
        
@app.route('/iris', methods = ['GET', 'POST'])
def iris():
    if request.method == 'GET':
        return render_template('12_form_iris.html')
    else:
        slen = float(request.form['slen']) * 2
        plen = float(request.form['plen']) * 2
        pwid = float(request.form['pwid']) * 2
        species = int(request.form['species']) 
        text = request.form['text']
        return render_template('12_iris-result.html', slen = slen, plen = plen, pwid = pwid, species = species, text = text)

@app.route('/project')
def project():
    return render_template('17_templates.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)

if __name__ == '__main__':
    app.run(debug = True)