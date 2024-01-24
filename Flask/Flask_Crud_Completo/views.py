from flask import Flask, render_template, request, redirect, session, flash, url_for
from app import app, db
from models import User, Jogo

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login/response', methods = ['POST'])
def autentica_login():
    nickname = User.query.filter_by(nickname = request.form['nickname']).first()
    senha = User.query.filter_by(senha = request.form['senha'] ).first()
    
 # vericação reduzida // nick e senha diferente de  None, se True, o request do form é encontrado dentro da database User? 
    if nickname != None and senha != None:
        if(nickname and senha):
            session['usuario_logado'] = request.form['nickname']
            flash(session['usuario_logado'] + " " + "logado com sucesso!")
            return redirect(url_for('index'))
                
    else:
        flash("erro ao logar")
        return redirect(url_for('login'))
        
@app.route('/logout')
def logout():
    session['usuario_logado'] = None 
    flash("Logout realizado com sucesso!")
    return redirect(url_for('login'))

@app.route('/signin')
def sign_in():
    return render_template('signin.html', titulo = 'Sign In')

@app.route('/response/signin', methods = ['POST'])
def cadastra_user():
    if "usuario_logado" not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    nome = request.form['nome']
    nickname = request.form['nickname']
    senha = request.form['senha']
    user = User(nome = nome, nickname = nickname, senha = senha)

    # adicionando verificação para não duplicar cadastro
    query  = User.query.filter_by(nickname = nickname).first()
    if query:
        flash(f"{nickname} já cadastrado no sistema!")
        return redirect(url_for('login'))

    else:
        db.session.add(user)
        db.session.commit()
        flash(f"Usuário {nome} foi criado com sucesso!")
        return redirect(url_for('login'))

@app.route('/home')
def index():
    if "usuario_logado" not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    titulo = 'Jogos'
    return render_template("index.html", titulo = titulo, lista = Jogo.query.all())

@app.route('/cadastro')
def cadastro():
    if "usuario_logado" not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    titulo = 'Cadastros'
    return render_template('cadastro.html', titulo = titulo)

@app.route('/response/cadastro', methods = ['POST',])
def response():
    if "usuario_logado" not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    titulo = request.form['titulo']
    categoria = request.form['categoria']
    console = request.form['console']

    query  = Jogo.query.filter_by(jogo = titulo).first()
    
    # adicionando verificação para não duplicar cadastro
    if query:
        flash(f"{titulo} já foi cadastrado")
        return redirect(url_for('index'))
    else:

        jogo = Jogo(jogo = titulo,categoria = categoria,console = console)
        db.session.add(jogo)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/search')
def search():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    
    return render_template('search.html')

@app.route('/response/search', methods = ['POST'])
def response_search():
    if "usuario_logado" not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    
    
    jogo = request.form['jogo']
    if request.form['jogo'] == '':

        flash ('Digite o nome de um Game')
        return redirect(url_for('index'))

    query = Jogo.query.filter_by(jogo = jogo).all()
    if query == []:
        flash(f"Nenhum Titulo Encontrado ")
        return redirect(url_for('search'))  
    else:
        return render_template('search.html', lista = query, jogo = jogo)

@app.route('/editar/<int:id>')
def editar(id):
    if "usuario_logado" not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    query = Jogo.query.filter_by(id = id).all()
    return render_template('editar.html', lista = query)

@app.route('/response/editar', methods = ['POST'])
def response_editar():
    if "usuario_logado" not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    query = Jogo.query.filter_by(id = request.form['id']).first()
    query.jogo  = request.form['jogo']
    query.categoria = request.form['categoria']
    query.console = request.form['console']
    db.session.add(query)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/response/delete/<int:id>', methods = ['GET','POST'])
def delete(id):
    if "usuario_logado" not in session or session['usuario_logado'] == None:
        flash('Usuário não logado')
        return redirect('/')
    jogo = Jogo.query.get(id)

    if jogo is not None:
        db.session.delete(jogo)
        db.session.commit()
        flash('Deltetado com Sucesso')
        return redirect(url_for('index'))
    

