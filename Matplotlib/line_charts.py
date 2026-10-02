import matplotlib.pyplot as plt
import numpy as np

X=np.array([2023,2024,2025,2026])
Y=np.array([15, 25, 30, 20])
Y2=np.array([17, 23, 38, 15])

line_style=dict( marker=".", 
         markersize=30, 
         markerfacecolor="cyan",
         markeredgecolor="red",
         linestyle="dashed",
         linewidth=2,
         color="blue")

plt.title("Class Size", fontsize=20,
                        family="Arial",
                        fontweight="bold",
                        color="black")

plt.xlabel("Year", fontsize=20,
                    family="Arial",
                    fontweight="bold",
                    color="black")

plt.ylabel("Students", fontsize=20,
                    family="Arial",
                    fontweight="bold",
                    color="black")

plt.xticks(X)

plt.tick_params(axis="both",
                colors="blue")

plt.plot(X, Y, **line_style)

plt.plot(X, Y2, **line_style)

plt.show()