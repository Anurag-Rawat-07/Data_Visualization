import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,1,2,3,4,5,6,7,7,8])    #Hours studied
y=np.array([55,60,65,62,68,70,75,78,82,85,87])   #Grades

plt.scatter(x,y, color="skyblue",
                 alpha=0.8,
                 s=40,
                 label="Class A"
                 )

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.legend()
plt.show()