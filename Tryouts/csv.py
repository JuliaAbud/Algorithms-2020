import csv
import math

def generarEstadistica(name,nPruebas):
    with open(name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["n", "nlogn", "insert", "Search"])
        for n in range(1,nPruebas+1):
            writer.writerow([1, n*math.log2(n), "Linux Kernel"])

generarEstadistica("prueba.csv",100)
print("hola")

#import csvwith open('eggs.csv', 'w', newline='') as csvfile:spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])