import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from datetime import date
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


class Saj:
    
    #PATHS
    data = date.today().strftime('%d.%m.%Y')
    nome_excel_leitura = f"Extração PJE-TRF3 - {data}.xlsx"
    path_leitura = f'{os.getcwd()}\\Arquivos_gerados\\'
    path_resultados = f'{os.getcwd()}\\Excel_resultados_SAJ\\'   
    arquivo_csv_todos = f'{path_resultados}'

    def __init__(self):

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        path_resultados_completo = os.path.join(self.path_resultados,)
        os.makedirs(path_resultados_completo, exist_ok=True)
        print(f"Diretório de resultados criado em {path_resultados_completo}")

    def only_wait(self, by, value):
        element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by, value)))
        return element

    def wait_and_click(self, by, value):
        element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((by, value))).click()
        return element

    def wait_and_send_keys(self, by, value, keys):
        element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((by, value)))
        element.send_keys(keys)
        return element

    def processos_escreve_csv(self, csv_filename, data, mode='a'):
        with open(csv_filename, mode, newline='\n') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    for linha in data:
                        csv_writer.writerow(linha)

    def processo_exibe_info_prompt(self, valor):
        print(f'Processo: {valor.replace(";","")}')

    def processo_loop_tag_tr(self, tbody, valor):
        # processo de loop -  captura no html as informações buscadas e armazena com array numpy em uma lista 
        lista_loop = list()

        trs = tbody.find_elements(By.TAG_NAME, 'tr')

        for row in trs:

            new_row = []
            new_row.append(row.text.replace("\n", ";"))
            new_row.insert(0, valor)

            new_row = np.array(new_row)
            new_row = new_row.T
            lista_loop.append(new_row)

        return lista_loop

    def captura_html_extraido_e_escreve_linha_csv(self, valor):
        try:
            # especializa o tbody utilizado,
            # 
            # quebra o programa quando processo nao tem a tabela 
            tbody = self.only_wait(By.XPATH, '//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody') 
            #define o nome do csv
            csv_filename = f'{self.path_resultados}{'saj'.title()}.csv'
            #chama o processo de captura dos html
            lista_loop = self.processo_loop_tag_tr(tbody, valor)
            #escreve uma linha com as informações no csv
            self.processos_escreve_csv(csv_filename, lista_loop)

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            raise  



    # Início Automação

    def __init__(self):

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        path_resultados_completo = os.path.join(self.path_resultados,)
        os.makedirs(path_resultados_completo, exist_ok=True)
        print(f"Diretório de resultados criado em {path_resultados_completo}")

    def auto_login(self):
        # automatiza a autenticação do usuário
        
        arquivo_csv = f'{self.path_leitura}{self.nome_excel_leitura.strip()}'
        #verifica a existência de um arquivo para leitura
        if not os.path.isfile(arquivo_csv):
            print("PROCESSOS NÃO ENCONTRADOS, POR FAVOR COLOQUE OS PROCESSOS NA PASTA")
        
        # se a verificação if retornar false, o código abre o saj
        else:
            self.driver.get("https://saj.pgfn.fazenda.gov.br/saj/login.jsf?dswid=-46")

    def auto_envia_numero_processo(self, valor):
        # automatiza a consulta e envio do valor do processo
        try:
            # realiza um bloco try para enviar o valor do processo para caixa input de consulta
            self.wait_and_send_keys(By.ID, "consultarProcessoForm:numeroProcesso", valor)
        except StaleElementReferenceException:
            self.wait_and_send_keys(By.ID, "consultarProcessoForm:numeroProcesso", valor)
        
        try:
            # realiza um bloco try para clicar no botão de consulta 
            self.wait_and_click(By.ID, "consultarProcessoForm:consultarProcessos")
        except (StaleElementReferenceException, ElementClickInterceptedException):
            
            self.wait_and_click(By.ID, "consultarProcessoForm:consultarProcessos")

    def auto_acessa_menu_consulta(self):
    # automatiza o acesso do menu saj para consulta de processos


    #OBS. Processo desenvolvido para dar continuidade a automação de consulta.
            # 1. auto_envia_numero_processo
            # 2 auto_acessa_menu_consulta

        # posiciona o cursor sobre o elemento especificado na navbar
        nav_bar_processo = self.only_wait(By.XPATH, "//*[@id='j_idt15:formMenus:j_idt34']/ul/li[1]/a/span[1]")

        webdriver.ActionChains(self.driver).move_to_element(nav_bar_processo).perform()

        try:
            #realiza um bloco try para clicar no elemento posicionado
            self.wait_and_click(By.ID, "j_idt15:formMenus:menuPerfilConsulta")
        except:
            self.wait_and_click(By.ID, "j_idt15:formMenus:menuPerfilConsulta")

    def auto_processa_a_leitura_do_excel(self, df):
    # automatiza o conusmo dos numeros de processo no arquivo excel de leitura

        # itera as linhas do dataframe
        for i, row in df.iterrows():
            # armazena o valor do número do processo consultado
            valor = row.iloc[0]
            valor = valor.strip() + ';'
            
            # chama a função que envia o número do processo
            self.auto_envia_numero_processo(valor)

            # chama função que exibe no prompt o processo consultado
            self.processo_exibe_info_prompt(valor)
            self.captura_html_extraido_e_escreve_linha_csv(valor)
            # erro ao localizar processo - button ok
            try:
                # chama função que da continuidade na automação, novamente, clicando na consulta da navbar
                self.auto_acessa_menu_consulta()
            except:
                # captura de exceção para botão de processo não encontrado
                self.wait_and_click(By.ID, 'j_idt220:btn')

    def processo_consultar_processos(self):
        # função que roda todo o processo de automação

        # lista que armazena todos os arquivos extração do pje, caso haja mais de um arquivo
        lista_arquivos = list()
        # procura todos os paths/ arquivos 
        extracao_pje_numero_processos = glob.glob(f'{self.path_leitura}{self.nome_excel_leitura}')

        # itera sobre o arquivo dentro do path
        for numero_do_processo in extracao_pje_numero_processos:
            # lê o arquivo com dataframe pandas
            df = pd.read_excel(numero_do_processo)
            # guarda o dataframe dentro da lista
            lista_arquivos.append(df)
            
            # chama a função que executa a automação do processo etl do saj
            self.auto_processa_a_leitura_do_excel(df)

            

        print('Finalizando...')
        time.sleep(5)
        self.driver.quit()

    def run(self):
        try:
            self.auto_login()
            self.auto_acessa_menu_consulta()
            self.processo_consultar_processos()
        finally:
            print('Finalizando...')
            time.sleep(5)
            self.driver.quit()

if __name__ == '__main__':
    app = Saj()
    app.run()