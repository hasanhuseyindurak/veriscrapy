from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
from requests import exceptions
import pandas as pd

class Uygulama():
    def __init__(self,):
        liste = []
        aranacak_sey = input("Aranacak ürün ismi giriniz : ")
        boslukdoldur = aranacak_sey.replace(' ','+')

        try:
            url = f"https://www.gittigidiyor.com/arama/?k={boslukdoldur}&qm=1"
            response = requests.get(url)
            html_icerigi = response.content
            soup = BeautifulSoup(html_icerigi, "html.parser")
            div = soup.find('div', {'class' : "vfy45n-0 bWfBMK"})
            div2 = div.find('div', {'class' : 'u0iwlj-0 dWEUSh'})
            div3 = div2.find('div', {'class' : 'sc-1yvp483-0 bPjkuS'})
            div4 = div3.find('div', {'class' : 'sc-1nx8ums-0 fbkkZW'})
            div5 = div4.find('div', {'class' : 'sc-1yvp483-0 dTGwmm'})
            div6 = div5.find('div', {'class': 'sc-533kbx-0 sc-1v2q8t1-0 iCRwxx gyNBA'})
            div7 = div6.find('div', {'class' : 'pmyvb0-0 jCCkZh'})
            ul = div7.find('ul')
            ulli = ul.find_all('li', {'class' : 'list-item'})
            #print(ulli)

            for i in ulli:
                urunadi = i.find('h3').text.strip('\n').strip('')
                urunfiyati = i.find('span',{'class' : 'buy-price'}).text.lstrip('\n').lstrip('').rstrip('\n').rstrip('')
                liste.append([urunadi,urunfiyati])

        except Exception as e:
            boslukdoldur = aranacak_sey.replace(' ', '% 20')
            url = f"https://www.gittigidiyor.com/{boslukdoldur}?k={boslukdoldur}&qm=1"
            response = requests.get(url)
            html_icerigi = response.content
            soup = BeautifulSoup(html_icerigi, "html.parser")
            div = soup.find('div', {'class': "vfy45n-0 bWfBMK"})
            div2 = div.find('div', {'class': 'u0iwlj-0 dWEUSh'})
            div3 = div2.find('div', {'class': 'sc-1yvp483-0 bPjkuS'})
            div4 = div3.find('div', {'class': 'sc-1nx8ums-0 fbkkZW'})
            div5 = div4.find('div', {'class': 'sc-1yvp483-0 dTGwmm'})
            div6 = div5.find('div', {'class': 'sc-533kbx-0 sc-1v2q8t1-0 iCRwxx gyNBA'})
            div7 = div6.find('div', {'class': 'pmyvb0-0 jCCkZh'})
            ul = div7.find('ul')
            ulli = ul.find_all('li', {'class': 'list-item'})
            # print(ulli)

            for i in ulli:
                urunadi = i.find('h3').text.strip('\n').strip('')
                urunfiyati = i.find('span', {'class': 'buy-price'}).text.lstrip('\n').lstrip('').rstrip('\n').rstrip('')
                liste.append([urunadi, urunfiyati])

        df = pd.DataFrame(liste,columns = ["Ürün Adı","Fiyat"])
        print(df)

if __name__ == '__main__':
    Uygulama()