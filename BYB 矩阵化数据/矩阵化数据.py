import numpy as np
data = np.load(r'C:\Users\86188\Desktop\寒假新冠本研\1\git\Trajectory-Clustering\files.npz')
print(data.files)
# items= ['WBC', 'NE', 'LYM', 'MON', 'IL_2', 'IL_4', 'IL_6', 'IL_10', 'TNF', 'IFN']
# t=80
# patients=213
print(data.files[0])
# for i in range(10):
#     print(len(data[data.files[i]][:,0]))
#     print(len(data[data.files[i]][0]))
ans=[]
print(np.isnan(data[data.files[0]][1][1]))
for j in range(1,80):
    for k in range(213):
        ans_i=[]
        for i in range(10):
            # print(data[data.files[i]][j][k])
            if np.isnan(data[data.files[i]][j][k]):
                ans_i = None
                break
            else:
                ans_i.append(data[data.files[i]][j][k])
        if ans_i is not None:
            if 0 <= k and k < 90:
                ans.append([1]+[k]+[j]+ans_i) # 类型 + patient + time + items
            elif 90 <= k and k < 90+99:
                ans.append([2] + [k] + [j] + ans_i)
            elif 90+99 <= k and k < 90+99+12:
                ans.append([3] + [k] + [j] + ans_i)
            elif 90 + 99 +12 <= k and k < 90 + 99 + 12 +12:
                ans.append([4] + [k] + [j] + ans_i)
    print("j=",j,"is ok","found",len(ans))
print(ans)
print(np.array(ans))
np.save("2dmatrix.npy",np.array(ans))