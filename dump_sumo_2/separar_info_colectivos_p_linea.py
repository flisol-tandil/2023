import json
import csv

def procesar_linea(datos_linea, n):
    for reg in datos_linea:
        reg = str(reg).replace("['[", "")
        reg = str(reg).replace("]']", "")
        reg = str(reg).replace("'", "")
        reg = str(reg).replace('"', "")
        reg = reg.split(',')
        
        if len(reg) > 2:
            p_0 = reg[5].split("]")
            numero = p_0[0]
            numero = str(numero).strip(" [")
            p_0 = str(p_0[1]).split(" ")
            reg = { "lat": str(reg[0]).strip(), "lng": str(reg[1]).strip("] "), "img": str(reg[2]).strip("] "), "numero": numero, "hora": p_0[0], "velocidad":p_0[1] }
        else:
            reg = ""
        
        with open('./2023_04_14_colectivos_'+str(n)+'.csv', 'a', newline='') as f:
            toCSV = ['dt', 'lat', "lng", "img", "numero", "hora", "velocidad"]
            w = csv.DictWriter(f, toCSV, delimiter='|')

            if (reg != ""):
                print(reg)
                print(" \n")
                w.writerow( {
                    'dt':row[0], 
                    'lat':reg['lat'], 
                    'lng':reg['lng'], 
                    'img':reg['img'], 
                    'numero':reg['numero'], 
                    'hora':reg['hora'], 
                    'velocidad':reg['velocidad'] 
                })
            else:
                w.writerow( {
                    'dt':row[0], 
                    'lat':"", 
                    'lng':"", 
                    'img':"", 
                    'numero':"", 
                    'hora':"", 
                    'velocidad':""
                })           

with open('2023_04_14_colectivos.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='|')

    for row in csvreader:
        procesar_linea(json.loads(row[1]), 0)
        procesar_linea(json.loads(row[2]), 1)
        procesar_linea(json.loads(row[3]), 2)
        procesar_linea(json.loads(row[4]), 3)
        procesar_linea(json.loads(row[5]), 4)
        procesar_linea(json.loads(row[6]), 5)
            

                
                
