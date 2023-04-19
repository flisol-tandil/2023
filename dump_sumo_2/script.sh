#!/bin/bash
         echo >> salida.dat
         SALIDA=''
         COUNTER=101180
         while [  $COUNTER -lt 999999 ]; do
             tarjeta=10
             tarjeta+=$COUNTER
             echo ========== Tarjeta $tarjeta ============
             url="http://www.gpssumo.com/movimientos/get_movimientos/"
             url+=$tarjeta
             url+="/3"
             SALIDA=$(curl $url)
             echo "${tarjeta}":${SALIDA}, >> salida.dat
            #curl $url | jq '.'
             let COUNTER=COUNTER+1
         done

#find . -name "*.txt" -size -3c -delete
