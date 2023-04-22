import json
import datetime

with open("data.json", "r") as read_file:
    data = json.load(read_file)

def get_parquimetro_maximo(data):
    maximo = 0.0
    maximo_item = {}
    for clave,parquimetro in data.items():
        if isinstance(parquimetro, list):
            for medida in parquimetro:
                saldo = float(medida['saldo'][1:])
                if float(medida['saldo'][1:]) > maximo:
                    maximo = saldo
                    maximo_item = medida

    print(maximo_item)


def get_parquimetro_negativo(data):
    minimo = 0.0
    minimo_item = {}
    for clave,parquimetro in data.items():
        if isinstance(parquimetro, list):
            for medida in parquimetro:
                saldo = float(medida['saldo'][1:])
                if float(medida['saldo'][1:]) < minimo:
                    minimo = saldo
                    minimo_item = medida
    print(minimo_item)    

#get_parquimetro_maximo(data)
#get_parquimetro_negativo(data)


def agrupar_movimientos_por_meses(data):
    movs_meses = dict()
    for clave,parquimetro in data.items():
        if isinstance(parquimetro, list):
            for medida in parquimetro:    

                fecha_arr = medida['fecha'].split('/')
                
                fecha_index = fecha_arr[2]+"-"+fecha_arr[1]

                if fecha_index in movs_meses:
                    movs_meses[fecha_index].append(medida)
                else:
                    movs_meses[fecha_index] = []
    
        

agrupar_movimientos_por_meses(data)