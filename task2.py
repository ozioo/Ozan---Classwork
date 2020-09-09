import pdb

width = int(input("what is the width of your room"))
height = int(input("what is the height of your room"))
non_area=int(input("What is the dimensions of the unaintable areas in your room ?"))
paint_area = (width * height)- non_area
cans= float(paint_area/11)
print(cans)
