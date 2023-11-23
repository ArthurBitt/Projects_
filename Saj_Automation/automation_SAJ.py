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
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from concurrent.futures import ThreadPoolExecutor
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
    arquivo_csv_todos = f'{path_resultados}'
     
    def __init__(self, chrome_opcao):

        self.chrome_opcao = chrome_opcao
        self.driver = webdriver.Chrome(options=chrome_opcao)

    def only_wait(self, by, value):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((by, value)))
        return element
    
    def wait_and_click(self, by, value):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, value))).click()
        return element
    
    def wait_and_send_keys(self, by, value, keys):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((by, value)))
        element.send_keys(keys)
        return element

    def processos_escreve_csv(self, csv_filename, data, mode='a'):
        with open(csv_filename, mode, newline='\n') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    for linha in data:
                        csv_writer.writerow(linha)

    def processo_epecializa_outros_processos(self, valor, temp_outros = list()):
        temp_outros.append([valor])
        return temp_outros

    def processo_loop_tag_tr(self, tbody, valor):
        # processo de loop -  transformação e armazenamento temporário dos dados capturados
        lista_loop = list()
        
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        
        for row in trs:
            new_row = []    
            new_row.append(row.text.replace("\n", ";"))
            new_row.insert(0, valor.replace(',"',';'))
            new_row = np.array(new_row)            
            new_row = new_row.T            
            lista_loop.append(new_row)

        return lista_loop

    def processo_verifica_tipo_processo(self, valor):
        processos_encontrados = 0 

        with ThreadPoolExecutor() as executor:
            # Executar consultas em paralelo para diferentes tipos de processos
            futures = [executor.submit(self.consulta_tipo_processo, valor, processo_type) for processo_type in ["Inss", "Sida", "Fgts"]]

            for future in futures:
                try:
                    future.result()  # Obter o resultado, isso também lançará exceções se ocorrerem durante a execução
                    processos_encontrados += 1
                except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
                    pass

        if processos_encontrados == 0:
            self.processo_exibe_info_prompt("OUTROS PROCESSOS", valor)
            outros = self.processo_epecializa_outros_processos(valor)
            csv_filename = f'{self.arquivo_csv_todos}Outros.csv'
            self.processos_escreve_csv(csv_filename, outros)

    def consulta_tipo_processo(self, valor, processo_type):
        try:
            tbody = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricao{processo_type.title()}Table_data']")))
            self.processo_exibe_info_prompt(processo_type.upper(), valor)
            csv_filename = f'{self.arquivo_csv_todos}{processo_type.title()}.csv'
            lista_loop = self.processo_loop_tag_tr(tbody, valor)
            self.processos_escreve_csv(csv_filename, lista_loop)
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            raise  # Propagar a exceção para ser capturada no chamador

    def processo_exibe_info_prompt(self, classe,valor):
        print(f'Classe: {classe} - {valor}')        
                    
    def auto_login(self): 
        # automatiza a autenticação do usuário
        arquivo_csv = f'{self.path_leitura}{self.nome_excel_leitura}'
        
        if not os.path.isfile(arquivo_csv):
            print("PROCESSOS NÃO ENCONTRADOS, POR FAVOR COLOQUE OS PROCESSOS NA PASTA")
            
        else:
            self.driver.get("https://saj.pgfn.fazenda.gov.br/saj/login.jsf?dswid=-46")
           
            campo_login = self.wait_and_send_keys(By.ID, "frmLogin:username","49437584877")
            campo_senha = self.wait_and_send_keys(By.ID, "frmLogin:password","melancia123")
            botao_ok = self.wait_and_click(By.ID, "frmLogin:entrar")
              
    def auto_consulta_processo(self, valor):

        try:
            self.wait_and_send_keys(By.ID, "consultarProcessoForm:numeroProcesso", valor)
        except StaleElementReferenceException:
            self.wait_and_send_keys(By.ID, "consultarProcessoForm:numeroProcesso", valor)
        try:
            self.wait_and_click(By.ID, "consultarProcessoForm:consultarProcessos")
        except (StaleElementReferenceException, ElementClickInterceptedException):
            # Se ocorrer uma exceção, tente localizar o elemento novamente antes de clicar
            self.wait_and_click(By.ID, "consultarProcessoForm:consultarProcessos")
                         
    def auto_acessa_menu_consulta(self): 
        # automatiza o acesso do menu saj para consulta de processos
        nav_bar_processo = self.only_wait(By.XPATH, "//*[@id='j_idt15:formMenus:j_idt34']/ul/li[1]/a/span[1]")
        webdriver.ActionChains(self.driver).move_to_element(nav_bar_processo).perform()

        try:
            self.wait_and_click(By.ID, "j_idt15:formMenus:menuPerfilConsulta")
        except:
            self.wait_and_click(By.ID, "j_idt15:formMenus:menuPerfilConsulta")
            
    def auto_processa_excel_leitura(self, df):
        # automatiza o conusmo dos numeros de processo no arquivo excel de leitura
        for i, row in df.iterrows():
                    valor = row.iloc[0]  
                    self.auto_consulta_processo(valor)
                  
                    self.processo_verifica_tipo_processo(valor)
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
        time.sleep(5)
        self.driver.quit()

    def run(self):
        self.auto_login() 
        self.auto_acessa_menu_consulta()
        self.processo_consultar_processos()
        

if __name__ == '__main__':
    app = mainSAJ(opcao_chrome)
    app.run()
    


     # código obsoleto
     
    # def processo_verifica_tipo_processo(self, valor):
        
    #     exceptions_count = 0

    #     for processo_type in ["Inss", "Sida", "Fgts"]:
    #         try:
    #             tbody = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricao{processo_type.title()}Table_data']")))
    #             self.processo_exibe_info_prompt(processo_type.upper(), valor)
    #             csv_filename = f'{self.arquivo_csv_todos}{processo_type.title()}.csv'
    #             lista_loop = self.processo_loop_tag_tr(tbody, valor)
    #             self.processos_escreve_csv(csv_filename, lista_loop)

    #         except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
    #             exceptions_count += 1

    #     if exceptions_count == 3:
    #         self.processo_exibe_info_prompt("OUTROS PROCESSOS", valor)
    #         outros = self.processo_epecializa_outros_processos(valor)
    #         csv_filename = f'{self.arquivo_csv_todos}Outros.csv'
    #         self.processos_escreve_csv(csv_filename,outros)
        
        # exceptions_count = 0

        # try:
        #     tbody_prev = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']")))
        #     self.processo_exibe_info_prompt("PREVIDENCIÁRIO", valor)
        #     csv_filename = self.arquivo_csv_todos_processos_prev
        #     lista_loop = self.processo_loop_tag_tr(tbody_prev, valor)
        #     self.processos_escreve_csv(csv_filename, lista_loop)

        # except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
        #     exceptions_count += 1

        # try:
        #     tbody_sida = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']")))
        #     self.processo_exibe_info_prompt("SIDA", valor)
        #     csv_filename = self.arquivo_csv_todos_processos_sida
        #     lista_loop = self.processo_loop_tag_tr(tbody_sida, valor)
        #     self.processos_escreve_csv(csv_filename, lista_loop)

        # except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
        #     exceptions_count += 1

        # try:
        #     tbody_fgts = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoFgtsTable_data']")))
        #     self.processo_exibe_info_prompt("FGTS", valor)
        #     csv_filename = self.arquivo_csv_todos_processos_fgts
        #     lista_loop = self.processo_loop_tag_tr(tbody_fgts, valor)
        #     self.processos_escreve_csv(csv_filename, lista_loop)

        # except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
        #     exceptions_count += 1

        # if exceptions_count == 3:
        #     self.processo_exibe_info_prompt("OUTROS PROCESSOS", valor)
        #     self.processo_epecializa_outros_processos(valor)