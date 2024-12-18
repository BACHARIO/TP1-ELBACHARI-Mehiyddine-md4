import numpy as np
import time  

frame = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
def compute_number_neighbors(padded_frame, index_line, index_column): 
    sub_matrix = padded_frame[index_line-1:index_line+2, index_column-1:index_column+2]
    number_neighbors = np.sum(sub_matrix) - padded_frame[index_line, index_column]
    return number_neighbors
def compute_next_frame(frame):
    padded_frame = np.pad(frame, pad_width=1, mode='constant')
    new_frame = np.zeros_like(frame)
    for i in range(1, padded_frame.shape[0] - 1):
        for j in range(1, padded_frame.shape[1] - 1):
            neighbors = compute_number_neighbors(padded_frame, i, j)
            if padded_frame[i, j] == 1:
                if neighbors in [2, 3]:
                    new_frame[i-1, j-1] = 1
                else:
                    new_frame[i-1, j-1] = 0
            else:
                if neighbors == 3:
                    new_frame[i-1, j-1] = 1
    return new_frame
while True:
    print("\nFrame :")
    print(frame)
    frame = compute_next_frame(frame)
    time.sleep(0.5)  
