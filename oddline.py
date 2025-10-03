fn1 = open('codingal.txt','r')
fn2 = open('codingalupdated.txt','w')
cont = fn1.readlines()
type (cont)
for i in range(1,len(cont)+1):
    if (i%2!=0):
        fn2.write(cont[i-1])
    else:
        pass
fn1.close()
fn2.close()