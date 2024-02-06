from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date
from pathlib import Path
from openpyxl import Workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path, mkdir

driver = webdriver.Chrome()
driver.maximize_window()

nomesParaPegar = [
    "idpj",
    "procdigdestaut",
    "procdigrestaut",
    "cartprecciv",
    "cumsen",
    "depos",
    "exfis",
    "caufis",
]


def tableExiste():
    try:
        driver.find_element(
            By.XPATH, '//*[@id="formExpedientes:tbExpedientes:scPendentes_table"]'
        )
        return True

    except:
        return "não"


def roda():
    try:
        x = driver.find_elements(
            By.XPATH,
            "//*[@id='formExpedientes:tbExpedientes:scPendentes_table']/tbody/tr/td",
        )[-2]
        y = driver.find_element(
            By.XPATH, "//td[@class='rich-datascr-button-dsbld rich-datascr-button'][2]"
        )

        if x == y:
            return "desabilitado"
        else:
            return "habilitado"
    except:
        return "erro"


if not path.isdir(
    f"{Path.cwd()}/Arquivos_gerados"
):  # vemos de este diretorio ja existe
    mkdir(f"{Path.cwd()}/Arquivos_gerados")  # aqui criamos a pasta caso nao exista
# Data atual
data = date.today().strftime("%d.%m.%Y")
nomeExcel = f"{Path.cwd()}/Arquivos_gerados/Extração PJE-TRF3 - {data}.xlsx"


def navegarEntreProcessos():
    try:
        tabelas = driver.find_elements(By.XPATH, "//td[@class='rich-table-cell'][2]")
        for tabela in tabelas:
            processo = tabela.find_element(
                By.CSS_SELECTOR, "div > div > div > div > a"
            ).text.split()
            exFis = processo[0].lower()
            if exFis in nomesParaPegar:
                exFis = processo[0]
                numProcess = processo[1]

                destinatario = tabela.find_elements(
                    By.CSS_SELECTOR, "div > div > div > div"
                )[1].text
                p1 = destinatario.upper().split(" X ")[0]
                p2 = destinatario.upper().split(" X ")[1]

                despacho = tabela.find_elements(
                    By.CSS_SELECTOR, "div > div > div > span"
                )[1].text
                despacho = despacho.upper().split("(")[1].replace(")", "")

                dataExpedicao = tabela.find_element(
                    By.CSS_SELECTOR, "div > div > div > span > span"
                ).text.split()[0]

                prazo = tabela.find_elements(By.CSS_SELECTOR, "div > div > div")[3].text
                prazo = prazo.split(":")[1]

                vara = tabela.find_elements(By.CSS_SELECTOR, "div > div > div > div")[
                    2
                ].text
                vara = vara.replace("/", "")

                dados = [
                    numProcess,
                    exFis,
                    vara,
                    dataExpedicao,
                    p1,
                    p2,
                    prazo,
                    despacho,
                ]
                ws.append(dados)

                print(exFis)
                print(numProcess)
                print(p1)
                print(p2)
                print(despacho)
                print(dataExpedicao)
                print(prazo)
                print(vara)
    except:
        sleep(1)
        navegarEntreProcessos()


# sites
paginaAuth = "https://pje1g.trf3.jus.br/pje/login.seam"
paginaPainel = "https://pje1g.trf3.jus.br/pje/Painel/painel_usuario/advogado.seam"

# abrir pagina
driver.get(paginaAuth)
wb = Workbook()
# trocar iframe para pegar campos para login
WebDriverWait(driver, 20).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "ssoFrame"))
)

driver.switch_to.default_content()
WebDriverWait(driver, 1000).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="j_id179"]/input[1]'))
)

# vai para página do painel
driver.get(paginaPainel)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='formAbaExpediente:listaAgrSitExp:1:j_id147']")
    )
)

# abrir caixa de entrada
botaoApenasPendentes = driver.find_element(
    By.XPATH, "//div[@id='formAbaExpediente:listaAgrSitExp:1:j_id147']"
)
botaoApenasPendentes.click()
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='formAbaExpediente:listaAgrSitExp:1:trPend:childs']")
    )
)
botaoSubsecao = driver.find_element(
    By.XPATH, "//div[@id='formAbaExpediente:listaAgrSitExp:1:trPend:childs']"
)
botaoSubsecao.click()

ws = wb.active

# entrar em cada um dos processos
while True:
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@class='col-md-8 informacoes-linha-expedientes']/div/div/a",
            )
        )
    )
    navegarEntreProcessos()
    if tableExiste():
        if roda() == "desabilitado":
            break
        else:
            driver.find_elements(
                By.XPATH,
                "//*[@id='formExpedientes:tbExpedientes:scPendentes_table']/tbody/tr/td",
            )[-2].click()
            sleep(2)
    else:
        break
wb.save(nomeExcel)
driver.quit()
print("Deu tudo certo")
