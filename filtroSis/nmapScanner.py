from ..buscador.ordenated import Buscar

import os
class nmapScanner:
    Buscar.scanear()
    ips = Buscar.filtrar()
    def __init__(self):
        self.scanearCadaIp()
    def scanearCadaIp(self):
        for x in self.ips:
            os.system("nmap -T4 -A -v -O -p 15-10000 %s | grep Discovered > scaneos/scaneo%sport.txt"%x)
            os.system("nmap -T4 -A -v -O -p 15-10000 %s | grep Service > scaneos/scaneo%sOs.txt" % x)
            os.system("nmap -T4 -A -v -O -p 15-10000 %s > scaneos/scaneo%full.txt" % x)
            print "scaneado la ip ",x
    def mostrarContenido(self):
        # imprimir los puertos
        for ip in self.ips:
            print "---------------------------------------------------------------------------"
            print "host ip :",ip
            puerto = open("scaneos/scaneo%sport.txt"%ip,"r")
            for puertos in puerto.readline():
                print puerto
            print open("scaneos/scaneo%sOs.txt"%ip,"r").readline()
            print "---------------------------------------------------------------------------"