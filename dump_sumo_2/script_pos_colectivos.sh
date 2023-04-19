#!/bin/bash
echo >> salida_lineas.dat
SALIDA=''

while true
do
    echo ========== Haciendo Peticion ============
    #url="http://gpssumo.com/ajax/ebus_dev/get_todos/faa8f91f9b9fbc077ac44ca18aaa7b97/0"
    fecha=$(date)
    SALIDA=$(curl 'http://gpssumo.com/ajax/ebus_dev/get_todos/faa8f91f9b9fbc077ac44ca18aaa7b97/0' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0' -H 'Accept: */*' -H 'Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3' -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: http://gpssumo.com' -H 'Connection: keep-alive' -H 'Referer: http://gpssumo.com/' -H 'Sec-GPC: 1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data-raw 't=0' --output - )
    echo "${fecha}":${SALIDA}, >> salida_pos_colectivos.dat
    sleep 3
done
