import matplotlib.pyplot as plt
import numpy as np

score=np.random.normal(loc=80, scale=10, size=100)

score=np.clip(score, 0, 100)

plt.hist(score, bins=10,
                color="lightgreen",
                edgecolor="black",
                )
plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("Number of students")

plt.show()