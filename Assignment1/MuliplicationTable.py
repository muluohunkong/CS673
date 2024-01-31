def MultiplicationTable(x):
    for i in range(x):
        i+=1
        for a in range(i):
                a+=1
                Result = a*i
                print(a,"X",i,"=",Result,end='\t')
        print()
MultiplicationTable(12)
