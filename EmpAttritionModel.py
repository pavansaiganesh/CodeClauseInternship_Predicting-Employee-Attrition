import joblib 

rf = joblib.load('filename1.pkl') 
arr = rf.predict([[  2, 449,   1,   0,   1,   1,   1,   0,   6,   1,   2,   0,   1,
       132, 271,   1,   1,   0,   0,   3,   1,   1,   1,   2,   1,   0,
         0,   0]])
for i in arr:
    if i == 0:
        print('Attrition: No')
    print('Attrition: Yes')
    