T = {16:0.4,18:0.8,20:1.0,22:1.0,24:0.8,26:0.5}
H = {0:0.2,20:0.8,40:1.0,60:0.6,80:0.2}
T_th = float(input("Enter the threshold temperature :"))
H_th = float(input("Enter the threshold humidity :"))
print("The membership of Acceptable Temperature or Acceptable Humidity ---- \n")
for t in T:
    for h in H:
        if T[t]>T_th and H[h]>H_th:
            print(f"({t},{h}) : {max(T[t],H[h])}")
