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

class PrevidenciariaException(Exception):
    def __init__(self, message="Erro na execução previdenciária"):
        self.message = message
        super().__init__(self.message)

class mainSAJ:  
    
    nome_excel_leitura = 'processos.xlsx'
    path_leitura = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Ademir_codigo\\Excel_leitura\\"
    path_resultados = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Ademir_codigo\\Excel_resultados\\"
    
    def __init__(self, chrome_opcao):  #Metodo Construtor
                
        self.chrome_opcao = chrome_opcao
        self.driver = webdriver.Chrome(options=chrome_opcao)
         
    #Lógica ok   - não mexer
    def captura_infos_exec_previdenciaria(self):
        
        new_lista = list()
        
        tbody = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']")
        trs = tbody.find_elements(By.TAG_NAME, 'tr')

        for row in trs:

            new_row = []
            new_row.append(row.text.replace("\n", ""))
            new_row = np.array(new_row)
            new_row = new_row.T
        
        new_lista.append(new_row)

        # np.savetxt('table.csv', new_lista, delimiter=';', fmt='%s')
            
        return new_lista

    #Lógica Ok           
    def captura_infos_exec_fiscal_SIDA(self): 
        new_lista = list()
        
        tbody = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']")
    # print(tbody.text)
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
    
        for row in trs:
            new_row = []    
            new_row.append(row.text.replace("\n", ""))
            
            new_row = np.array(new_row)            
            new_row = new_row.T
            
            new_lista.append(new_row)
            
        return new_lista
            # #desse jeito ele sobreescreve
            # np.savetxt('table.csv', new_lista, delimiter=';', fmt='%s')

    #Lógica testando
    def verifica_info(self):
        
        try:
            info_sida =  self.captura_infos_exec_fiscal_SIDA()
            print("CLASSE: SIDA")

        except:
            info_prev = self.captura_infos_exec_previdenciaria()
            print("CLASSE: PREVIDENCIÁRIO")       
                
    # def converteEmExcel(self, lista_exc_fisc,lista_exc_prev):
    #     df1 = pd.DataFrame(lista_exc_fisc )
    #     df2 = pd.DataFrame(lista_exc_prev)
    #     arquivo_excel_todos_processos_fisc = f'{self.path_resultados}todos_processos_SIDA.xlsx'
    #     arquivo_excel_todos_processos_prev = f'{self.path_resultados}todos_processos_prev.xlsx'
    #     df1.to_excel(arquivo_excel_todos_processos_fisc)
    #     df2.to_excel(arquivo_excel_todos_processos_prev)

    # def converteEmExcelOutrosProcessos(self, lista_outros_processos):
        
    #     df3 = pd.DataFrame(lista_outros_processos)
    #     arquivo_excel_outros_processos = f'{self.path_resultados}todos_processos_outros.xlsx'
    #     df3.to_excel(arquivo_excel_outros_processos)

    # Lógica ok - - não mexer            
    def loginSAJ(self): 
        arquivo_excel = F'{self.path_leitura}{self.nome_excel_leitura}'
        
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
            new_lista_outros_processos = [['Número Processos']]
            new_lista_exc_sida = []
            new_lista_exc_prev = []
        
            ListaProcessos = glob.glob(f'{self.path_leitura}*')
           
            for numeros_de_processos in ListaProcessos:
                
                df = pd.read_excel(numeros_de_processos)
                
                try:
                    for i, row in df.iterrows():
                        valor = row.iloc[0]  # Supondo que o número do processo está na primeira coluna do DataFrame
                        print(f'Processo Numero: {valor}')

                        caixa_consulta = self.driver.find_element(By.ID, "consultarProcessoForm:numeroProcesso")
                        time.sleep(1)
                        
                        caixa_consulta.send_keys(valor)
                        time.sleep(1)
                        
                        botao_pesquisar = self.driver.find_element(By.ID, "consultarProcessoForm:consultarProcessos")
                        time.sleep(1)

                        botao_pesquisar.click()
                        time.sleep(10)

#Tentando trabalhar em uma exceção para separar as classes e pegar direto a nova row na 
# captura info para passar em uma lista e concerter em csv aqui

                        try:
                            self.captura_infos_exec_previdenciaria()
                        
                        except PrevidenciariaException as e:
                            # Lida com a exceção específica capturada em captura_infos_exec_previdenciaria
                            print(f"Capturou exceção de previdenciária: {e}")
                            print("PREV")
                        
                        except Exception:
                            # Se ocorrer outra exceção, executa o bloco de código a seguir
                            try:
                                self.captura_infos_exec_fiscal_SIDA()
                                print("SIDA")
                            except Exception:
                                # Captura qualquer outra exceção não especificada anteriormente
                                new_lista_outros_processos.append([valor])
                                print("OUTROS PROCESSOS")
                        
                            


                        
                        self.acessaMenuConsultaSAJ()

                except NoSuchElementException:
                    continue

                except ElementClickInterceptedException:
                    continue

            # print(new_lista_exc_prev)
            # print(new_lista_exc_sida)
            # np.savetxt('table.csv', new_list, delimiter=';', fmt='%s')
            # self.converteEmExcel(new_lista_exc_sida,new_lista_exc_prev)
            # self.converteEmExcelOutrosProcessos(new_lista_outros_processos)
            
    def run(self):
        self.loginSAJ() 
        self.acessaMenuConsultaSAJ() 
        self.consultarProcessosSAj()
        # self.driver.quit()


if __name__ == '__main__':
    app = mainSAJ(opcao_chrome)
    app.run()

     
     
