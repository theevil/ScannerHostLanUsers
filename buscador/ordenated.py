"""
this is the part of the source where
do the find th lan userts


"""
import os

class Buscar:
    x = open("../scaneo.txt", 'r')
    ips = []
    def __init__(self):
        self.scanear()

    def scanear(self):
        print "inicio scaneo host en lan..."
        os.system("sudo fing | grep UP > ../scaneo.txt")
        print "termino scaneo en lan..."
        print "host obtenidos: ",len(self.x.readlines())

    def filtrar(self):
        print "procesando datos..."
        for y in self.x.readline() :
            ip = y.split("|")
            print(ip)
            self.ips.append(ip[1])
        return self.ips


