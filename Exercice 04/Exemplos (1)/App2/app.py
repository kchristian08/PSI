from flask import render_template, request, redirect
from flask import url_for, Flask

app = Flask(__name__)

user = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():

    if user:
        return redirect(url_for('dash'))

    return render_template('cadastro.html')

@app.route('/login', methods=['POST'])
def login():

    global user
    if user:
        return redirect(url_for('dash'))
    
    user = request.form.get('login')
    senha = request.form.get('senha')
    return redirect(url_for('dash'))
    

@app.route('/dash')
def dash():

    if not user:
        return redirect(url_for('cadastro'))

    return render_template('dash.html', user=user)

@app.route('/logout', methods=['POST'])
def logout():
    global user
    user = None
    return redirect(url_for('index'))


@app.route('/modalidade')
def modalidade():
    # somente usuário cadastrado e logado
    if not user:
        return redirect(url_for('cadastro'))
    
    if request.args:
        modalidade = request.args.get('opcao')
        return render_template(f"modalidade/{modalidade}.html")

    return render_template('modalidade/modalidade.html')
