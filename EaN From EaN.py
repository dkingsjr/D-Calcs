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
 
#Current o2% after air fill
def o2():
     tpress=int(tpress_entry.get())
     dpress=int(dpress_entry.get())
     coxy=int(coxy_entry.get())
     doxy=int(doxy_entry.get())
     
     r1 = (float(tpress) / 100)
     r2 = (float(dpress) / 100)
     r3 =  (float(coxy) / 100)
     result = ((r2 - r1) * float(doxy) / r3)
     oxy_out.delete(0, END)
     oxy_out.insert(0,f"{result:.0f} psi")
     
"""
     r1= float(dp) - float(ctp)
     r2= float(r1) * 0.21
     r3= (float(fo2) / 100)
     r4=((float(ctp) * float(r3)) + (float(r2))) / float(dp)
     result = (float(r4) * 100)
     out_put.insert(0, f"{result:.0f}")
""" 
def clear():
    tpress_entry.delete(0, END)
    dpress_entry.delete(0, END)
    coxy_entry.delete(0, END)
    doxy_entry.delete(0, END)
    oxy_out.delete(0, END)
    
    
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
 
#labels
lbl1 = Label(mainframe, text="Fill EaN from EaN", bg='#384048', fg="white")
lbl1.grid(row=0, columnspan=3, pady=100)
 
lbl2 = Label(mainframe, text="Tank Pressure", bg='#384048', fg="white")
lbl2.grid(row=1, column=0, pady=15)
 
lbl3 = Label(mainframe, text="Desired Pressure", bg='#384048', fg="white")
lbl3.grid(row=1, column=1, pady=15)
 
lbl4 = Label(mainframe, text="Current Oxygen %", bg='#384048', fg="white")
lbl4.grid(row=3, column=0, pady=15)
 
lbl5 = Label(mainframe, text="Desired Oxygen %", bg='#384048', fg="white")
lbl5.grid(row=3, column=1, pady=15)
 
lbl6 = Label(mainframe, text="Fill o2 to:", bg='#384048', fg="white")
lbl6.grid(row=5, columnspan=3, pady=15)
 
 
 
#entry widgets
Tpress = StringVar()
Dpress = StringVar()
Coxy = StringVar()
Doxy = StringVar()
Oxy = StringVar()
 
tpress_entry = Entry(mainframe, textvariable=Tpress)
tpress_entry.grid(row=2, column=0, padx=15, pady=15) 
 
dpress_entry = Entry(mainframe, textvariable=Dpress)
dpress_entry.grid(row=2, column=1, padx=15, pady=15) 
 
coxy_entry = Entry(mainframe, textvariable=Coxy)
coxy_entry.grid(row=4, column=0, padx=15, pady=15)
 
doxy_entry = Entry(mainframe, textvariable=Doxy)
doxy_entry.grid(row=4, column=1, padx=15, pady=15)
 
oxy_out = Entry(mainframe)
oxy_out.grid(row=6, columnspan=3, pady=15)
 
#buttons
calc = Button(mainframe, text="Calculate", command=o2)
calc.grid(row=10, columnspan=3, pady=15)
 
clear = Button(mainframe, text="Reset", bg="red", fg="white", command=clear)
clear.grid(row=11, columnspan=3, pady=15)
 
 
 
root.mainloop()
