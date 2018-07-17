import random
import matplotlib.pyplot as plt
truedata=0
lim=1000000
x=list()
y=list()
xtrue=list()
ytrue=list()
for i in range(1,lim):
	newx=random.random()
	newy=random.random()
	x.append(newx)
	y.append(newy)
	if ((newy-0.5)**2)+((newx-0.5)**2)<0.25:
		truedata+=1
		xtrue.append(newx)
		ytrue.append(newy)
yekchaharompi=truedata/lim
pii=4*yekchaharompi
print(pii)
plt.plot(x,y,'bo',xtrue,ytrue,'ro')
plt.axis([0,1,0,1])
plt.show()