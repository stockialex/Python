from bs4 import BeautifulSoup
import requests 

class Cedear:
    def __init__(self, co_name, co_symbol, co_mkt, cedar_ratio):
        self.name = co_name
        self.symbol = co_symbol
        self.ratio = cedar_ratio
        self.market = co_mkt

def get_info():
    cedear_list = []
    with open('file_info_csv', 'r') as file:
        for line in file:
            line = clean_data(line)
            data = line.split(',')
            cedear_list.append(create_reg(data))
    return cedear_list
            
def clean_data(line):
    line = line.replace(', ',' ')
    line = line.replace('\n','')
    line = line.replace('"','')
    return line

def create_reg(data):
    cedear = Cedear(data[0],data[1],data[2],data[3])
    return cedear

lista = get_info()

for c in lista:
    print(c.name)
