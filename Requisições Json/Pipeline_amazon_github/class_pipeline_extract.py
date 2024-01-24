import requests
import pandas as pd
import time
class Pipeline:


    def __init__(self, acess_token ='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'):

        self.acess_token = acess_token
        self.base_url = f'https://api.github.com/'
        self.owner = "amzn"
        self.headers = {"Authorization":"Bearer" + self.acess_token, 
           'X-GitHub-Api-Version': '2022-11-28' }
        

    # def get_total_pages(self):
    #     url = f'{self.base_url}users/{self.owner}'

    #     response = requests.get(f'{url}', headers=self.headers)
    #     lista = list()
    #     lista.append(response.json()) 
    #     for info in lista:
    #         x = info['public_repos']
    #     print("Total Pages: ",x)
    #     time.sleep(3)
    #     return x


    def paginacao_repos(self):
        # total_pages = self.get_total_pages()
        lista_repos = list()
        for page in range(1,6):
            try:
                url = f'{self.base_url}users/{self.owner}/repos?page={page}'
                response = requests.get(url, headers = self.headers)
                lista_repos.append(response.json())            
            except:
                lista_repos.append(None)
            
            print(lista_repos)

        return lista_repos
    
    def selecao_values_names(self):
        lista = self.paginacao_repos()
        lista_nomes = list()
        for page in lista:
            for repo in page:
                try:
                    name = repo['name']
                    lista_nomes.append(name)
                
                except:
                    pass
                
        return lista_nomes
    


    def selecao_values_languages(self):
        lista = self.paginacao_repos()
        lista_lang = list()
        for page in lista:
            for repo in page:
                try:
                    language = repo['language']
                    lista_lang.append(language)
                
                except:
                    pass
                
        return lista_lang
    

    def dataframe_cria(self):
        repositorios = self.paginacao_repos()
        nomes = self.selecao_values_names(repositorios)
        linguagens = self.selecao_values_languages(repositorios)

        data = {
            "Repositorios" : repositorios,
            "Linguagens": linguagens
        }

        df = pd.DataFrame(data)

        df.to_csv("Amazon.csv")

        return data
    

    def run(self):
        obj.paginacao_repos()
        obj.selecao_values_languages()
        obj.selecao_values_names()
        obj.dataframe_cria()

if __name__ == "__main__":
    obj = Pipeline()
    obj.run()


    