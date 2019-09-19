## made by Lucka Barbeau 1748294 and Matthew Coffey 1642072
import matplotlib.pyplot as plt
import numpy as np


def plot_error(error , nb_cell):
    log_e = np.log(error)
    log_nb = np.log(1/nb_cell)
    a , b = np.polyfit(log_nb , log_e , 1)

    plt.plot(log_nb,log_e,'bo')
    X_1=np.zeros((2,1))
    Y_1 = np.zeros((2, 1))
    X_1[0] = np.min(log_nb)
    X_1[1] = np.max(log_nb)
    Y_1[0] = np.min(log_nb)*a+b
    Y_1[1] = np.max(log_nb)*a+b
    plt.xlabel('ln(1/nx)')
    plt.ylabel( 'ln(Error)')
    plt.title(('log log curve of error in function of the cell size , Slop =',str(a)))
    plt.plot(log_nb, log_e, 'bo')
    plt.plot(X_1, Y_1,)
    print(('the slope of the error curve is ', str(a)))
    return a , b