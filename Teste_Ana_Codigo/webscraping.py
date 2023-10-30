# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from triagem import TriagemApp
import tkinter as tk
from tkinter import messagebox


# google sources
opcao_chrome = webdriver.ChromeOptions()
opcao_chrome.add_argument("--start-maximized")
opcao_chrome.add_argument("--disable-gpu")  # Corregido el nombre del argumento


# PJE Scraping Class
class WebScrape:

    def __init__(self, numProcesso, numCPF, senhaPje, chrome_opcao=opcao_chrome):

        self.__numProcesso = numProcesso
        self.__numCPF = numCPF
        self.__senhaPje = senhaPje
        self.chrome_opcao = chrome_opcao
        self.google = webdriver.Chrome(options=self.chrome_opcao)

    def start(self):
        self.google.get("https://pje2g.trf3.jus.br/pje/authenticateSSO.seam")  # Corregido el uso de comillas simples
        time.sleep(4)
        # Tirar get valores do realizar_triagem() e passar para o send()
        app = TriagemApp()
        app.run()

        #trazer a lista do return realizar_triagem() e passar valores no sendKey
        self.send_cpf()
        self.send_password()
        time.sleep(4)

    def send_numprocesso(self):
        campo_numprocesso = self.google.find_element(By.ID, "tagnumprocess")
        campo_numprocesso.send_keys(self.__numProcesso)

    def send_cpf(self):
        campo_login = self.google.find_element(By.XPATH, '//input[@id="username"]')
        campo_login.send_keys(self.__numCPF)

    def send_password(self):
        campo_senha = self.google.find_element(By.XPATH, '//input[@id="password"]')
        campo_senha.send_keys(self.__senhaPje)

    def click(self):
       #clicar botao entrar PJE
        pass

if __name__ == "__main__":
    app = WebScrape("1", "2", "3")
    app.start()
