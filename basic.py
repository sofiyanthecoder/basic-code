radius=float(input("input the radius of the circle"))
area=3.141*(radius**2)
print("The area of the circle with radius 1.1 is ",area)
filename=input("input the Filename:")
file_ext=filename.split(".")
print("the extension is"+ repr(file_ext[-1]))
