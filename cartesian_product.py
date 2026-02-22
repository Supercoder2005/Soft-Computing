import numpy as np 

R = np.array([[0.5,0.7,0.2],
              [0.8,0.6,0.9]])
S = np.array([[0.6,0.3],
              [0.9,0.4],
              [0.5,0.8]])

final = []
for i in range(len(R)):
    for j in range(len(R[0])):
        row = []
        for k in range(len(S)):
            for l in range(len(S[0])):
                element = min(R[i][j],S[k][l])
                row.append(element)
        final.append(row)
print(np.array(final))
        

