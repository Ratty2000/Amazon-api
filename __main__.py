
if __name__ == "__main__":

    class scrape():
        def __init__(self, url='', price=''):
            if url == '':
                ScraperErrors.NoURL()
            self.target =   price
            self.url =     url
            self.headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
            self.page =    requests.get(url, headers=self.headers)
            self.soup =    BeautifulSoup(self.page.content, 'html.parser')

            ########## get the title

        

            self.titl =   str(self.soup.find(id="title"))
            titl = str(self.titl)
            titl = titl.split(' ')
            self.titleList = titl[7:-1]
            print(self.titleList)
            self.title = ''
            for self.titleList in self.titleList:
                self.title = self.title + ' ' + self.titleList
            

            ############ get the price

            proce = str(self.soup.find(id="priceblock_ourprice"))
            
            priceList = proce.split('$')
            print(priceList)
            prace = str(priceList[1])
            prooce = prace.split('<')
            price = str(prooce[0])
            print('Title: $'+self.title)
            print('Price: '+price)
            price = int(price)
            if self.target == price:
                print('price matches target')
            elif self.tagret > price:
                print('price is lower than target')