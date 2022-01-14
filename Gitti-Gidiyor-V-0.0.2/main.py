from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
from requests import exceptions
import pandas as pd

class Uygulama():
    def __init__(self):
        self.aranacak_sey = input("Aranacak ürün ismi giriniz : ")
        boslukdoldur = self.aranacak_sey.replace(' ', '+')

        print("Veriler Sitelere Bakılarak Analiz Ediliyor")

        self.gittigidiyor(boslukdoldur)

        print("=======================================================================================")
        print("===================================== GİTTİ GİDİYOR ===================================")
        print("=======================================================================================")
        for i in range(len(self.gittigidiyorliste)):
            uruns_ad = self.gittigidiyorliste[i][0]
            uruns_fiyat = self.gittigidiyorliste[i][1]
            print(f"Ürün Adı : {uruns_ad} - Ürün Fiyatı : {uruns_fiyat}")
        print("=======================================================================================")

        time.sleep(2)

        self.n11()

        print("=======================================================================================")
        print("===================================== N11 =============================================")
        print("=======================================================================================")
        for i in range(len(self.n11liste)):
            urunss_ad = self.n11liste[i][0]
            urunss_fiyat = self.n11liste[i][1]
            print(f"Ürün Adı : {urunss_ad} - Ürün Fiyatı : {urunss_fiyat}")
        print("=======================================================================================")

    def n11(self):
        self.n11liste = []
        self.aranacak_sey = input("Aranacak ürün ismi giriniz : ")
        boslukdoldur = self.aranacak_sey.replace(' ', '+')
        url = f"https://www.n11.com/arama?q={boslukdoldur}"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        div = soup.find('div', {'class': 'content'})
        div2 = div.find('div', {'class' : 'container'})
        div3 = div2.find('div', {'class' : 'listingHolder'})
        div4 = div3.find('div', {'class' : 'productArea'})
        div5 = div4.find_all('div', {'class' : 'columnContent'})
        for i in div5:
            # bu bölüm düzeltilecek
            urun_adi1 = i.find('div', {'class' : 'pro'}).find('h3', {'class' : 'productName'})
            urun_adi = urun_adi1.text
            print(urun_adi)
            urn_fiat1 = i.find('div', {'class' : 'proDetail'}).find('span' , {'class' : 'newPrice cPoint priceEventClick'})
            urn_fiat = urn_fiat1.text
            print(urn_fiat)
            self.n11liste.append([urun_adi, urn_fiat])

    def gittigidiyor(self,boslukdoldur):
        self.gittigidiyorliste = []

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
            for i in ulli:
                urunadi = i.find('h3').text.strip('\n').lstrip('\n').lstrip('').rstrip('\n').rstrip('')
                urunfiyati = i.find('span',{'class' : 'buy-price'}).text.lstrip('\n').lstrip('').rstrip('\n').rstrip('')
                self.gittigidiyorliste.append([urunadi,urunfiyati])

        except Exception as e:
            boslukdoldur = self.aranacak_sey.replace(' ', '%20')
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
            for i in ulli:
                urunadi = i.find('h3').text.lstrip('\n').lstrip('').rstrip('\n').rstrip('')
                urunfiyati = i.find('span', {'class': 'buy-price'}).text.lstrip('\n').lstrip('').rstrip('\n').rstrip('')
                self.gittigidiyorliste.append([urunadi, urunfiyati])

        # df = pd.DataFrame(liste,columns = ["Ürün Adı","Fiyat"])
        # print(df)

if __name__ == '__main__':
    Uygulama()