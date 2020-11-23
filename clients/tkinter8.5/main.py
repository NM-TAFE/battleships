import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window,
                  height=200,
                  width=300,
                  relief=tk.RIDGE,
                  borderwidth=10)
frame1.pack()

for i in range(10):
    for j in range(10):
        frame2 = tk.Frame(
            master=frame1,
            relief=tk.RAISED,
            borderwidth=3
        )
        frame2.grid(row=i, column=j,padx=2,pady=2)
        label = tk.Label(master=frame2, text=f"Row {i}\nColumn {j}")
        label.pack(padx=4,pady=4)
        frame2.pack

window.mainloop()