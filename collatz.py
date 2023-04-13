import matplotlib.pyplot as plt

a1 = int(input("Input a1: "))

iterationsPlot = [] #this will act as the x-axis
plotA1 = [] #this will act as y-axis

def setCoord(a1):
    iter = 0
    plotA1.append(a1)
    iterationsPlot.append(iter)

    while a1 != 1:
        if a1 % 2 != 0:
            a1 = 3 * a1 + 1
            iter+=1
            plotA1.append(a1)
            iterationsPlot.append(iter)
        elif a1 % 2 == 0:
            a1 = a1 / 2
            iter+=1
            plotA1.append(a1)
            iterationsPlot.append(iter)

setCoord(a1)


plt.plot(iterationsPlot, plotA1)
plt.title("Collatz conjecture")
plt.xlabel("Iterations")
plt.ylabel("Collatz numbers")
plt.show()