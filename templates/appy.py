from flask import Flask, render_template, request, redirect, session

app= Flask(_name_)
app.config['SECRET_KEY'] = 'chave-super-secreta'

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/painel")
def painel():
    if 'usuario_nome' in session:
        return render_template("painel.html", usuario_nome=session['usuario_nome'])

@app.route("/verificar", methodes=['POST'])
def verificar():
    cpf = request.form.get('cpf')
    senha = request.form.get('senha')
    
           