import matplotlib.pyplot as plt
Sales=[20000,35000,40000,50000,60000]
Months=['April','May','June','July','August']
plt.plot(Sales,Months,marker='o')
plt.title("The Line Graph showing numbers of Sales")
plt.xlabel(Sales)
plt.ylabel(Months)
plt.grid(color='red',linestyle='--',linewidth=1.5)
plt.show()
