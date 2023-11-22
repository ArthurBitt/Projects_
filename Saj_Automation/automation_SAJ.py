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
opcao_chrome = webdriver.ChromeOptions() 
opcao_chrome.add_argument("--start-maximized")  
opcao_chrome.add_argument('--disable-gpu') 

class mainSAJ:  

    #PATHS
    nome_excel_leitura = 'processos.xlsx'
    path_leitura = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Automation\\Excel_leitura\\"
    path_resultados = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Automation\\Excel_resultados\\"
    arquivo_csv_todos_processos_sida = f'{path_resultados}todos_processos_SIDA.csv'
    arquivo_csv_todos_processos_prev = f'{path_resultados}todos_processos_PREVIDENCIÁRIO.csv'
    arquivo_csv_outros_processos = f'{path_resultados}todos_processos_outros.csv'
    arquivo_csv_todos_processos_fgts = f'{path_resultados}todos_processos_FGTS.csv'
    
    def __init__(self, chrome_opcao):  #Metodo Construtor
                
        self.chrome_opcao = chrome_opcao
        self.driver = webdriver.Chrome(options=chrome_opcao)

    def processo_loop_tag_tr(self, tbody):
        # processo de loop -  transformação e armazenamento temporário dos dados capturados
        lista_loop = list()
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        num_processo = self.driver.find_element(By.XPATH, '//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody/tr[1]/td[2]/div/span[1]').text

        for row in trs:
            new_row = []    
            new_row.append(row.text.replace("\n", ";"))
            new_row.insert(0, num_processo.replace(' ',';'))
            new_row = np.array(new_row)            
            new_row = new_row.T            
            lista_loop.append(new_row)
        print(lista_loop)
        return lista_loop

    def processo_verifica(self):
         # processo_verifica o tipo de processo que esta sendo consultado e o escreve no excel pertinente
                            
        # classe_judicial = self.driver.find_element(By.XPATH, '//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody/tr[2]/td[2]').text                        
        exceptions_count = 0  

        try:
            tbody_prev = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']")
            print(f" prev ")
            csv_filename = self.arquivo_csv_todos_processos_prev
            lista_loop = self.processo_loop_tag_tr(tbody_prev)
            self.processos_escreve_csv(csv_filename, lista_loop)
        
        except NoSuchElementException:
            exceptions_count += 1 

        try:
            tbody_sida = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']")
            print(f" sida ")
            # csv_filename = self.arquivo_csv_todos_processos_sida
            # lista_loop = self.processo_loop_tag_tr(tbody_sida)
        except NoSuchElementException: 
            exceptions_count += 1  

        try:
            tbody_fgts = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoFgtsTable_data']")
            print(f" fgts ")
            # csv_filename = self.arquivo_csv_todos_processos_fgts
            # lista_loop = self.processo_loop_tag_tr(tbody_fgts)

        except NoSuchElementException:
            exceptions_count += 1  

        if exceptions_count == 3:
            self.processo_especializa_outros_processos()
            print(f" ")
            # csv_filename = self.arquivo_csv_outros_processos
            # self.processos_escreve_csv(csv_filename)
               
    def auto_login(self): 
        # automatiza a autenticação do usuário
        arquivo_csv = f'{self.path_leitura}{self.nome_excel_leitura}'
        
        if not os.path.isfile(arquivo_csv):
            print("PROCESSOS NÃO ENCONTRADOS, POR FAVOR COLOQUE OS PROCESSOS NA PASTA")
            
        else:
            self.driver.get("https://saj.pgfn.fazenda.gov.br/saj/login.jsf?dswid=-46")
            time.sleep(1)
           
            campo_login = self.driver.find_element(By.ID, "frmLogin:username")
            campo_senha = self.driver.find_element(By.ID, "frmLogin:password")
            campo_login.send_keys("49437584877")
            campo_senha.send_keys("melancia123")
            time.sleep(1)
            botao_ok = self.driver.find_element(By.ID, "frmLogin:entrar")
            time.sleep(1) 
            botao_ok.click()
            time.sleep(1)

    def auto_consulta_processo(self, valor):
        # automatiza o envio do numero de processo e o click de consulta desse numero
        caixa_consulta = self.driver.find_element(By.ID, "consultarProcessoForm:numeroProcesso")
        time.sleep(1)
        
        caixa_consulta.send_keys(valor)
        time.sleep(1)
        
        botao_pesquisar = self.driver.find_element(By.ID, "consultarProcessoForm:consultarProcessos")
        time.sleep(1)

        botao_pesquisar.click()
        time.sleep(10)
              
    def auto_acessa_menu_consulta(self): 
        # automatiza o acesso do menu saj para consulta de processos
        time.sleep(1)
        botao_processo = self.driver.find_element(By.CLASS_NAME, "ui-menuitem-text")  
        webdriver.ActionChains(self.driver).move_to_element(botao_processo).perform() # MOVE MOUSE ATÉ A LISTA 
     # TEMPO NECESSARIO
        time.sleep(1)

        botao_pesquisar = self.driver.find_element(By.ID, "j_idt15:formMenus:menuPerfilConsulta") 
        time.sleep(1)
        
        botao_pesquisar.click() 
        time.sleep(1)

    def processos_escreve_csv(self, csv_filename, data, mode='a'):
        with open(csv_filename, mode, newline='\n') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    for linha in data:
                        csv_writer.writerow(linha)

    def processo_especializa_outros_processos(self):
        print(f'OUTROS PROCESSOS')
          
    def auto_processa_excel_leitura(self, df):
        # automatiza o conusmo dos numeros de processo no arquivo excel de leitura
        for i, row in df.iterrows():
                    valor = row.iloc[0]  
                    self.auto_consulta_processo(valor)                    
                    self.processo_verifica()
                    self.auto_acessa_menu_consulta()

    def processo_consultar_processos(self):

        ListaProcessos = glob.glob(f'{self.path_leitura}*')
        
        for numeros_de_processos in ListaProcessos:
            
            df = pd.read_excel(numeros_de_processos)
            
            try:
                 self.auto_processa_excel_leitura(df)
                
            except (NoSuchElementException, ElementClickInterceptedException):
                 continue
    


        print('Finalizando...')
        time.sleep(4)
                       
    def run(self):
        self.auto_login() 
        self.auto_acessa_menu_consulta()
        self.processo_consultar_processos()
        self.driver.quit()


if __name__ == '__main__':
    app = mainSAJ(opcao_chrome)
    app.run()
    


     
     
