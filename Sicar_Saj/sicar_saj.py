import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
import os

class Sicar_Saj:

    pagina = 'https://sida.pgfn.fazenda/sida/#/sida/login'
    pagina_busca = 'https://sida.pgfn.fazenda/sida/#/sida/consulta/busca'
    nome_arquivo_leitura = "Solicitação.xlsx"
    nome_arquivo_escrita = "Lista_PA.xlsx"
    lista_processos = []
    lista_pa = []   

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        

    def only_wait(self, by, value):
        element = WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located((by, value)))
        return element

    def wait_and_click(self, by, value):
        element = WebDriverWait(self.driver, 1000).until(EC.element_to_be_clickable((by, value))).click()
        return element

    def wait_and_send_keys(self, by, value, keys):
        element = WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located((by, value)))
        element.send_keys(keys)
        return element

    # Autenticação de login - redireciona para página busca quando autenticado ## entrada feita pelo usuário
    def auto_login(self):
        self.driver.get(self.pagina)
        self.only_wait(By.CLASS_NAME,"login-form ng-pristine ng-invalid ng-invalid-required ng-valid-maxlength")
        

    def auto_consulta(self):
        #num_inscrição_pagina_busca 
        self.wait_and_click(By.XPATH, '//div[@class="col-md-3 clickable linhaFiltroConsulta"]')
        self.wait_and_send_keys(By.XPATH, '/html/body/ng-include/article/div/div/ui-view/ui-view/section/fieldset/div/form/fieldset[1]/div[3]/div[2]/input',12214213)

if __name__ == '__main__':
    app = Sicar_Saj()       
    app.auto_login()
    

    