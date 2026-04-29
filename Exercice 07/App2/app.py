from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "chave-secreta-para-sessoes"

# Banco simples em memória
# formato: {nome: {"email": ..., "senha": ...}}
usuarios = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'usuario' in session:
        return redirect(url_for('dash'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome or not email or not senha:
            return render_template('cadastro.html', erro="Preencha todos os campos.")

        if nome in usuarios:
            return render_template('cadastro.html', erro="Esse nome de usuário já existe.")

        usuarios[nome] = {
            'email': email,
            'senha': senha
        }

        session['usuario'] = nome
        return redirect(url_for('dash'))

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'usuario' in session:
        return redirect(url_for('dash'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        if nome in usuarios and usuarios[nome]['senha'] == senha:
            session['usuario'] = nome
            return redirect(url_for('dash'))

        return render_template('login.html', erro="Nome ou senha inválidos.")

    return render_template('login.html')


@app.route('/dash')
def dash():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    return render_template('dash.html', user=session['usuario'])


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))


@app.route('/modalidade/<opcao>')
def modalidade(opcao):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    return render_template(f"modalidade/{opcao}.html")
    

if __name__ == '__main__':
    app.run(debug=True)