from math import sqrt
a = int(input("2.dereceden x sayısının baş katsayısını girin:"))
b = int(input("Birinci dereceden x sayısının katsayısını girin:"))
c = int(input("Sabit Sayıyı Girin:"))
dis = b*b-4*a*c
if dis>0:
    kokdis = sqrt(dis)
    x1 = (-b+kokdis)/2*a
    x2 = (-b-kokdis)/2*a
    print("Birinci Kok:{} İkinci Kok: {}".format(x1,x2))
elif dis == 0:
    kokdis = sqrt(dis)
    x1 = (-b + kokdis) / 2 * a
    print("Bir Kok Bulunmaktadır ve Kok:{}".format(x1))
else :
    print("Reel Kök Yoktur.")
