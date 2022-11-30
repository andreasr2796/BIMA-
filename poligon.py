import math 

n = int(input("Number of points: "))

list_X = []
list_Y = []

for i in range(0,n):
    x = int(input("Enter X value for point No " + str(i+1) + " : "))
    list_X.append(x)
    y = int(input("Enter Y value for point No " + str(i+1) + " : "))
    list_Y.append(y)

sum_xy = []

#AREA
for i in range(0,n-1):
    sum_xy.append((list_X[i+1]+list_X[i])*(list_Y[i+1]-list_Y[i]))

sum_xy.append((list_X[0]+list_X[len(list_X)-1])*(list_Y[0]-list_Y[len(list_Y)-1]))

AREA = (sum(sum_xy))*(0.5)
print("Poligon Area: " + str("%.2f" % AREA))

#Static cross sectional moments X

scs_x = []

for i in range(0,n-1):
    scs_x.append((list_X[i+1]-list_X[i])*((list_Y[i+1]**2)+list_Y[i]*list_Y[i+1]+(list_Y[i]**2)))

scs_x.append((list_X[0]-list_X[len(list_X)-1])*((list_Y[0]**2)+list_Y[i]*list_Y[0]+(list_Y[len(list_Y)-1]**2)))

SCSx =  (sum(scs_x))*(-0.6)
print("Static cross sectional moments for x: " + str("%.2f" % SCSx))

#Static cross sectional moments Y

scs_y = []

for i in range(0,n-1):
    scs_y.append((list_Y[i+1]-list_Y[i])*((list_X[i+1]**2)+list_X[i]*list_X[i+1]+(list_X[i]**2)))

scs_y.append((list_Y[0]-list_Y[len(list_Y)-1])*((list_X[0]**2)+list_X[i]*list_X[0]+(list_X[len(list_X)-1]**2)))

SCSy =  (sum(scs_y))*(0.6)
print("Static cross sectional moments for y: " + str("%.2f" % SCSy))

# Axial moments of inertia of the transmission (X)

I_x = []

for i in range(0,n-1):
    I_x.append((list_X[i+1]-list_X[i])*((list_Y[i+1]**3)+((list_Y[i+1]**2)*list_Y[i])+(list_Y[i+1]*(list_Y[i]**2)+(list_Y[i]**3))))

I_x.append((list_X[0]-list_X[len(list_X)-1])*((list_Y[0]**3)+((list_Y[0]**2)*list_Y[len(list_Y)-1])+(list_Y[0]*(list_Y[len(list_Y)-1]**2)+(list_Y[len(list_Y)-1]**3))))

IxSum = (sum(I_x))*(-(1/12))
print("Axial moment of intertia of the transmission on X: " + str("%.2f" % IxSum))

# Axial moments of inertia of the transmission (y)

I_y = []

for i in range(0,n-1):
    I_y.append((list_Y[i+1]-list_Y[i])*((list_X[i+1]**3)+((list_X[i+1]**2)*list_X[i])+(list_X[i+1]*(list_X[i]**2)+(list_X[i]**3))))

I_y.append((list_Y[0]-list_Y[len(list_Y)-1])*((list_X[0]**3)+((list_X[0]**2)*list_X[len(list_X)-1])+(list_X[0]*(list_X[len(list_X)-1]**2)+(list_X[len(list_X)-1]**3))))

IySum = (sum(I_y))*((1/12))
print("Axial moment of intertia of the transmission on y: " + str("%.2f" % IySum))

#Axial moments of intertia of the transmission (xy)

I_xy = []

for i in range(0,n-1):
    I_xy.append((list_Y[i+1]-list_Y[i])*(list_Y[i+1]*((3*(list_X[i+1]**2))+((2*list_X[i+1])*list_X[i])+list_X[i]**2)+list_Y[i]*((3*list_X[i]**2)+(2*list_X[i+1]*list_X[i]+(list_X[i+1]**2)))))

I_xy.append((list_Y[0]-list_Y[len(list_Y)-1])*(list_Y[0]*((3*(list_X[0]**2))+((2*list_X[0])*list_X[len(list_X)-1])+list_X[len(list_X)-1]**2)+list_Y[len(list_Y)-1]*((3*list_X[len(list_X)-1]**2)+(2*list_X[0]*list_X[len(list_X)-1]+(list_X[0]**2)))))

IxySum = (sum(I_xy))*(-(1/24))
print("Axial moment of intertia of the transmission on xy: " + str("%.2f" % IxySum))

#Coordinates of the centroid

X_t = SCSy/AREA
print("Coordinates of the centroid on x: " +str("%.2f" % X_t))

#Coordinates of the centroid

Y_t = SCSx/AREA
print("Coordinates of the centroid on y: " +str("%.2f" % Y_t))

# moments of inertia with respect to the axes moved in parallel through points of gravity

IxT = IxSum-(Y_t**2)*AREA
IyT = IySum-(X_t**2)*AREA
IxyT = IxySum+(X_t)*(Y_t)*AREA

print("The moment of inertia with respect of X is: " +str("%.2f" % IxT))
print("The moment of inertia with respect of y is: " +str("%.2f" % IyT))
print("The moment of inertia with respect of xy is: " +str("%.2f" % IxyT))


#Assigment#3 - Andrea Soto Roldan


