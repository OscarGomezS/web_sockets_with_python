from dataInitial import DataInitial

if __name__=='__main__':
    time = int(input("Digite el tiempo en minutos que desea ejecutar el script: "))
    url = "ws://209.126.82.146:8080"
    DataInitial(url, time).run_loop()
    