import requests
from bs4 import BeautifulSoup

class MyBotException(Exception):
    pass

class Currency:
    def __init__(self, shortname, fullname, price, volume):
        self.fullName = fullname
        self.shortName = shortname
        self.price = price
        self.volume = volume

    def getshortName(self):
        return self.shortName

    def getfullName(self):
        return self.fullName

    def getprice(self):
        return self.price

    def getvolume(self):
        return self.volume

    def exchange(self, secondcurrency, quantity):
        return (self.price * self.volume * quantity) / (secondcurrency.price * secondcurrency.volume)

    def __str__(self):
        return f'(Валюта {self.fullName}, Обозначение {self.shortName}, Стоимость в рублях {self.price} За {self.volume})'

class Converter:
    @staticmethod
    def getcurrency():
        base = 'https://cbr.ru/currency_base/daily/'
        html = requests.get(base).content
        data = BeautifulSoup(html, 'lxml')
        div = data.find('table', class_='data')
        div2 = div.findAll('td')
        div2 = list(div2)
        for i in range(len((div2))):
            div2[i] = str(div2[i])
            div2[i] = div2[i][4:-5]
        currencysimbols = []
        currencynames = []
        currencyprice = []
        currencyvolume = []
        for i in range(1, len(div2), 5):
            currencysimbols.append(div2[i])

        for i in range(3, len(div2), 5):
            currencynames.append(div2[i])

        for i in range(4, len(div2), 5):
            currencyprice.append(div2[i])
        for i in range(2, len(div2), 5):
            currencyvolume.append(div2[i])
        currencys = []
        for i in range(len(currencyprice)):
            currencyprice[i] = currencyprice[i].replace(',', '.')
            currencyvolume[i] = currencyvolume[i].replace(',', '.')
        for i in range(len(currencynames)):
            currencys.append(
                Currency(currencysimbols[i], currencynames[i], float(currencyprice[i]), float(currencyvolume[i])))
        currencys.append(Currency('RUB', "Рубль", 1, 1))
        return currencys

    @staticmethod
    def currenc(name):
        match = False
        for cur in Converter.getcurrency():
            if cur.getfullName().lower() == name.lower() or cur.getshortName() == name.upper():
                match = True
                return cur
        if not match:
            return "Нет такой валюты"
    @staticmethod
    def getcourse(name):
        match = False
        for cur in Converter.getcurrency():
            if cur.getfullName().lower() == name.lower() or cur.getshortName() == name.upper():
                match = True
                return f'{cur.getprice()} рублей за {cur.getvolume()} {name}'
        if not match:
            return "Нет такой валюты"
    @staticmethod
    def convert(message):
        fistcurrens = 0
        fistcurrenslen = 0
        secondcurrenc = 0
        secondcurrenclen = 0
        try:
            if len(message) < 3:
                raise MyBotException("Мало параметров")

            if Converter.getcourse(message[0]) != "Нет такой валюты":
                fistcurrenslen = 1
            elif len(message) > 3 and Converter.getcourse(message[0] + " " + message[1]) != "Нет такой валюты":
                fistcurrenslen = 2
            elif len(message) > 4 and Converter.getcourse(message[0] + " " + message[1] + " " + message[2]) != "Нет такой валюты":
                fistcurrenslen = 3
            elif len(message) > 5 and Converter.getcourse(message[:4]) != "Нет такой валюты":
                fistcurrenslen = 4
            else:
                raise MyBotException("Нет такой валюты")
        except MyBotException as e:
            return "Неверная команда"
        except Exception as e:
            return "Неудалось обработать запрос"
        fistcurrens = message[:fistcurrenslen]
        secondcurrenc = message[fistcurrenslen:-1]
        value = message[-1]
        fistcurrens = " ".join(fistcurrens)
        secondcurrenc = " ".join(secondcurrenc)
        value = int(value)
        fistcurrens = Converter.currenc(fistcurrens)
        secondcurrenc = Converter.currenc(secondcurrenc)
        result = fistcurrens.exchange(secondcurrenc, value)
        return result





