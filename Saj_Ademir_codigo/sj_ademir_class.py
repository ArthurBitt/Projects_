import time
import colorama
import tkinter as ademir
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import os
import glob
import re
import pandas
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from sj_pge import SjPge classe do PGE, PRA IMPORTAR, TÁ? VIDA!!


"""
Autor: Adriano Angioletto, Arthur Bittencourt
Data de Criação: 19 de setembro de 2023
Descrição: Boot, para o SAJ
"""


# Configuração do ChromeOptions
opcao_chrome = webdriver.ChromeOptions() # argumentos para metodo construtor
opcao_chrome.add_argument("--start-maximized")  # argumeto 2 para metodo construtor
opcao_chrome.add_argument("--disable--gpu") # necessario para rodar, o arquivo .exe se não so funcionara Visual, code bebe

class SajAdemir:  
    
    def __init__(self, chrome_opcao):  #Metodo Construtor
        bemvindo_bb = '''
            +===========================================================================+
            |             BEM VINDO,  Ao Robô, SAJ Ademir                               |
            |                                                                           |
            |                                                                           |
            |          Procuradoria Geral da Fazenda 3° Regiao                          |
            |                                                                           |
            |                                                                           |    
            |                                                                           |
            | Devs:  AdrianoAngioletto, Arthur Bittencourt                              |
            +===========================================================================+
            '''
        print(bemvindo_bb)
                
        self.chrome_opcao = chrome_opcao
        self.google = webdriver.Chrome(options=chrome_opcao) # recebe argumento, bebe!
        #   self.saj_pge = SjPge() FUTURA MENTE IR BUSCAR OS DADOS LÁ DO PGE!! JA DEIXEI AQUI NO JEITO AMOR!
    
                 

    def InicioSAJ(self): # FUNÇÃO PAPAI 
        arquivo_excel = "processos.xlsx"     
        if not os.path.isfile(arquivo_excel):   # VERIFICA, SE O ARQUIVO DO PROCESSOS, EXISTE SE EXISTIR DA CONTINUIDADE SE NÃO FECHA O PROGRAMA
            print(colorama.Fore.WHITE + "PROCESSOS NÃO ENCONTRADOS, POR FAVOR COLOQUE OS PROCESSOS NA PASTA")
            return 
        
        self.google.get("https://saj.pgfn.fazenda.gov.br/saj/login.jsf?dswid=3754") # chama o site
        time.sleep(10)
        # alerta = 'alert("ROBÔ SAJ_ADEMIR > LOGUE COM TOKEN, OU CPF, VOCÊ TEM 30 SEGUNDOS PARA LOGAR, APÓS ISSO CLICAREMOS, EM ENTRAR, PARA FUNCIONAMENTO CORRETO, DEIXE CLICAR SOZINHO");' # aqui ja ta explicado
        # self.google.execute_script(alerta) # executa o script
        campo_login = self.google.find_element(By.ID, "frmLogin:username")
        campo_senha = self.google.find_element(By.ID, "frmLogin:password")
        campo_login.send_keys("49437584877")
        campo_senha.send_keys("banana123")
        botao_ok = self.google.find_element(By.ID, "frmLogin:entrar")
        time.sleep(2) 
        botao_ok.click()
        time.sleep(3)
              
    def SegundoPassoSaj(self): # é a segunda parte do codigo, onde ele clica e Consulta os Processos
    
        print('Estamos Carregando, a Segunda Parte do código, para Clicar nos Processos, e Consultar')  
        botao_processo = self.google.find_element(By.CLASS_NAME, "ui-menuitem-text")  # PEGA  ID DA LISTA > PROCESSO
        webdriver.ActionChains(self.google).move_to_element(botao_processo).perform() # MOVE MOUSE ATÉ A LISTA 
     # TEMPO NECESSARIO
        botao_consulta = self.google.find_element(By.ID, "j_idt15:formMenus:menuPerfilConsulta") # PEGA O ITEM DA LISTA >>> CONSULTA
       
        botao_consulta.click() # CLICA NO ITEM >>> CONSULTA
        # TEMPO PARA RETONAR O PROCESSO.

        

    def ConsultarProcessos(self):
        # Encontre todos os arquivos Excel que correspondem ao padrão
        ListaProcessos = glob.glob('processos*.xlsx')
        # Crie um arquivo HTML para salvar todos os processos
        arquivo_html_todos_processos = "todos_processos.html"

        with open(arquivo_html_todos_processos, "w", encoding="utf-8") as arquivo_todos_processos:
            for arquivo_excel in ListaProcessos:
                # Leia o arquivo Excel e armazene-o em um DataFrame
                dados_temporarios = pandas.read_excel(arquivo_excel)

                for index, row in dados_temporarios.iterrows():
                    valor = row.iloc[0]  # Supondo que o número do processo está na primeira coluna do DataFrame
                    print(f'Robô Saj Ademir Acabou de ler e salvar o Processo Numero: {valor}')

                    caixa_consulta = self.google.find_element(By.ID, "consultarProcessoForm:numeroProcesso")
                    time.sleep(1)
                    # Insira o número do processo
                    caixa_consulta.send_keys(valor)
                    # Execute a pesquisa clicando no botão "Consultar"
                    botao_consulta = self.google.find_element(By.ID, "consultarProcessoForm:consultarProcessos")
                    time.sleep(1)
                    botao_consulta.click()
                    time.sleep(1)

                    wait = WebDriverWait(self.google, 2)  # Wait for up to 10 seconds

                    elemento1 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[1]/div"))).text
                    elemento2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[2]/div"))).text
                    elemento3 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[3]/div"))).text
                    elemento4 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[4]/div"))).text
                    elemento5 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[5]/div"))).text
                    lista = list()
                    lista.append(elemento1)
                    lista.append(elemento2)
                    lista.append(elemento3)
                    lista.append(elemento4)
                    lista.append(elemento5)

                    print(lista)
                
                    data = {'numero processo:': elemento1
                            }

                    df = pd.Dataframe(data)
                    df.to_excel('')

                    # elemento = self.google.find_element(By.XPATH,"//tbody[@id = 'frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[8]/div")
                    # print(elemento)
                
                    # Localize o elemento pelo ID
                    
                                       
                    # html_tabela = elemento.get_attribute("innerHTML")

                    # # Escreva as informações do processo no arquivo HTML
                    # arquivo_todos_processos.write(f'<h2>Processo Numero: {valor}</h2>\n')
                    # arquivo_todos_processos.write(html_tabela)
                    # arquivo_todos_processos.write('\n')  # Ad
                    # botao_processo = self.google.find_element(By.CLASS_NAME, "ui-menuitem-text")  # PEGA  ID DA LISTA > PROCESSO
                    # webdriver.ActionChains(self.google).move_to_element(botao_processo).perform() # MOVE MOUSE ATÉ A LISTA 
                    # time.sleep(1) # TEMPO NECESSARIO
                    # botao_consulta = self.google.find_element(By.ID, "j_idt15:formMenus:menuPerfilConsulta") # PEGA O ITEM DA LISTA >>> CONSULTA
                    # time.sleep(1) 
                    # botao_consulta.click() # CLICA NO ITEM >>> CONSULTA
                    # time.sleep(1) 



# Pge = SjPge()  JA DEIXEI AQUI NO JEITO AMOR, PRA FUTURAMENTE BUSCAR OS DADOS LA NO PGE!!     
Sj = SajAdemir(opcao_chrome)
Sj.InicioSAJ() #  dá inicio a função
Sj.SegundoPassoSaj() # chama a segunda e dai por diante.
Sj.ConsultarProcessos()



     
     
