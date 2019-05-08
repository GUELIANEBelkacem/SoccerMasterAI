
k=0
for i in range(1,11):
    vol=-1+3*i/11;
    b=vol*vol*vol*vol*vol-6*vol*vol*vol*vol+13*vol*vol*vol-12*vol*vol+4*vol;
    print( b);
    k+=b
    
    
print( (k*2 -36)*3/22);
