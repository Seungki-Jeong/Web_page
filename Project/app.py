from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    menu = {'home': True, 'rgrs': False, 'stmt': False, 'clsf':False, 'clst': False, 'user': False}
    return render_template('home.html', menu = menu)

@app.route('/regression', methods = ['GET', 'POST'])
def regression():
    menu = {'home': False, 'rgrs': True, 'stmt': False, 'clsf':False, 'clst': False, 'user': False}
    if request.method == 'GET':
        return render_template('regression.html', menu = menu)
    else:
        slen = float(request.form['slen'])
        plen = float(request.form['plen'])
        pwid = float(request.form['pwid'])
        species = int(request.form['species'])
        swid = round(slen * 0.6183 - plen * 0.5504 + pwid * 0.5772 - species * 0.9039 + 0.9038, 3)

        iris = {'slen': slen, 'swid': swid, 'plen': plen, 'pwid': pwid, 'species': species}
        return render_template('reg_result.html', menu = menu, iris = iris)

@app.route('/sentiment')
def sentiment():
    menu = {'home': False, 'rgrs': False, 'stmt': True, 'clsf':False, 'clst': False, 'user': False}
    return render_template('sentiment.html', menu = menu)

@app.route('/classification')
def classification():
    menu = {'home': False, 'rgrs': False, 'stmt': False, 'clsf':True, 'clst': False, 'user': False}
    return render_template('classification.html', menu = menu)

@app.route('/clust')
def clustering():
    menu = {'home': False, 'rgrs': False, 'stmt': False, 'clsf':False, 'clst': True, 'user': False}
    return render_template('clustering.html', menu = menu)

@app.route('/user')
def user():
    menu = {'home': False, 'rgrs': False, 'stmt': False, 'clsf':False, 'clst': False, 'user': True}
    return render_template('user.html', menu = menu)

if __name__ == '__main__':
    app.run(debug = True)