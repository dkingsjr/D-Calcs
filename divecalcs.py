"""
#fsw to ata conversion
depth = input("Enter Depth:")
result = (float(depth)/33) + 1
print(f"{result:.2f}","Total Atmospheres")
"""
"""
#ffw to ata
depth = input("Enter Depth:")
result = (float(depth)/34) + 1
print(f"{result:.2f}","Total Atmospheres")
"""
 
 
 
"""
#fractional pressures calculator
tpress = input("Enter Tank Pressure:")
Oxy = input("Enter o2 Percentage:")
Nitro = input("Enter n2 Percentage:")
Heli = input("Enter HE Percentage:")
 
#convert to decimal
r1 = (float(tpress) * (float(Oxy) / 100))
r2= (float(tpress) * (float(Nitro) / 100))
r3=  (float(tpress) * (float(Heli) / 100))
 
if Oxy > "0":
    print("Total O2 Pressure:", r1, "psi")
 
if Nitro > "0":
    print("Total N2 Pressure:", r2, "psi") 
 
if Heli > "0":
    print("Total He Pressure:", r3, "psi")
 
#print("Total Gas Pressure:", result)
#exit()
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
print("Add", f"{result:.2f}", "PSI more o2")
"""
 
"""
#Current o2% after air fill
Fo2 = input("Enter Current o2:")
Ctp = input("Enter Current Tank Pressure:")
Dp = input("Enter Desired Tank Pressure:")
r1= float(Dp) - float(Ctp)
r2= float(r1) * 0.21
r3=(float(Fo2) / 100)
r4=((float(Ctp) * float(r3)) + (float(r2))) / float(Dp)
result = (float(r4) * 100)
print("New o2 Percentage:", f"{result:.0f}")
exit()
#(500*0.36 + 2500*0.21)/3000 = 0.235 (23.5% O2)
"""
 
"""
#calculate SAC Rate...
Fo2 = input("Enter Current o2:")
Fn2 = input("Enter Current n2:")
DFo2 = input("Enter Desired o2%:")
DP = input("Enter Desired Tank Pressure:")
r1 = (float(DFo2) / 100)
r2 = (float(Fo2) / 100)
r3 =  (float(Fn2) / 100)
result = ((r1 - r2) * float(DP) / r3)
print("Add", f"{result:.2f}", "PSI more o2")
"""
