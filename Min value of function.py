# Find the minimum value of a function y = (x+3)^2, where ^ means power.

x=2 #initial value of x
l=0.01 #learning rate
prec=1
df= lambda x: 2*(x+3) #derivative function value
while prec>0.0001:
    prev_x=x
    x = x -l*df(x)
    prec=prev_x-x
print("Minimum value of function y=(x+3)^2 is ",x)
