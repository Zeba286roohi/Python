import matplotlib.pyplot as plt
x=[2001,2002,2003,2004]
y=[1500,6000,3000,2000]
x2=[2001,2002,2003,2004]
y2=[1700,3000,5430,1200]
    
plt.plot(x,y,label="company1")
plt.plot(x2,y2,label="company2")
plt.title("Sales Information\n (in years)")
plt.xlabel("years")
plt.ylabel("sales (lakhs)")

plt.legend()
plt.show()
