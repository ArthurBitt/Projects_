const puppeteer = require('puppeteer');
const xlsx = require('xlsx');
const Excel = require('exceljs');
const path = require('path');
const fs = require('fs');

let processos = []

// Pega os processos Excel e joga em um array
let ler_processos = async () => {
    var sheets = [];
    var wb = new Excel.Workbook();
    const arquivoLeitura = 'processosTRT.xlsx';
    
    var filePath = path.resolve(__dirname + "/ProcessosTRT", arquivoLeitura);
    if (fs.existsSync(filePath)) { 
        await wb.xlsx.readFile(filePath);
        wb.eachSheet(function (worksheet) {
            sheets.push(worksheet.name); //Coloca o nome das abas da planilha em um array
        });
    }

    for (let p = 0; p < sheets.length; p++) { //Para todas as abas da planilha
        let sh = wb.getWorksheet(sheets[p]); // Primeira aba do arquivo excel - Planilha
        if (sh.getRow(2).getCell(1).text !== '') {
            for (let i = 2; i <= sh.rowCount; i++) { //Começa a ler da linha 2
                processos.push(sh.getRow(i).getCell(1).text)                
            }
        }
    }
}

(async function abrir_painel_procurado(){
    await ler_processos();
    const browser = await puppeteer.launch({
        executablePath:'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
        ignoreHTTPSErrors: true,
        headless: false, args: ['--start-maximized']});
const page = await browser.newPage(); 
page.setDefaultTimeout(300*1000);
var pages = await browser.pages();
await pages[0].close();

const tribunal = [
                    {
                    login: "https://pje.trt2.jus.br/primeirograu/login.seam",
                    painel: "https://pje.trt2.jus.br/primeirograu/Painel/painel_usuario/advogado.seam"
                    }
                ];

console.log('Aguarde, processando a requisição...')

// acessa o PJE, faz login e vai até o painel do procurador
await page.setViewport({ width: 0, height: 0});
for (i=0; i<tribunal.length; i++){
    await page.goto(tribunal[i].login);
    await page.waitForSelector('#loginAplicacaoButton');
    console.log('Fazendo login')    
    await page.waitForSelector('#botao-menu');
    await page.goto(tribunal[i].painel);    
    await page.waitForSelector('#tabProcAdvPainelPeticaoInicial_lbl');
    await page.click("#idCaixa_lbl") // Aba "Acervo Geral", para o perfil Dr. Ademir
    await page.click('#tabProcAdvPainelPeticaoInicial_lbl');
    console.log("Acessou o painel do usuário.");   
    
    for (j=0; j<processos.length; j++){ // Para todos os processos dentro do array
        // Suspende a abertura dos processos enquanto houver mais de 3 abas abertas
        do{
            await new Promise(resolve => setTimeout(resolve, 3000)); 
            var pages = await browser.pages();
        }
        while(pages.length >= 2);

        if ((await page.$("#formLocCaix\\:btnLimparPesquisa")) !== null) { // Verifica se o botão limpar existe na página
            await page.click("#formLocCaix\\:btnLimparPesquisa")
        }
        await new Promise(resolve => setTimeout(resolve, 3000)); 
        await page.focus("#formLocCaix\\:decosuggestProcessoAdvogadoProc\\:suggestProcessoAdvogadoProc")
        await page.type("#formLocCaix\\:decosuggestProcessoAdvogadoProc\\:suggestProcessoAdvogadoProc", processos[j])
        await new Promise(resolve => setTimeout(resolve, 2000));
        await page.waitForSelector("#formLocCaix\\:decosuggestProcessoAdvogadoProc\\:sugsuggestProcessoAdvogadoProc\\:suggest > tbody > tr.rich-sb-int.richfaces_suggestionEntry.rich-sb-int-sel > td")
        await page.click("#formLocCaix\\:decosuggestProcessoAdvogadoProc\\:sugsuggestProcessoAdvogadoProc\\:suggest > tbody > tr.rich-sb-int.richfaces_suggestionEntry.rich-sb-int-sel > td")
        await page.click("#formLocCaix\\:btnPesquisa")
        // document.querySelector("#processoTrfInicialAdvogadoList\\:0\\:abreTarefResponder")
        
        await new Promise(resolve => setTimeout(resolve, 3000));
        if ((await page.$("#processoTrfInicialAdvogadoList\\:0\\:abreTarefResponder")) !== null) { // Verifica se o botão limpar existe na página
            await new Promise(resolve => setTimeout(resolve, 2000));
            await page.waitForSelector("#processoTrfInicialAdvogadoList\\:0\\:abreTarefResponder")
            await page.click("#processoTrfInicialAdvogadoList\\:0\\:abreTarefResponder")
        }
        else{
            await new Promise(resolve => setTimeout(resolve, 2000));
            await page.waitForSelector("#processoTrfInicialAdvogadoList\\:0\\:abreTarefDetalhes")
            await page.click("#processoTrfInicialAdvogadoList\\:0\\:abreTarefDetalhes")
        }
        await new Promise(resolve => setTimeout(resolve, 3000));
    }     
}

await browser.close();

})(); // finaliza a função principal