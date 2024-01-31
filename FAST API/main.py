from fastapi import FastAPI, Query
import requests

'''uvicorn main:app --reload
http://127.0.0.1:8000/docs
'''

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    ENDPOINT Hello World
    '''
    return {'hello' :'world'}


@app.get('/api/restaurantes/')
def get_restaurante(request : str = Query(None)):
    '''
    Endpoint que retorna o json do cardápio dos restaurantes
    '''

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