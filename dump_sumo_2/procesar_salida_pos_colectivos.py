import json
import csv



def procesarLineaColectivo(data):
    i = 0
    points_0 = ''
    for r_data in data[0]:
        data[0][i] = str(data[0][i]).replace('L.latLng(', '')
        data[0][i] = str(data[0][i]).replace("['", '')
        data[0][i] = str(data[0][i]).replace(')', '')
        data[0][i] = str(data[0][i]).replace("']", '')
        data[0][i] = str(data[0][i]).replace("[]", '')
        points_0 = points_0 + data[0][i]
        i = i + 1

    data[1] = str(data[1]).split('L.marker(')
    i = 0
    for r_data in data[1]: 
        data[1][i] = str(data[1][i]).replace("{icon: L.icon({iconUrl:", '')
        data[1][i] = str(data[1][i]).replace("iconSize: [", '')
        #data[1][i] = str(data[1][i]).replace("]", '')
        data[1][i] = str(data[1][i]).replace("'", '')
        data[1][i] = str(data[1][i]).replace("}", '')
        data[1][i] = str(data[1][i]).replace("{", '')
        #data[1][i] = str(data[1][i]).replace("[", '')
        data[1][i] = str(data[1][i]).replace(")", '')
        data[1][i] = str(data[1][i]).replace("title:", '')
        data[1][i] = str(data[1][i]).split(',')   

        j=0
        for r_data_2 in data[1][i]:
            data[1][i][j] = data[1][i][j].strip()
            j = j + 1
        i = i + 1 

    return json.dumps( data[1] , sort_keys=True)
c = 0
with open("salida_pos_colectivos.dat") as archivo:
    for data in archivo:

        data = data.split(':',3)
        if len(data) < 3:
            continue
        
        data[3] = data[3].replace("\ufeff", "")
        
        linea_date = data[0]+':'+data[1]+':'+data[2]
        linea_data = data[3]

        linea_data = linea_data.replace('[L.latLng(', '["L.latLng(')
        linea_data = linea_data.replace('[L.marker(', '["L.marker(')
        linea_data = linea_data.replace(')]', ')"]')
        linea_data = linea_data.replace('"http://', "'http://")
        linea_data = linea_data.replace('.png"', ".png'")
        linea_data = linea_data.replace("'], ['", "],[")
        linea_data = linea_data.replace("'], []], [", "'], []], [")
        linea_data = linea_data[:-2]
        print(linea_data)
        print('registro '+str(c)+"\n")
        c = c + 1
        try:
            linea_data = json.loads( linea_data )
        except:
            print('Ocurrio una excepción \n')
            linea_data = ""

        if linea_data != "":
            with open('./2023_04_14_colectivos.csv', 'a', newline='') as f:
                toCSV = ['dt', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5']
                toReg = {
                    'dt': linea_date, 
                    'b0': procesarLineaColectivo(linea_data[0]), 
                    'b1': procesarLineaColectivo(linea_data[1]), 
                    'b2': procesarLineaColectivo(linea_data[2]), 
                    'b3': procesarLineaColectivo(linea_data[3]), 
                    'b4': procesarLineaColectivo(linea_data[4]), 
                    'b5': procesarLineaColectivo(linea_data[5]) 
                }

                w = csv.DictWriter(f, toCSV, delimiter='|')
                w.writerow( toReg )
