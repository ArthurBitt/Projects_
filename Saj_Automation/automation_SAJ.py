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
        

    def converteEmExcel(self, new_lista_exc_sida,new_lista_exc_prev, outros_processos):
        df1 = pd.DataFrame(new_lista_exc_sida)
        df2 = pd.DataFrame(new_lista_exc_prev)
        df3 = pd.DataFrame(outros_processos)
        df1.to_csv(self.arquivo_csv_todos_processos_sida)
        df2.to_csv(self.arquivo_csv_todos_processos_prev)
        df3.to_csv(self.arquivo_csv_outros_processos)
    #Lógica ok   - não mexer
    def captura_infos_exec_previdenciaria(self):

        lista_loop = list()
        
        tbody = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']")
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        num_processo = self.driver.find_element(By.XPATH, '//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody/tr[1]/td[2]/div/span[1]').text

        for row in trs:
            new_row = []    
            new_row.append(row.text.replace("\n", ";"))
            new_row.insert(0, num_processo.replace(' ',';'))
            new_row = np.array(new_row)            
            new_row = new_row.T            
            lista_loop.append(new_row)

        lista_loop = lista_loop   
        print(lista_loop)
            
        return lista_loop
    #Lógica Ok           
    def captura_infos_exec_fiscal_SIDA(self): 

        lista_loop = list()
        
        tbody = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']")
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        num_processo = self.driver.find_element(By.XPATH, '//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody/tr[1]/td[2]/div/span[1]').text

        for row in trs:
            new_row = []    
            new_row.append(row.text.replace("\n", ";"))
            new_row.insert(0, num_processo.replace(' ',';'))
            new_row = np.array(new_row)            
            new_row = new_row.T            
            lista_loop.append(new_row)

        lista_loop = lista_loop   
        print(lista_loop)
            
        return lista_loop

    def captura_infos_FGTS(self):

        lista_loop = list()
        
        tbody = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoFgtsTable_data']")
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        num_processo = self.driver.find_element(By.XPATH, '//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody/tr[1]/td[2]/div/span[1]').text

        for row in trs:
            new_row = []    
            new_row.append(row.text.replace("\n", ";"))
            new_row.insert(0, num_processo.replace(' ',';'))
            new_row = np.array(new_row)            
            new_row = new_row.T            
            lista_loop.append(new_row)

        lista_loop = lista_loop   
        print(lista_loop)
            
        return lista_loop

    def especializa_infos(self,valor):
        outros_processos = set()
        
        try:
            prev = self.captura_infos_exec_previdenciaria()
            csv_filename = self.arquivo_csv_todos_processos_prev
            with open(csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for linha in prev:
                    csv_writer.writerow(linha)          
            print(f"CLASSE: PREVIDENCIÁRIO - {valor}")               

        except:
            
            try:
                sida = self.captura_infos_exec_fiscal_SIDA()
                csv_filename = self.arquivo_csv_todos_processos_sida
                with open(csv_filename, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    for linha in sida:
                        csv_writer.writerow(linha)
                print(f"CLASSE: SIDA - {valor}")

            except:
                
                try:
                    fgts = self.captura_infos_FGTS()
                    csv_filename = self.arquivo_csv_todos_processos_fgts
                    with open(csv_filename, 'w', newline='') as csvfile:
                        csv_writer = csv.writer(csvfile)
                        for linha in fgts:
                            csv_writer.writerow(linha)
                    print(f"CLASSE: FGTS - {valor}")

                except:
                    outros_processos.add(valor)
                    fgts = self.captura_infos_FGTS()
                    csv_filename = self.arquivo_csv_outros_processos
                    with open(csv_filename, 'w', newline='') as csvfile:
                        csv_writer = csv.writer(csvfile)
                        for linha in outros_processos:
                            csv_writer.writerow(linha)
                    print(f"OUTROS PROCESSOS - {valor}")  

        

    # Lógica ok - - não mexer            
    def loginSAJ(self): 

        arquivo_csv = f'{self.path_leitura}{self.nome_excel_leitura}'
        
        if not os.path.isfile(arquivo_csv):
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
            
            
        ListaProcessos = glob.glob(f'{self.path_leitura}*')
        
        for numeros_de_processos in ListaProcessos:
            
            df = pd.read_excel(numeros_de_processos)
            
            try:
                for i, row in df.iterrows():
                    valor = row.iloc[0]  # Supondo que o número do processo está na primeira coluna do DataFrame
                    self.auto_consulta_processo(valor)
                    self.especializa_infos(valor)
                    self.acessaMenuConsultaSAJ()
            except NoSuchElementException:
                continue

            except ElementClickInterceptedException:
                continue


        print('Finalizando...')
        time.sleep(4)
                       
    def run(self):
        self.loginSAJ() 
        self.acessaMenuConsultaSAJ() 
        self.consultarProcessosSAj()
        self.driver.quit()


if __name__ == '__main__':
    app = mainSAJ(opcao_chrome)
    app.run()
    


     
     
