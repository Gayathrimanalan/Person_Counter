import matplotlib.pyplot as plt

def plot(values):
    plt.scatter(getX(values), values, s=values, c='red')
    plt.xlabel('Frames')
    plt.ylabel('Count')
    plt.show()


def getX(values):
    l = []
    for i in range(len(values)):
        l.append(i)
    return l
