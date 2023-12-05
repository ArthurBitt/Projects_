# Documentação SAJ

O código fornecido é um script em Python que automatiza a extração de informações de processos judiciais do sistema SAJ (Sistema de Automação da Justiça). Utiliza a biblioteca `Selenium` para interagir com o navegador Chrome e realizar a extração de dados de processos judiciais a partir de um arquivo Excel.

## Módulos e Bibliotecas Utilizados

- `time`: Módulo para manipulação de tempo.
- `webdriver` e `ChromeOptions` do `selenium`: Biblioteca para automação de interações com o navegador Chrome.
- `os`: Módulo para interação com o sistema operacional.
- `date` do `datetime`: Módulo para trabalhar com datas.
- `glob`: Módulo para encontrar todos os caminhos de arquivos que correspondem a um padrão.
- `pandas`: Biblioteca para manipulação e análise de dados.
- `expected_conditions` e `WebDriverWait` do `selenium.webdriver.support.ui`: Condições esperadas para a espera no Selenium.
- `NoSuchElementException`, `ElementClickInterceptedException`, `StaleElementReferenceException`, e `TimeoutException` do `selenium.common.exceptions`: Exceções comuns no Selenium.
- `ThreadPoolExecutor` do `concurrent.futures`: Módulo para execução de código em paralelo.
- `numpy`: Biblioteca para manipulação de arrays.
- `csv`: Módulo para manipulação de arquivos CSV.

## Observação

Certifique-se de que o Sistema PJE (Processo Judicial Eletrônico) foi executado antes do SAJ (Sistema de Automação da Justiça), pois o caminho para o diretório de leitura do Excel leva em consideração a data do documento `.xlsx` gerado.

## Classe `Saj`

### Atributos

#### `data`

- **Descrição:** A data atual formatada como string (dia.mês.ano).

#### `nome_excel_leitura`

- **Descrição:** O nome do arquivo Excel de leitura.

#### `path_leitura`

- **Descrição:** O caminho para o diretório de arquivos gerados.

#### `path_resultados`

- **Descrição:** O caminho para o diretório de resultados em Excel.

#### `arquivo_csv_todos`

- **Descrição:** O caminho para o arquivo CSV de todos os resultados.

### Métodos

```PYTHON
def __init__(self)

Argumentos:
#Nenhum.

Retorna:
#Nenhum.

Funcionalidade:
#Inicializa a instância da classe, configurando as opções do navegador Chrome e criando o diretório de resultados.
```

```PYTHON
def only_wait(self, by, value)

Argumentos:
#`by`: Método de localização do elemento.
#value`: Valor a ser procurado.

Retorna:
#`element`: Elemento encontrado.

Funcionalidade:
#Espera até que um elemento seja visível na página.

```
```PYTHON
def`wait_and_click(self, by, value)`

Argumentos:
#`by`: Método de localização do elemento.
#`value`: Valor a ser procurado.

Retorna:
#`element`: Elemento encontrado.

Funcionalidade:
#Espera até que um elemento seja clicável na página e o clica.

```
```PYTHON
def`wait_and_send_keys(self, by, value, keys)`

Argumentos:
#`by`: Método de localização do elemento.
#`value`: Valor a ser procurado.
#`keys`: Teclas a serem enviadas.

Retorna:
#`element`: Elemento encontrado.

Funcionalidade:
#Espera até que um elemento seja visível na página e envia as teclas especificadas

```
```PYTHON
def`processos_escreve_csv(self, csv_filename, data, mode='a')`

Argumentos:
#`csv_filename`: Nome do arquivo CSV.
#`data`: Dados a serem escritos.
#`mode`: Modo de abertura do arquivo ('a' para adicionar, 'w' para escrever).

Retorna:
#Nenhum.

Funcionalidade:
#Escreve dados em um arquivo CSV.

```
```PYTHON
def`processos_escreve_csv(self, csv_filename, data, mode='a')`

Argumentos:
#`csv_filename`: Nome do arquivo CSV.
#`data`: Dados a serem escritos.
#`mode`: Modo de abertura do arquivo ('a' para adicionar, 'w' para escrever).

Retorna:
#Nenhum.

Funcionalidade:
#Escreve dados em um arquivo CSV.

```
```PYTHON
def processo_epecializa_outros_processos(self, valor, temp_outros=list())`

Argumentos:
# valor: Valor a ser processado.
# temp_outros: Lista temporária para armazenamento.

Retorna:
#temp_outros: Lista atualizada.

Funcionalidade:
#Especializa outros processos e os armazena temporariamente.

```
```PYTHON
def processo_loop_tag_tr(self, tbody, valor)

Argumentos:
#tbody: Elemento tbody.
#valor: Valor associado ao processo.

Retorna:
#lista_loop: Lista com os dados temporários.

Funcionalidade:
#Realiza um loop sobre as tags 'tr' e armazena temporariamente os dados capturados.

```
```PYTHON
def processo_verifica_tipo_processo(self, valor)

Argumentos:
#valor: Valor associado ao processo.

Retorna:
#Nenhum.

Funcionalidade:
#Verifica o tipo de processo e inicia consultas em paralelo.

```
```PYTHON
def consulta_tipo_processo(self, valor, processo_type)

#Argumentos:
#valor: Valor associado ao processo.
#processo_type: Tipo específico de processo.

Retorna:
#Nenhum.

Funcionalidade:
#Consulta um tipo específico de processo e armazena temporariamente os dados.


```
```PYTHON
def processo_exibe_info_prompt(self, classe, valor)

Argumentos:
#classe: Classe associada ao processo.
#valor: Valor associado ao processo.

Retorna:
#Nenhum.

Funcionalidade:
#Exibe informações sobre a classe e o valor.

```
```PYTHON

def auto_login(self)

Argumentos:
#Nenhum.

Retorna:
#Nenhum.

Funcionalidade:
#Automatiza a autenticação do usuário.


```
```PYTHON

def auto_consulta_processo(self, valor)

Argumentos:
#valor: Valor associado ao processo.

Retorna:
#Nenhum.

Funcionalidade:
#Automatiza a consulta de um processo.


```
```PYTHON

def auto_acessa_menu_consulta(self)

Argumentos:
#Nenhum.

Retorna:
#Nenhum.

Funcionalidade:
#Automatiza o acesso ao menu SAJ para consulta de processos.


```
```PYTHON

def auto_processa_a_leitura_do_excel(self, df)

Argumentos:
#df: DataFrame contendo os números de processo.

Retorna:
#Nenhum.

Funcionalidade:
#Automatiza o consumo dos números de processo no arquivo Excel de leitura.


```
```PYTHON

def processo_consultar_processos(self)

Argumentos:
#Nenhum.

Retorna:
#Nenhum.

Funcionalidade:
#Consulta processos para cada arquivo Excel encontrado no diretório de leitura.

```
```PYTHON

def run(self)

Argumentos:
#Nenhum.

Retorna:
#Nenhum.

Funcionalidade:
#Método principal que inicia o processo de automação.

```












