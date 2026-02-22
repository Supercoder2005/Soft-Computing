import numpy as np
R = np.array([[0.5,0.7,0.2],
              [0.8,0.6,0.9]])
S = np.array([[0.6,0.3],
              [0.9,0.4],
              [0.5,0.8]])
final = []
for i in range(len(R)):
    row = []
    for j in range(len(S[0])):
        elementlist = []
        for k in range(len(S)):
            element = min(R[i][k],S[k][j])
            elementlist.append(element)
        row.append(max(elementlist))
    final.append(row)

print(np.array(final))
            