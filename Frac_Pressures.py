from tkinter import *
 
root = Tk()
root.title('New Project 1.0')
#root.iconbitmap('insert path')
root.geometry("500x300")
root.configure(bg='#384048')
#Removes frame from the window. Commented out for now due to development.
#root.overrideredirect(True)
 
#window dimensions(auto size)
#RWidth=root.winfo_screenwidth()
#RHeight=root.winfo_screenheight()
#root.geometry(("%dx%d")%(RWidth,RHeight))
 
#img = ImageTK.PhotoImage(image.open(path))
#panel = tk.Label(mainframe, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
 
 
#Frame containing the app within the window.
mainframe = LabelFrame(root, bg='#384048', padx=15, pady=15, relief=SUNKEN)
mainframe.pack(fill="both", expand=True, padx=15, pady=15)
mainframe.columnconfigure(0, weight=2)
mainframe.columnconfigure(1, weight=2)
mainframe.columnconfigure(2, weight=2)
 
 
#Fractional Pressures Calculator
def o2():
     tpress=int(tpress_entry.get())
     oxy=int(oxy_entry.get())
     nitro=int(nitro_entry.get())
     heli=int(heli_entry.get())
     
     r1 = (float(tpress) * (float(oxy) / 100))
     r2= (float(tpress) * (float(nitro) / 100))
     r3=  (float(tpress) * (float(heli) / 100))
     if oxy > 0:
        oxy_out.insert(0, f"{r1:.0f}")
        
     else:
        pass
     if nitro > 0:
        nitro_out.insert(0, f"{r2:.0f}")
     else:
        pass
     if heli > 0:
        heli_out.insert(0, f"{r3:.0f}")
     else:
        pass
 
def clear():
    tpress_entry.delete(0, END)
    oxy_entry.delete(0, END)
    oxy_out.delete(0, END)
    nitro_entry.delete(0, END)
    nitro_out.delete(0, END)
    heli_entry.delete(0, END)
    heli_out.delete(0, END)
 
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
    print("Total Gas Pressure:", r1, "psi")
 
if Nitro > "0":
    print("Total Gas Pressure:", r2, "psi") 
 
if Heli > "0":
    print("Total Gas Pressure:", r3, "psi")
 
#print("Total Gas Pressure:", result)
#exit()
"""
#labels
lbl1 = Label(mainframe, text="Fractional Pressures Calculator", bg='#384048', fg="white")
lbl1.grid(row=0, columnspan=3, pady=100)
 
lbl2 = Label(mainframe, text="Tank Pressure", bg='#384048', fg="white")
lbl2.grid(row=1, columnspan=3, pady=15)
 
lbl3 = Label(mainframe, text="Oxygen %", bg='#384048', fg="white")
lbl3.grid(row=3, column=0, pady=15)
 
lbl4 = Label(mainframe, text="Oxygen Pressure", bg='#384048', fg="white")
lbl4.grid(row=3, column=1, pady=15)
 
lbl5 = Label(mainframe, text="Nitrogen %", bg='#384048', fg="white")
lbl5.grid(row=5, column=0, pady=15)
 
lbl6 = Label(mainframe, text="Nitrogen Pressure", bg='#384048', fg="white")
lbl6.grid(row=5, column=1, pady=15)
 
lbl7 = Label(mainframe, text="Helium %", bg='#384048', fg="white")
lbl7.grid(row=7, column=0, pady=15)
 
lbl8 = Label(mainframe, text="Helium Pressure", bg='#384048', fg="white")
lbl8.grid(row=7, column=1, pady=15)
 
Tpress = StringVar()
Oxy = StringVar()
Nitro = StringVar()
Heli = StringVar()
 
tpress_entry = Entry(mainframe, textvariable=Tpress)
tpress_entry.grid(row=2, columnspan=2, pady=15) 
 
oxy_entry = Entry(mainframe, textvariable=Oxy)
oxy_entry.grid(row=4, column=0, padx=15, pady=15)
 
oxy_out = Entry(mainframe)
oxy_out.grid(row=4, column=1, padx=15, pady=15)
 
nitro_entry = Entry(mainframe, textvariable=Nitro)
nitro_entry.grid(row=6, column=0, padx=15, pady=15)
 
nitro_out = Entry(mainframe)
nitro_out.grid(row=6, column=1, padx=15, pady=15)
 
heli_entry = Entry(mainframe, textvariable=Heli)
heli_entry.grid(row=8, column=0, padx=15, pady=15)
 
heli_out = Entry(mainframe)
heli_out.grid(row=8, column=1, padx=15,pady=15)
 
calc = Button(mainframe, text="Calculate", command=o2)
calc.grid(row=10, columnspan=3, pady=15)
 
clear = Button(mainframe, text="Reset", bg="red", fg="white", command=clear)
clear.grid(row=11, columnspan=3, pady=15)
 
 
 
root.mainloop()
