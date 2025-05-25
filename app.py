from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
from denuncia import Denuncia_bairro, NoBairro, inserir_bairro, buscar_denuncias_bairro
from collections import deque

app = Flask(__name__)
app.secret_key = 'batinha123' 

fila_atendimento = deque()
vetor_historico = []
vetor_denuncias = []
raiz_bairros = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        tipo = request.form['tipo']
        descricao = request.form['descricao']
        data = request.form['data']
        local = request.form['local']
        prioridade = int(request.form['prioridade'])

        denuncia = Denuncia_bairro(tipo, descricao, data, local, prioridade)
        vetor_denuncias.append(denuncia)
        fila_atendimento.append(denuncia)
        vetor_historico.append(f"Denúncia cadastrada: {tipo} - {local}")
        
        global raiz_bairros
        raiz_bairros = inserir_bairro(raiz_bairros, local, denuncia)
        
        flash('Denúncia registrada com sucesso!', 'success')
        return redirect(url_for('index'))
    
    return render_template('cadastrar.html')

@app.route('/denuncias')
def listar_denuncias():
    return render_template('denuncias.html', denuncias=vetor_denuncias)

@app.route('/fila')
def fila_atendimento_view():
    fila_ordenada = sorted(fila_atendimento, key=lambda x: x.prioridade)
    return render_template('fila.html', fila=fila_ordenada)

@app.route('/historico')
def historico():
    return render_template('historico.html', historico=vetor_historico)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        bairro = request.form['bairro']
        resultados = buscar_denuncias_bairro(raiz_bairros, bairro)
        return render_template('buscar.html', resultados=resultados, bairro=bairro)
    return render_template('buscar.html')

@app.route('/atender', methods=['POST'])
def atender():
    if not fila_atendimento:
        flash('Nenhuma denúncia na fila de atendimento.', 'warning')
        return redirect(url_for('fila_atendimento_view'))
    
    fila_ordenada = sorted(fila_atendimento, key=lambda x: x.prioridade)
    denuncia_atendida = fila_ordenada[0]
    fila_atendimento.remove(denuncia_atendida)
    vetor_historico.append(f"Denúncia atendida: {denuncia_atendida.tipo} - {denuncia_atendida.local}")
    
    flash('Denúncia atendida com sucesso!', 'success')
    return redirect(url_for('fila_atendimento_view'))

if __name__ == '__main__':
    app.run(debug=True) 