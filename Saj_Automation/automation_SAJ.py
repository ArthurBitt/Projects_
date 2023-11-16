import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import glob
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import numpy as np
import csv

# Configuração do ChromeOptions
opcao_chrome = webdriver.ChromeOptions() # argumentos para metodo construtor
opcao_chrome.add_argument("--start-maximized")  # argumeto 2 para metodo construtor
opcao_chrome.add_argument("--disable--gpu") # necessario para rodar, o arquivo .exe se não so funcionara Visual, code bebe

class mainSAJ:  
    
    nome_excel_leitura = 'processos.xlsx'
    path_leitura = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Automation\\Excel_leitura\\"
    path_resultados = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Automation\\Excel_resultados\\"
    arquivo_excel_todos_processos_sida = f'{path_resultados}todos_processos_SIDA.csv'
    arquivo_excel_todos_processos_prev = f'{path_resultados}todos_processos_PREVIDENCIÁRIO.csv'
    arquivo_excel_outros_processos = f'{path_resultados}todos_processos_outros.csv'
    
    def __init__(self, chrome_opcao):  #Metodo Construtor
                
        self.chrome_opcao = chrome_opcao
        self.driver = webdriver.Chrome(options=chrome_opcao)

    def converteEmExcel(self, new_lista_exc_sida,new_lista_exc_prev, outros_processos):
        df1 = pd.DataFrame(new_lista_exc_sida)
        df2 = pd.DataFrame(new_lista_exc_prev)
        df3 = pd.DataFrame(outros_processos)
        df1.to_csv(self.arquivo_excel_todos_processos_sida)
        df2.to_csv(self.arquivo_excel_todos_processos_prev)
        df3.to_csv(self.arquivo_excel_outros_processos)
    #Lógica ok   - não mexer
    def captura_infos_exec_previdenciaria(self):
   
        tbody = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']")
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        
        for row in trs:

            new_row = []
            new_row.append(row.text.replace("\n", ""))
            new_row = np.array(new_row)
            new_row = new_row.T

        return new_row
    #Lógica Ok           
    def captura_infos_exec_fiscal_SIDA(self): 

        tbody = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']")
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        
        for row in trs:
            new_row = []    
            new_row.append(row.text.replace("\n", ""))
            
            new_row = np.array(new_row)            
            new_row = new_row.T

        return new_row
        
    def especializa_info(self,new_lista_exc_prev, new_lista_exc_sida, outros_processos, valor):
        
        try:
            prev = self.captura_infos_exec_previdenciaria()
            new_lista_exc_prev.append(prev)
            print(f"CLASSE: PREVIDENCIÁRIO - {valor}")   
            print(new_lista_exc_prev)
            
        except:
            pass
        
        try:
            sida = self.captura_infos_exec_fiscal_SIDA()
            new_lista_exc_sida.append(sida)
            print(f"CLASSE: SIDA - {valor}")
            print(new_lista_exc_sida)
            
        except:
            pass

        try:
            outros_processos.add(valor)
            print(f"OUTROS PROCESSOS - {valor}")
            print(outros_processos)
           
        except:
            pass                               
    # Lógica ok - - não mexer            
    def loginSAJ(self): 
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

    def auto_consulta_processo(self, valor):
        caixa_consulta = self.driver.find_element(By.ID, "consultarProcessoForm:numeroProcesso")
        time.sleep(1)
        
        caixa_consulta.send_keys(valor)
        time.sleep(1)
        
        botao_pesquisar = self.driver.find_element(By.ID, "consultarProcessoForm:consultarProcessos")
        time.sleep(1)

        botao_pesquisar.click()
        time.sleep(10)
    # Lógica ok - - não mexer          
    def acessaMenuConsultaSAJ(self): 
        time.sleep(1)
        botao_processo = self.driver.find_element(By.CLASS_NAME, "ui-menuitem-text")  
        webdriver.ActionChains(self.driver).move_to_element(botao_processo).perform() # MOVE MOUSE ATÉ A LISTA 
     # TEMPO NECESSARIO
        time.sleep(1)

        botao_pesquisar = self.driver.find_element(By.ID, "j_idt15:formMenus:menuPerfilConsulta") 
        time.sleep(1)
        
        botao_pesquisar.click() 
        time.sleep(1)

    def consultarProcessosSAj(self):
            outros_processos = set()
            new_lista_exc_sida = list()
            new_lista_exc_prev = list()
        
            ListaProcessos = glob.glob(f'{self.path_leitura}*')
           
            for numeros_de_processos in ListaProcessos:
                
                df = pd.read_excel(numeros_de_processos)
                
                try:
                    for i, row in df.iterrows():
                        valor = row.iloc[0]  # Supondo que o número do processo está na primeira coluna do DataFrame
                        self.auto_consulta_processo(valor)
                        self.especializa_info(new_lista_exc_prev,new_lista_exc_sida,outros_processos,valor)
                        self.acessaMenuConsultaSAJ()

                except NoSuchElementException:
                    continue

                except ElementClickInterceptedException:
                    continue

            self.converteEmExcel(new_lista_exc_sida,new_lista_exc_prev,outros_processos)
            print('Finalizando...')
            time.sleep(15)
                       
    def run(self):
        self.loginSAJ() 
        self.acessaMenuConsultaSAJ() 
        self.consultarProcessosSAj()
        self.driver.quit()


if __name__ == '__main__':
    app = mainSAJ(opcao_chrome)
    app.run()
    


     
     
