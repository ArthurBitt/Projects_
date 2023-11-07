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

# Configuração do ChromeOptions
opcao_chrome = webdriver.ChromeOptions() 
opcao_chrome.add_argument("--start-maximized")  

class mainSAJ:  

    nome_excel_leitura = 'processos.xlsx'
    path_leitura = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Ademir_codigo\\Excel_leitura\\"
    path_resultados = "Y:\\DIAFI-PRE-TRIAGEM\\Arthur\\Repos_\\Naj_\\Saj_Ademir_codigo\\Excel_resultados\\"
    
    def __init__(self, chrome_opcao):  #Metodo Construtor
                
        self.chrome_opcao = chrome_opcao
        self.driver = webdriver.Chrome(options=chrome_opcao)
        
    def captura_infos_exec_previdenciaria(self):
        
        lista = list()
        
        time.sleep(1)
        #VERIFICAR /tbody durante o tempo de execução
        numero_processo = self.driver.find_element(By.XPATH,'//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody/tr[1]/td[2]/div/span[1]').text
        elemento1 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[1]/div").text
        elemento2 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[2]/div").text
        elemento3 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[3]/div").text
        elemento4 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[4]/div").text
        elemento5 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[5]/div").text

                                                
        lista.append(numero_processo)
        lista.append(elemento1)
        lista.append(elemento2)
        lista.append(elemento3)
        lista.append(elemento4)
        lista.append(elemento5)

        lista.append(lista)

        return lista
            
    def captura_infos_exec_fiscal_SIDA(self): 
        
        lista = list()
        time.sleep(1)
        #VERIFICAR /tbody durante o tempo de execução
        numero_processo = self.driver.find_element(By.XPATH,'//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody/tr[1]/td[2]/div/span[1]').text
        elemento1 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[1]/div").text
        elemento2 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[2]/div").text
        elemento3 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[3]/div").text
        elemento4 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[4]/div").text
        elemento5 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[5]/div").text
        elemento6 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[6]/div").text
        elemento7 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[7]/div").text
        elemento8 = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[8]/div").text

        lista.append(numero_processo)
        lista.append(elemento1)
        lista.append(elemento2)
        lista.append(elemento3)
        lista.append(elemento4)
        lista.append(elemento5)
        lista.append(elemento6)
        lista.append(elemento7)
        lista.append(elemento8)

        
        return lista

#Testando 
    def veririfica_qntd_linhas(self):
        try:
            tr = self.driver.find_elements(By.XPATH, '//*[@id="frmDetalhar:j_idt104:inscricaoSidaTable_data"]/tr')
            tr = len(tr)
            print(tr)
        except:
            tr = self.driver.find_elements(By.XPATH, '//*[@id="frmDetalhar:j_idt104:inscricaoInssTable_data"]/tr')
            
            tr = len(tr)
            print(tr)
        return tr

    def verifica_info(self,new_lista_exc_prev,new_lista_exc_fisc):
        try:
            lista_exc_fisc =  self.captura_infos_exec_fiscal_SIDA()
            new_lista_exc_fisc.append(lista_exc_fisc)
            print("CLASSE: SIDA")

        except:
            
            lista_exc_prev = self.captura_infos_exec_previdenciaria()
            new_lista_exc_prev.append(lista_exc_prev)  
            print("CLASSE: PREVIDENCIÁRIO")       
            
    def converteEmExcel(self, lista_exc_fisc,lista_exc_prev):
        df1 = pd.DataFrame(lista_exc_fisc )
        df2 = pd.DataFrame(lista_exc_prev)
        arquivo_excel_todos_processos_fisc = f'{self.path_resultados}todos_processos_SIDA.xlsx'
        arquivo_excel_todos_processos_prev = f'{self.path_resultados}todos_processos_prev.xlsx'
        df1.to_excel(arquivo_excel_todos_processos_fisc)
        df2.to_excel(arquivo_excel_todos_processos_prev)

    def converteEmExcelOutrosProcessos(self, lista_outros_processos):
        
        df3 = pd.DataFrame(lista_outros_processos)
        arquivo_excel_outros_processos = f'{self.path_resultados}todos_processos_outros.xlsx'
        df3.to_excel(arquivo_excel_outros_processos)
                
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
            new_lista_exc_fisc = []
            new_lista_exc_prev = []
        
            ListaProcessos = glob.glob(f'{self.path_leitura}*')
           
            for numeros_de_processos in ListaProcessos:
                
                df = pd.read_excel(numeros_de_processos)

                try:
                    for i, row in df.iterrows():
                        valor = row.iloc[0]  # Supondo que o número do processo está na primeira coluna do DataFrame
                        print(f'Robô mainSAJ Ademir Acabou de ler e salvar o Processo Numero: {valor}')

                        caixa_consulta = self.driver.find_element(By.ID, "consultarProcessoForm:numeroProcesso")
                        time.sleep(1)
                        
                        caixa_consulta.send_keys(valor)
                        time.sleep(1)
                        
                        botao_pesquisar = self.driver.find_element(By.ID, "consultarProcessoForm:consultarProcessos")
                        time.sleep(1)

                        botao_pesquisar.click()
                        time.sleep(1)
                        
                        
                        try:     
                            time.sleep(10000)                
                            self.verifica_info(new_lista_exc_fisc,new_lista_exc_prev)
                            #Testando 
                            # tr = self.veririfica_qntd_linhas()
                        except:
                            print("CLASSE: OUTROS PROCESSOS")
                            
                            new_lista_outros_processos.append([valor])
                            pass

                                #Testando 
                        # for i in range(0,tr):
                        #     elemento = self.driver.find_element(By.XPATH, f"//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr[{i}]/td[1]/div").text
                        #     print(elemento)
                            
                        botao_processo = self.driver.find_element(By.CLASS_NAME, "ui-menuitem-text")  
                        webdriver.ActionChains(self.driver).move_to_element(botao_processo).perform() 
                        time.sleep(1)

                        botao_pesquisar = self.driver.find_element(By.ID, "j_idt15:formMenus:menuPerfilConsulta") 
                        time.sleep(1)

                        botao_pesquisar.click()
                        time.sleep(1) 

                except NoSuchElementException:
                    continue

                except ElementClickInterceptedException:
                    continue
                    
            self.converteEmExcel(new_lista_exc_fisc,new_lista_exc_prev)
            self.converteEmExcelOutrosProcessos(new_lista_outros_processos)
            
    def run(self):
        self.loginSAJ() 
        self.acessaMenuConsultaSAJ() 
        self.consultarProcessosSAj()
        # self.driver.quit()


if __name__ == '__main__':
    app = mainSAJ(opcao_chrome)
    app.run()

     
     
