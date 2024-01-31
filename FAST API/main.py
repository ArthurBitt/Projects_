from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'hello' :'world'}


@app.get('/api/restaurantes/')
def get_restaurante(request : str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json  = response.json()
        if request is None:
            return {"Dados": dados_json}
        
        dados_restaurantes = []
        for dicionario in dados_json:
            if dicionario['Company']  == request:

                dados_restaurantes.append({ 
                "item": dicionario['Item'], # value item
                "price": dicionario['price'], # value price
                "description": dicionario['description'] # value description
            
            })
            
        return {"Restaurante": request, 
            'Cardapio': dados_restaurantes}
    else:
        print(f"Error: {response.status_code}")