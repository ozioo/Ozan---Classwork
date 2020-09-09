mileage_before=int(input("what was the  mileage the last time the car was filled"))
mileage_now=int(input("what is the mileage now?"))
gas=int(input("how many litres does it take to fill the tank up?"))

miles= int(mileage_now - mileage_before)
ratio = round(miles / (gas * 0.22))
print("your car does ",ratio," miles to the gallon")
