import matplotlib.pyplot as plt

x1=0
x2=24

y1=0
y2=24
plt.axis([x1,x2,y1,y2])
plt.axis('on')
plt.grid(True)
plt.title("Tangram Fichas")


#azul
plt.plot([5,5,0,5,5,5],[5,5,5,10,5,10])

#amarillo
plt.plot([7.5,11.5,15.5,7.5,15.5],[2.5,7.5,2.5,2.5,2.5])

#verde
plt.plot([7.5,7.5,10,10,7.5],[10,12.5,12.5,10,10])

#rojo
plt.plot([10,19,14.5,10],[17.5,17.5,12.5,17.5])

#morado
plt.plot([2.5,7.5,5,2.5],[15,15,17.5,15])

#cafe
plt.plot([20,20,22,20],[20,24,22,20])

#violeta
plt.plot([20,20,22,22,20],[5,9,12,8,5])


#plt.plot([1,2],[1,1])


x1=0
x2=20.2

y1=0
y2=20.2
plt.axis([x1,x2,y1,y2])
plt.axis('on')
plt.grid(True)
plt.title("Tangram Completo")


#azul
plt.plot([8.4,12.4,12.4,8.4],[5,5,10.5,5])

#amarillo
plt.plot([0.5,4,8,0.5],[5,10.5,5,5])



#verde
plt.plot([7.2,7.2,9.2,9.2,7.2],[10.7,13.8,13.8,10.7,10.7])

#rojo
plt.plot([8.2,4.2,12.2,8.2],[5,10.5,10.5,5])


#morado
plt.plot([5.7,10.7,8.2,5.7],[14,14,16.5,14])

#cafe
plt.plot([2.2,2.2,3.7,2.2],[8.1,12.2,10.3,8.1])

#violeta
plt.plot([0.4,0.4,2,2,0.4],[5,9,12,7.5,5])
