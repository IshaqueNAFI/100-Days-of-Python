import matplotlib.pyplot as plt

x = [ 1,2,3,4,5,6,7]
y= [3,4,6,2,4,6,7]


plt.plot(x,y)

plt.xlabel('x axis level')
plt.ylabel('y axiz level')

plt.savefig(' line.jpg' , format ='jpg' )
plt.close
