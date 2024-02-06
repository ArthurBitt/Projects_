import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from datetime import date
import glob
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
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

# POR FAZER
# contador de processos pra verificar se bate com a quantidade do excel


class Saj:

    # PATHS
    data = date.today().strftime("%d.%m.%Y")

    nome_excel_leitura = f"Extração PJE-TRF3 - {data}.xlsx"

    path_leitura = f"{os.getcwd()}\\Arquivos_gerados\\"

    path_resultados = f"{os.getcwd()}\\Excel_resultados_SAJ\\"

    arquivo_csv_todos = f"{path_resultados}"

    def __init__(self):

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        path_resultados_completo = os.path.join(
            self.path_resultados,
        )
        os.makedirs(path_resultados_completo, exist_ok=True)
        print(f"Diretório de resultados criado em {path_resultados_completo}")

    def only_wait(self, by, value):
        element = WebDriverWait(self.driver, 1000).until(
            EC.visibility_of_element_located((by, value))
        )
        return element

    def wait_and_click(self, by, value):
        element = (
            WebDriverWait(self.driver, 1000)
            .until(EC.element_to_be_clickable((by, value)))
            .click()
        )
        return element

    def wait_and_send_keys(self, by, value, keys):
        element = WebDriverWait(self.driver, 1000).until(
            EC.visibility_of_element_located((by, value))
        )
        element.send_keys(keys)
        return element

    def processos_escreve_csv(
        self, data, csv_filename=f"{path_resultados}processos.csv", mode="a"
    ):
        with open(csv_filename, mode, newline="\n") as csvfile:
            csv_writer = csv.writer(csvfile)
            for linha in data:
                csv_writer.writerow(linha)

    def processos_encontra_numero_de_processo_e_classe_fiscal(self):
        classe = self.only_wait(
            By.XPATH,
            '//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody/tr[1]/td[2]/div/span[1]',
        )

        valor = self.only_wait(
            By.XPATH,
            '//*[@id="frmDetalhar:j_idt104:0:pgDadosBasicos"]/tbody/tr[2]/td[2]',
        )

        return classe, valor

    def processo_exibe_info_prompt(self, classe, valor):
        print(f"Classe: {classe.text} - {valor.text}")

    def auto_login(self):
        # automatiza a autenticação do usuário
        arquivo_csv = f"{self.path_leitura}{self.nome_excel_leitura}"
        if not os.path.isfile(arquivo_csv):
            print("PROCESSOS NÃO ENCONTRADOS, POR FAVOR COLOQUE OS PROCESSOS NA PASTA")

        else:
            self.driver.get("https://saj.pgfn.fazenda.gov.br/saj/login.jsf?dswid=-46")

    def auto_consulta_processo(self, valor):

        try:
            self.wait_and_send_keys(
                By.ID, "consultarProcessoForm:numeroProcesso", valor
            )
        except StaleElementReferenceException:
            self.wait_and_send_keys(
                By.ID, "consultarProcessoForm:numeroProcesso", valor
            )
        try:
            self.wait_and_click(By.ID, "consultarProcessoForm:consultarProcessos")
        except (StaleElementReferenceException, ElementClickInterceptedException):

            self.wait_and_click(By.ID, "consultarProcessoForm:consultarProcessos")

    def auto_acessa_menu_consulta(self):
        # automatiza o acesso do menu saj para consulta de processos

        nav_bar_processo = self.only_wait(
            By.XPATH, "//*[@id='j_idt15:formMenus:j_idt34']/ul/li[1]/a/span[1]"
        )

        webdriver.ActionChains(self.driver).move_to_element(nav_bar_processo).perform()

        try:
            self.wait_and_click(By.ID, "j_idt15:formMenus:menuPerfilConsulta")
        except:
            self.wait_and_click(By.ID, "j_idt15:formMenus:menuPerfilConsulta")

    
    def auto_processa_a_leitura_do_excel(self, df):
        # automatiza o conusmo dos numeros de processo no arquivo excel de leitura
        for i, row in df.iterrows():
            valor = row.iloc[0]
            valor = valor.strip() + ";"

            self.auto_consulta_processo(valor)
            classe, valor = self.processos_encontra_numero_de_processo_e_classe_fiscal()
            dict_processos = dict(Processo = valor.text, classe = classe.text )
            
            self.processo_exibe_info_prompt(classe, valor)
            print(df)
            

            # erro ao localizar processo - button ok
            try:
                self.auto_acessa_menu_consulta()
            except:
                self.wait_and_click(By.ID, "j_idt220:btn")

    def processo_consultar_processos(self):

        ListaProcessos = glob.glob(f"{self.path_leitura}{self.nome_excel_leitura}")

        for numeros_de_processos in ListaProcessos:

            df = pd.read_excel(numeros_de_processos)

            self.auto_processa_a_leitura_do_excel(df)

        print("Finalizando...")
        time.sleep(5)
        self.driver.quit()

    def run(self):
        self.auto_login()
        self.auto_acessa_menu_consulta()
        self.processo_consultar_processos()


if __name__ == "__main__":
    app = Saj()
    app.run()
