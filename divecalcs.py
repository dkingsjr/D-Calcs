"""

#feet to atm conversion
depth = input("Enter Depth:")
result = (float(depth)/33) + 1
print(f"{result:.2f}","Total Atmospheres")"""

"""

#fractional pressures calculator
tpress = input("Enter Tank Pressure:")
Oxy = input("Enter o2 Percentage:")
Nitro = input("Enter n2 Percentage:")
Heli = input("Enter HE Percentage:")

r1 = (float(tpress) * (float(Oxy) / 100))
r2= (float(tpress) * (float(Nitro) / 100))
r3=  (float(tpress) * (float(Heli) / 100))

if Oxy > "0":
	print("Total Gas Pressure:", r1)
if Nitro > "0":
	print("Total Gas Pressure:", r2)
if Heli > "0":
	print("Total Gas Pressure:", r3)
"""

"""

#blend EaN from EaN
Fo2 = input("Enter Current o2:")
Fn2 = input("Enter Current n2:")
DFo2 = input("Enter Desired o2%:")
DP = input("Enter Desired Tank Pressure:")

r1 = (float(DFo2) / 100)
r2 = (float(Fo2) / 100)
r3 =  (float(Fn2) / 100)

result = ((r1 - r2) * float(DP) / r3)
print("Add", f"{result:.2f}", "PSI more o2")"""

#feet seawater calc