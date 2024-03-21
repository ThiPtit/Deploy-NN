import matplotlib.pyplot as plt
import numpy as np
import scipy.io as scio
def display_data(x):
    (m, n) = x.shape
    
    #Set width and height of 1 image
    width =  np.round(np.sqrt(n)).astype(int)
    height = (n / width).astype(int)

    #Set row and column.
    row = np.floor(np.sqrt(m)).astype(int)
    column = np.ceil(m / row).astype(int)

    # Set blank between image
    pad = 1

     # Setup blank display
    display_array = - np.ones((pad + row * (height + pad),
                              pad + row * (height + pad)))
    curr_ex = 0
    for j in range(row):
        for i in range(column):
            if curr_ex > m:
                break

            # Copy the patch
            # Get the max value of the patch
            max_val = np.max(np.abs(x[curr_ex]))
            display_array[pad + j * (height + pad) + np.arange(height),
                          pad + i * (width + pad) + np.arange(width)[:, np.newaxis]] = x[curr_ex].reshape((height, width)) / max_val
            curr_ex += 1

        if curr_ex > m:
            break

    # Display image
    plt.figure()
    plt.imshow(display_array, cmap='gray', extent=[-1, 1, -1, 1])
    plt.axis('off')




