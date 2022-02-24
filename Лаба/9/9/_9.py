array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
chet=0
nechat=0
for i in array:
    if i%2==0:
        chet+=1
    if i%2!=0:
        nechat+=1
print('Количество чётных чисел:',chet)
print('Количество нечетных чисел:',nechat)
