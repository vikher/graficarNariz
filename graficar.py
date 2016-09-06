import matplotlib.pyplot as plt
import numpy
import csv

fruta,s1,s2,s3,s4,s5 = ([] for i in range(6))


with open('Entrenamiento.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        fruta.append(int(row[5]))
        s1.append(int(row[0]))
        s2.append(int(row[1]))
        s3.append(int(row[2]))
        s4.append(int(row[3]))
        s5.append(int(row[4]))


#plt.plot(x,y, label='Loaded from file!')
plt.scatter(fruta,s1, label='sensor1', color='k', s=25, marker="o")
plt.scatter(fruta,s2, label='sensor2', color='blue', s=25, marker="v")
plt.scatter(fruta,s3, label='sensor3', color='red', s=25, marker="1")
plt.scatter(fruta,s4, label='sensor4', color='green', s=25, marker="2")
plt.scatter(fruta,s5, label='sensor5', color='yellow', s=25, marker="3")
plt.xlabel('frutas')
plt.ylabel('salida sensor')
plt.title('Grafica Nariz Electronica\nScatter')
plt.legend()
plt.show()

as1,as2,as3,as4,as5 = ([] for i in range(5))


with open('Ajo.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        as1.append(int(row[0]))
        as2.append(int(row[1]))
        as3.append(int(row[2]))
        as4.append(int(row[3]))
        as5.append(int(row[4]))

as1.extend(as2)
as1.extend(as3)
as1.extend(as4)
as1.extend(as5)
print(as1)



bins = [0,100,200,300,400,500,600]

plt.hist(as1, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Distribucion Ajo\nHistograma')
plt.legend()
plt.show()