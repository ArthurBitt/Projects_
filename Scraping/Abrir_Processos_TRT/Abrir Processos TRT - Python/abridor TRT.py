from ast import Await, Import, Not
from asyncio import current_task, wait_for
from curses import KEY_ENTER, window
from faulthandler import is_enabled
from fileinput import close
from imp import is_builtin
from importlib.resources import path
from multiprocessing.connection import wait
from multiprocessing.context import _default_context
from multiprocessing.pool import CLOSE
from operator import is_not
from pydoc import pager
from re import A
from sqlite3 import Row
from sys import maxsize
from textwrap import fill
from this import d
from threading import active_count
from tkinter import ACTIVE, PAGES, Button, Widget
from tkinter.filedialog import Open
from tkinter.tix import CELL, COLUMN
from turtle import title
from webbrowser import WindowsDefault
from h11 import CLOSED
import openpyxl
import openpyxl
from openpyxl import workbook
from openpyxl import load_workbook, workbook
import openpyxl
import pandas as pd
import pyautogui
import keyboard



from pydantic import FilePath 

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from playwright.sync_api import sync_playwright
import pyperclip
import pyperclip
from tkinter.tix import CELL, COLUMN
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.window import WindowTypes
from console.utils import wait_key, clear_line, sc
import threading as th
from selenium.common.exceptions import TimeoutException
from msvcrt import kbhit, getch




import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver = webdriver.Chrome()

window_count = len(driver.window_handles)


driver.get('https://pje.trt18.jus.br/primeirograu/login.seam')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="conteudologin"]/div[2]/div[2]/div/div[1]/a[1]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//*[@id="j_id110:btnUtilizarPjeOffice"]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//*[@id="loginAplicacaoButton"]').click()
time.sleep(2)

nome_do_arquivo = "processosTRT.xlsx"
pagina = "https://pje.trt18.jus.br/primeirograu/Painel/painel_usuario/advogado.seam?"
df = pd.read_excel(nome_do_arquivo, index_col='INDEX')



for index,row in df.iterrows():
    driver.switch_to.new_window(WindowTypes.TAB)
    driver.get('https://pje.trt18.jus.br/primeirograu/Painel/painel_usuario/advogado.seam?')
    time.sleep(2)
    campo_numero = driver.find_element(By.XPATH, '//*[@id="formLocCaix:decosuggestProcessoAdvogadoProc:suggestProcessoAdvogadoProc"]')
    campo_numero.send_keys(row["PROCESSO"]+ Keys.TAB)
    time.sleep(2)
    driver.find_element(By. XPATH, '//*[@id="formLocCaix:decosuggestProcessoAdvogadoProc:sugsuggestProcessoAdvogadoProc:suggest"]/tbody/tr[1]/td').click()
    time.sleep(2)
    driver.find_element_by_css_selector("input[value='Localizar'][id='formLocCaix:btnPesquisa']").click()
    while len(driver.window_handles) != window_count+1:
        time.sleep(0.5)
    driver.switch_to.window(driver.window_handles[0])