#Creates pickle for mechanics variables + variable names as a tuple
# [(a, acceleration),(m,mass)...]

from pickle import dump

re = []
#file = open("mechanics.txt","w")
with open("mechanics_raw.txt") as f:
    for line in f:
        arr = line.strip().split(" = ")
        re.append((arr[0],arr[1]))
        #file.write(arr[0],arr[1]) must be a string
fout = open( 'mechanics.pkl' , 'wb' )
dump( re , fout , protocol = 2 )
fout.close()

#To open pickle use...
#from pickle import load
#dicto = load( open( 'nbrs.pkl' , 'rb' ) )
