import time
import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import glob
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
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

# Configuração do ChromeOptions
opcao_chrome = webdriver.ChromeOptions() # argumentos para metodo construtor
opcao_chrome.add_argument("--start-maximized")  # argumeto 2 para metodo construtor
opcao_chrome.add_argument("--disable--gpu") # necessario para rodar, o arquivo .exe se não so funcionara Visual, code bebe

class SajAdemir:  
    
    def __init__(self, chrome_opcao):  #Metodo Construtor
                
        self.chrome_opcao = chrome_opcao
        self.google = webdriver.Chrome(options=chrome_opcao) # recebe argumento, bebe!
        #   self.saj_pge = SjPge() FUTURA MENTE IR BUSCAR OS DADOS LÁ DO PGE!! JA DEIXEI AQUI NO JEITO AMOR!
    
                 
    
    def captura_infos(self):
        
        lista = list()
        # Wait for up to 10 seconds
        try:
            
            elemento1 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[1]/div").text
            elemento2 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[2]/div").text
            elemento3 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[3]/div").text
            elemento4 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[4]/div").text
            elemento5 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[5]/div").text
                                                                
            
            lista.append(elemento1)
            lista.append(elemento2)
            lista.append(elemento3)
            lista.append(elemento4)
            lista.append(elemento5)

        
            # dict1 = {"Inscrição Previdênciaria": elemento1,
            #         "Data da Inscrição": elemento2,
            #         "Valor Atualizado": elemento3,
            #         "Situação da Inscrição": elemento4,
            #         "Periodo da Dívida": elemento5,
            #     "Valor Atualizado": elemento6}

        except: 
            print(".........................É SIDA......................")

            # else: 
            elemento1 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[1]/div").text
            elemento2 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[2]/div").text
            elemento3 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[3]/div").text
            elemento4 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[4]/div").text
            elemento5 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[5]/div").text
            elemento6 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[6]/div").text
            elemento7 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[7]/div").text
            elemento8 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[8]/div").text

            lista.append(elemento1)
            lista.append(elemento2)
            lista.append(elemento3)
            lista.append(elemento4)
            lista.append(elemento5)
            lista.append(elemento6)
            lista.append(elemento7)
            lista.append(elemento8)


            
            

        # except:
        #      elemento1 = self.google.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[1]/div").text

        return lista
            

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
            
            new_lista = []
        # Encontre todos os arquivos Excel que correspondem ao padrão
            ListaProcessos = glob.glob('processos*.xlsx')
            # Crie um arquivo HTML para salvar todos os processos
            for arquivo_excel in ListaProcessos:
                # Leia o arquivo Excel e armazene-o em um DataFrame
                dados_temporarios = pandas.read_excel(arquivo_excel)

                try:
                    for index, row in dados_temporarios.iterrows():
                        valor = row.iloc[0]  # Supondo que o número do processo está na primeira coluna do DataFrame
                        print(f'Robô Saj Ademir Acabou de ler e salvar o Processo Numero: {valor}')

                        caixa_consulta = self.google.find_element(By.ID, "consultarProcessoForm:numeroProcesso")
                        time.sleep(1)

                        caixa_consulta.send_keys(valor)
                        botao_consulta = self.google.find_element(By.ID, "consultarProcessoForm:consultarProcessos")
                        time.sleep(1)

                        botao_consulta.click()
                        time.sleep(1)

                        lista = self.captura_infos()
                        print(lista)

                        
                        new_lista.append(lista)

                        botao_processo = self.google.find_element(By.CLASS_NAME, "ui-menuitem-text")  # PEGA  ID DA LISTA > PROCESSO
                        webdriver.ActionChains(self.google).move_to_element(botao_processo).perform() # MOVE MOUSE ATÉ A LISTA 
                        time.sleep(1) # TEMPO NECESSARIO

                        botao_consulta = self.google.find_element(By.ID, "j_idt15:formMenus:menuPerfilConsulta") # PEGA O ITEM DA LISTA >>> CONSULTA
                        time.sleep(1) 

                        botao_consulta.click() # CLICA NO ITEM >>> CONSULTA
                        time.sleep(1) 
                
                    return new_lista
                
                except NoSuchElementException:
                    continue

                except ElementClickInterceptedException:
                    continue
            
            print(new_lista)
            df = pandas.DataFrame(new_lista)
            print(df)
            arquivo_excel_todos_processos = "todos_processos.xlsx"
            df.to_excel(arquivo_excel_todos_processos)
            
            
                    

                

        # df.to_excel("My_excel")
        # self.google.quit()

# Pge = SjPge()  JA DEIXEI AQUI NO JEITO AMOR, PRA FUTURAMENTE BUSCAR OS DADOS LA NO PGE!!     
Sj = SajAdemir(opcao_chrome)
Sj.InicioSAJ() #  dá inicio a função
Sj.SegundoPassoSaj() # chama a segunda e dai por diante.
Sj.ConsultarProcessos()


     
     
