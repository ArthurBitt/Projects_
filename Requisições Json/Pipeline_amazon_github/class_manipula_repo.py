import requests
import base64
class Manipula_Repos:


    def __init__(self, username) :
        self.username = username
        self.acess_token = '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'
        self.api_base_url = "https://api.github.com/"
        self.headers = {'Authorization':'Beares' + self.acess_token,
                        "X-Github-Api-Version": "2022-11-28"}
        

    
    def cria_repositorio(self, nome_repo):
        data = {
            "name": nome_repo,
            "description": "Dados dos repositorios da empresa",
            "private": False
        }

        response = requests.post(f'{self.api_base_url}/user/repos', json=data, headers=self.headers)
        print(f'status_code criação do repositório {response.status_code}')

    def add_file(self, nome_repo, nome_file, path_file):
        with open(f"{path_file}", "rb") as f:
            file = f.read()


        encode_content = base64.b64encode(file)

        url = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/content'
        data = {'message':"Add file",
                "content": encode_content.decode('utf-8')}

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code criação do repositório {response.status_code}')



novo_repo = Manipula_Repos('ArthurBitt')
nome_repo = 'Repo'
novo_repo.cria_repositorio(nome_repo)
novo_repo.add_file(nome_repo, "file.csv", "path_file")
