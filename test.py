import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Classworks Statistic')
style = ttk.Style(window)
window.tk.call("source", "forest-light.tcl")
window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

frame = ttk.Frame(window)
frame.pack()


common_config_frame = ttk.LabelFrame(frame, text="Common Configure")
common_config_frame.grid(row=0, column=0, padx=20, pady=10)

root_dir_label = ttk.Label(common_config_frame,text='Root Directory of Classworks')
root_dir_label.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")

root_dir__entry = ttk.Entry(common_config_frame)
root_dir__entry.insert(0, "/home/dd/Desktop/Repositories/Classwork-Statistic-App")
root_dir__entry.bind("<FocusIn>", lambda e: root_dir__entry.delete('0', 'end'))
root_dir__entry.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="w")

root_dir_button = ttk.Button(common_config_frame,text='Select')
root_dir_button.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="e")

classwork_dir_label = ttk.Label(common_config_frame,text='Root Directory of Classes')
classwork_dir_label.grid(row=3, column=0, padx=5, pady=(0, 5), sticky="ew")

classwork_dir__entry = ttk.Entry(common_config_frame)
classwork_dir__entry.insert(0, "/home/dd/Desktop/Repositories/Classwork-Statistic-App")
classwork_dir__entry.bind("<FocusIn>", lambda e: classwork_dir__entry.delete('0', 'end'))
classwork_dir__entry.grid(row=4, column=0, padx=5, pady=(0, 5), sticky="w")

classwork_dir_button = ttk.Button(common_config_frame,text='Select')
classwork_dir_button.grid(row=5, column=0, padx=5, pady=(0, 5), sticky="e")

appearance_style_label = ttk.Label(common_config_frame,text='Appearance Style')
appearance_style_label.grid(row=6, column=0, padx=5, pady=(0, 5), sticky="ew")




statistic_frame = ttk.LabelFrame(frame, text="Statistic")
statistic_frame.grid(row=1, column=0, padx=20, pady=10)

class_label = ttk.Label(common_config_frame,text='Class')
class_label.grid(row=3, column=0, padx=5, pady=(0, 5), sticky="ew")

class__entry = ttk.Entry(common_config_frame)
class__entry.insert(0, "37")
class__entry.bind("<FocusIn>", lambda e: class__entry.delete('0', 'end'))
class__entry.grid(row=4, column=0, padx=5, pady=(0, 5), sticky="w")








notebook = ttk.Notebook(frame)
notebook.grid(row=0,column=1,padx=20,pady=10,sticky='nsew')
tab1 = ttk.Frame(notebook)
notebook.add(tab1,text='Tab1')

window.mainloop()
