from bs4 import BeautifulSoup
import requests 

req = requests.get('https://dolarhoy.com/cotizaciondolarcontadoconliqui')
soup = BeautifulSoup(req.text, 'html.parser')

tipos = soup.select('.pull-left')
precios = soup.select('.pull-right')

def limpiar_precios(precios):
    lista_precios = []
    for i, costo in enumerate(precios):
        compraventa = precios[i].getText().replace('$ ', '')
        if i == 0:
            lista_precios.append({'tipo': 'compra', 'costo': float(compraventa[:-3] + '.' + compraventa[-2:])})
        else:
            lista_precios.append({'tipo': 'venta', 'costo': float(compraventa[:-3] + '.' + compraventa[-2:])})
    listar_precio_ccl(lista_precios)

def listar_precio_ccl(lista):
    print('*****    Precio CCL    *****')
    for item in lista:
        print(item.get('tipo') + ': ' + str(item.get('costo')))

limpiar_precios(precios)


