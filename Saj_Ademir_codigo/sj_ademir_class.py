import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import glob
import pandas 
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
    
    def __init__(self, chrome_opcao):  #Metodo Construtor
                
        self.chrome_opcao = chrome_opcao
        self.driver = webdriver.Chrome(options=chrome_opcao) # recebe argumento, bebe!
        #   self.mainSAJ_pge = SjPge() FUTURA MENTE IR BUSCAR OS DADOS LÁ DO PGE!! JA DEIXEI AQUI NO JEITO AMOR!
    
    def captura_infos_exec_previdenciaria(self):
        
        lista = list()

        time.sleep(2)

        elemento1 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[1]/div").text
        elemento2 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[2]/div").text
        elemento3 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[3]/div").text
        elemento4 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[4]/div").text
        elemento5 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[5]/div").text
                                                        
    
        lista.append(elemento1)
        lista.append(elemento2)
        lista.append(elemento3)
        lista.append(elemento4)
        lista.append(elemento5)


        return lista
            
    def captura_infos_exec_fiscal_SIDA(self):
            
            lista = list()

            time.sleep(2)

            elemento1 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[1]/div").text
            elemento2 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[2]/div").text
            elemento3 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[3]/div").text
            elemento4 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[4]/div").text
            elemento5 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[5]/div").text
            elemento6 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[6]/div").text
            elemento7 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[7]/div").text
            elemento8 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoSidaTable_data']/tr/td[8]/div").text

            lista.append(elemento1)
            lista.append(elemento2)
            lista.append(elemento3)
            lista.append(elemento4)
            lista.append(elemento5)
            lista.append(elemento6)
            lista.append(elemento7)
            lista.append(elemento8)

            return lista


            
            

        # except:
        #      elemento1 = self.driver.find_element(By.XPATH, "//*[@id='frmDetalhar:j_idt104:inscricaoInssTable_data']/tr/td[1]/div").text

    def verifica_info(self,new_lista_exc_fisc,new_lista_exc_prev):
        try:
            lista_exc_fisc = self.captura_infos_exec_previdenciaria()
            new_lista_exc_fisc.append(lista_exc_fisc)
            print(1)
        except:
             lista_exc_prev = self.captura_infos_exec_fiscal_SIDA()
             new_lista_exc_prev.append(lista_exc_prev)
             print(2)
   
    def converteEmExcel(self, new_lista_exc_fisc,new_lista_exc_prev):
        df1 = pandas.DataFrame(new_lista_exc_fisc)
        df2 = pandas.DataFrame(new_lista_exc_prev)
        arquivo_excel_todos_processos_fisc = "todos_processos_fisc.xlsx"
        arquivo_excel_todos_processos_prev = "todos_processos_prev.xlsx"
        df1.to_excel(arquivo_excel_todos_processos_fisc)
        df2.to_excel(arquivo_excel_todos_processos_prev)
         
    def loginSAJ(self): 
        arquivo_excel = "processos.xlsx"     
        if not os.path.isfile(arquivo_excel):   # VERIFICA, SE O ARQUIVO DO PROCESSOS, EXISTE SE EXISTIR DA CONTINUIDADE SE NÃO FECHA O PROGRAMA
            print("PROCESSOS NÃO ENCONTRADOS, POR FAVOR COLOQUE OS PROCESSOS NA PASTA")
            
        else:
            self.driver.get("https://saj.pgfn.fazenda.gov.br/saj/login.jsf?dswid=-46") # chama o site
            time.sleep(6)
            # alerta = 'alert("ROBÔ mainSAJ_ADEMIR > LOGUE COM TOKEN, OU CPF, VOCÊ TEM 30 SEGUNDOS PARA LOGAR, APÓS ISSO CLICAREMOS, EM ENTRAR, PARA FUNCIONAMENTO CORRETO, DEIXE CLICAR SOZINHO");' # aqui ja ta explicado
            # self.driver.execute_script(alerta) # executa o script
            campo_login = self.driver.find_element(By.ID, "frmLogin:username")
            campo_senha = self.driver.find_element(By.ID, "frmLogin:password")
            campo_login.send_keys("49437584877")
            campo_senha.send_keys("banana123")
            botao_ok = self.driver.find_element(By.ID, "frmLogin:entrar")
            time.sleep(2) 
            botao_ok.click()
            time.sleep(3)
              
    def acessaMenuConsultaSAJ(self): 

        time.sleep(3)
        botao_processo = self.driver.find_element(By.CLASS_NAME, "ui-menuitem-text")  
        webdriver.ActionChains(self.driver).move_to_element(botao_processo).perform() # MOVE MOUSE ATÉ A LISTA 
     # TEMPO NECESSARIO
        time.sleep(3)

        botao_pesquisar = self.driver.find_element(By.ID, "j_idt15:formMenus:menuPerfilConsulta") 
        time.sleep(3)
        
        botao_pesquisar.click() 
        time.sleep(3)

    def consultarProcessosSAj(self):
            
            new_lista_exc_fisc = []
            new_lista_exc_prev = []
        
            ListaProcessos = glob.glob('processos*.xlsx')
           
            for arquivo_excel in ListaProcessos:
                
                dados_temporarios = pandas.read_excel(arquivo_excel)

                try:
                    for i, row in dados_temporarios.iterrows():
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

                        self.verifica_info(new_lista_exc_fisc,new_lista_exc_prev)
                        
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
                    
            
                    

                

        # df.to_excel("My_excel")
        # self.driver.quit()

    def run(self):
        self.loginSAJ() 
        self.acessaMenuConsultaSAJ() #
        self.consultarProcessosSAj()
     

if __name__ == '__main__':
    app = mainSAJ(opcao_chrome)
    app.run()

     
     
