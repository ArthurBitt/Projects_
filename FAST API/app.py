import requests
import json
import csv


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json  = response.json()
    dados_restaurantes = {}
    
    for dicionario in dados_json: 
        nome_do_restaurante = dicionario['Company'] #value nome rest
        if nome_do_restaurante not in dados_restaurantes: #se o value da key company nao estiver no dict dados restaurantes
            
            # dict(nomerestaurante = list())
            dados_restaurantes[nome_do_restaurante] = [] 

        # nomerest.append(dict) -> {nomerestaurante[{item,price,descp}]}
        dados_restaurantes[nome_do_restaurante].append({ 
            "item": dicionario['Item'], # value item
            "price": dicionario['price'], # value price
            "description": dicionario['description'] # value description
        })
else:
    print(f"Error: {response.status_code}")


# dados_restaurantes -> {nome_rest: list({item, price, description})}
# dados_restaurantes['nome_rest'] -> acessa uma lista que contem um {}
# cada lista que contem um {} possui um índex - [i]: 
# [i]: traz um dict com o value de item, price e description
print(dados_restaurantes["McDonald’s"]) # printa os dados de um restaurante do dict


# nome_do_restaurante:{item, price, description}
# para cada nome de restaurante -> dicionario = ({item,price,dscription})

for nome_do_restaurante, dicionario in dados_restaurantes.items():
    nome_arquivo = f'{nome_do_restaurante}.json'
    nome_arquivo_csv = f'{nome_do_restaurante}.csv'

    with open(nome_arquivo,'w') as file:
        json.dump(dicionario, file, indent=4)
    
    with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["item", "price", "description"])  # Escreve o cabeçalho

        # itera somente sobre o dicionário - 1 key uma coluna
        for item in dicionario:
            writer.writerow([item["item"], item["price"], item["description"]])