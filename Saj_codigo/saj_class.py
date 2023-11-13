import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import glob
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

# Configuração do ChromeOptions
opcao_chrome = webdriver.ChromeOptions() # argumentos para metodo construtor
opcao_chrome.add_argument("--start-maximized")  # argumeto 2 para metodo construtor
opcao_chrome.add_argument("--disable--gpu") # necessario para rodar, o arquivo .exe se não so funcionara Visual, code bebe

class mainSAJ:  

    nome_excel_leitura = 'processos.xlsx'
    path_leitura = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Ademir_codigo\\Excel_leitura\\"
    path_resultados = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Ademir_codigo\\Excel_resultados\\"
    arquivo_csvs_outros_processos = f'{path_resultados}todos_processos_outros.csv'
    arquivo_csv_todos_processos_fisc = f'{path_resultados}todos_processos_SIDA.csv'
    arquivo_csv_todos_processos_prev = f'{path_resultados}todos_processos_prev.csv'
    
    def __init__(self, chrome_opcao):  #Metodo Construtor
                
        self.chrome_opcao = chrome_opcao
        self.driver = webdriver.Chrome(options=chrome_opcao)
        
    def captura_infos_exec_previdenciaria(self):
        

        tbody = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tbody").text
        trs = tbody.find_element(By.TAG_NAME, 'tr')

        for row in trs:
            new_row = []
            new_row.append(row.text)
            new_row = np.array(new_row)
            new_row = new_row.T

        return new_row
                    
    def captura_infos_exec_fiscal_SIDA(self): 
        
       
        tbody = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tbody").text
        trs = tbody.find_element(By.TAG_NAME, 'tr')

        for row in trs:
            new_row = []
            new_row.append(row.text)
            new_row = np.array(new_row)
            new_row = new_row.T

        return new_row
        
    def verifica_info(self):
        new_lista_exc_fisc = list()
        new_lista_exc_prev = list()
        
        try:
            new_lista_exc_fisc.append(self.captura_infos_exec_fiscal_SIDA())
            print("CLASSE: SIDA")

        except:
            
            new_lista_exc_prev.append(self.captura_infos_exec_previdenciaria())  
            print("CLASSE: PREVIDENCIÁRIO")       
            

        return new_lista_exc_fisc, new_lista_exc_prev
    
    def converteEmCSV(self, lista_exc_fisc,lista_exc_prev):
        df1 = pd.DataFrame(lista_exc_fisc )
        df2 = pd.DataFrame(lista_exc_prev)
        df1.to_csv(self.arquivo_excel_todos_processos_fisc)
        df2.to_csv(self.arquivo_excel_todos_processos_prev)

    def converteEmCSVOutrosProcessos(self, lista_outros_processos):
        
        df3 = pd.DataFrame(lista_outros_processos)
        
        df3.to_csv(self.arquivo_excel_outros_processos)
                
    def Auto_login(self): 
        arquivo_excel = f'{self.path_leitura}{self.nome_excel_leitura}'
        
        if not os.path.isfile(arquivo_excel):
            print("PROCESSOS NÃO ENCONTRADOS, POR FAVOR COLOQUE OS PROCESSOS NA PASTA")
            
        else:
            self.driver.get("https://saj.pgfn.fazenda.gov.br/saj/login.jsf?dswid=-46")
            time.sleep(1)
           
            campo_login = self.driver.find_element(By.ID, "frmLogin:username")
            campo_senha = self.driver.find_element(By.ID, "frmLogin:password")
            campo_login.send_keys("49437584877")
            campo_senha.send_keys("banana123")
            botao_ok = self.driver.find_element(By.ID, "frmLogin:entrar")
            time.sleep(1) 
            botao_ok.click()
            time.sleep(1)
              
    def Auto_acessaMenuConsulta(self): 

        time.sleep(1)
        botao_processo = self.driver.find_element(By.CLASS_NAME, "ui-menuitem-text")  
        webdriver.ActionChains(self.driver).move_to_element(botao_processo).perform() # MOVE MOUSE ATÉ A LISTA 
     
        time.sleep(1)

        botao_pesquisar = self.driver.find_element(By.ID, "j_idt15:formMenus:menuPerfilConsulta") 
        time.sleep(1)
        
        botao_pesquisar.click() 
        time.sleep(1)

    def Auto_consultarUmProcesso(self):
        ListaProcessos = glob.glob(f'{self.path_leitura}*')
        for numeros_de_processos in ListaProcessos:
            df = pd.read_excel(numeros_de_processos)
            for i, row in df.iterrows():
                        valor = row # Supondo que o número do processo está na primeira coluna do DataFrame
                        print(f'Processo: {row}')

                        caixa_consulta = self.driver.find_element(By.ID, "consultarProcessoForm:numeroProcesso")
                        time.sleep(1)
                        
                        caixa_consulta.send_keys(valor)
                        time.sleep(1)
                        
                        botao_pesquisar = self.driver.find_element(By.ID, "consultarProcessoForm:consultarProcessos")
                        time.sleep(1)

                        botao_pesquisar.click()
                        time.sleep(1)
        return valor
    
    def consultarProcessosSAj(self):
        new_lista_outros_processos = [['Número Processos']]
                       
        try:
            valor = self.Auto_consultarUmProcesso()               
               
            try:                     
                infos = self.verifica_info()
                
            except:
                print("CLASSE: OUTROS PROCESSOS")
                
                new_lista_outros_processos.append([valor])
                pass
                       
            self.Auto_acessaMenuConsulta()

        except NoSuchElementException:
            pass

        except ElementClickInterceptedException:
            pass
            
        print(infos)
            # self.converteEmCSV(new_lista_exc_fisc,new_lista_exc_prev)
            # self.converteEmCSVOutrosProcessos(new_lista_outros_processos)
            
    def run(self):
        self.Auto_login() 
        self.Auto_acessaMenuConsulta() 
        self.consultarProcessosSAj()
        # self.driver.quit()


if __name__ == '__main__':
    app = mainSAJ(opcao_chrome)
    app.run()

     
     
