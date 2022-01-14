# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:43:49 2022

@author: matheus.sartor
"""
import os
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
import pickle

colunas = ['tamanho','ano','frente']
modelo = pickle.load(open('models/modelo.sav','rb'))

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return "Bom dia MLMundo!"

@app.route('/feel/<phrase>')
@basic_auth.required
def feel(phrase):
    tb = TextBlob(phrase)
    polarity = tb.sentiment.polarity
    label = 'Vibes Positivas!!' if polarity > 0 else 'Vibe Negativa cara, melhora ai!'
    return f'A polaridade de sua frase é: {polarity}. ({label})'

@app.route('/cotacao',methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return f'Preço: R${preco[0]}'
app.run(debug=True, host='0.0.0.0')