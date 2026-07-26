# WAP to print pattern:
# g)

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    

    for j in range( 1,i+1) :   
       print(chr(64+j),end=' ')
   
    
    for j in range(1,i):
        print(chr(65+i),end=' ')
        i+=1
    print()
        
   