from filtroSis.nmapScanner import nmapScanner
from buscador.ordenated import Buscar
"""
@author =? theevil24a
@version =? python 2.7
@definition =? this is a program where detect users in lan and show
                what is the open ports and whats is the os

@packetes_necesaries =? nmap , fing
@os_requered =? Unix and defivateds

"""
if __name__ == '__main__':
    Buscar.scanear()
    nmapScanner.scanearCadaIp()