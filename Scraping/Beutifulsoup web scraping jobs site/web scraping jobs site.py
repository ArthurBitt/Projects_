from bs4 import BeautifulSoup
import requests
import time

i = False
list = list()
while i == False:
    print("Insert keywords for seach one job")
    answer = input("> ")
    answer = answer.lower()
    list.append(answer)
    close = input("Do you want insert another keyword? y/n: ")
    if close.lower() == "y":
        continue;
    else:
         break;



def main(): 

    


    print(list)
    print(f"filtering jobs by... {list}")
    # get request
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    #intancia beutifulsoup e argumentos
    soup = BeautifulSoup(html_text, 'lxml')

    # tag macro> tags especificas
    li = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')

    #index variável contadora 1- job; 2 - job....

    for index, jobs in enumerate(li) :
        publish_date = jobs.find('span', class_ ='sim-posted').text
    # filtro de data
        if "few" in publish_date.lower():

            company_name = jobs.find('h3', class_='joblist-comp-name').text.replace(" ","")
            skills = jobs.find('span',class_ = 'srp-skills').text.replace(" ","")
        # iterando as keywords dadas dentro do scraping    
        for answer in range(len(list)):
                if list[answer] in skills.lower():
                    with open(f'C:\\Users\\arthu\\OneDrive\\Documentos\\Projetos\\Projetos de estudo\\Python\\Programas\\web scraping jobs site\\data{index}.txt', 'w') as f:
                        link = jobs.header.h2.a['href']
                                
                        print("------------------------------")

                        print(f'COMPANY: {company_name}')
                        
                        print(f'SKILLS: {skills}')
                    
                        print(f'LINK: {link}')


if __name__ == '__main__':
    while True:
        main()
        print(f"waiting {time_waiting}")
        time_waiting = time.sleep(10)
        