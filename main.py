import tkinter as tk
from tkinter import ttk
import openpyxl

# Theme Github repo: github.com/rdbende/Forest-ttk-theme


class Classwork_statistic:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('班级课堂作业统计')

        # Create a style
        self.style = ttk.Style(self.window)
        # Import the tcl file
        # See more: Https://github.com/rdbende/Forest-ttk-theme
        self.window.tk.call('source','forest-dark.tcl')
        self.window.tk.call('source','forest-light.tcl')
        # Set theme
        self.style.theme_use('forest-light')

        self.frame_top = self.create_frame_top(self.window)
        self.frame_down = self.create_frame_down(self.window)

        self.common_configure_frame = self.create_common_configure_frame(self.frame_top)
        self.statistic_frame = self.create_statistic_frame(self.frame_top)

        self.create_common_widgets(self.common_configure_frame)
        self.create_statistic_widgets(self.statistic_frame)

        self.notebook = self.create_notebook(self.frame_down)
        self.notebook.add(self.create_tab(),text='Tab1')
        self.notebook.add(self.create_tab(),text='Tab2')

    def run(self):
        self.window.mainloop()

    def create_frame_top(self,frame):
        self.frame = frame
        frame_top = ttk.Frame(self.frame)
        frame_top.pack(side=tk.TOP,fill=tk.X)
        return frame_top

    def create_frame_down(self,frame):
        self.frame = frame
        frame_down = ttk.Frame(self.frame)
        frame_down.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        return frame_down


    def create_notebook(self,frame):
        self.frame = frame
        notebook = ttk.Notebook(self.frame)
        notebook.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        return notebook

    def create_common_configure_frame(self,frame):
        self.frame = frame
        common_configure_frame = ttk.LabelFrame(self.frame,text='常规设置')
        common_configure_frame.pack(side=tk.LEFT,fill=tk.Y,padx=2,pady=2)
        return common_configure_frame

    def create_statistic_frame(self,frame):
        self.frame = frame
        statistic_frame = ttk.LabelFrame(self.frame,text='统计')
        statistic_frame.pack(side=tk.LEFT,fill=tk.Y,padx=2,pady=2)
        return statistic_frame

    def create_tab(self):
        tab = ttk.Frame(self.notebook)
        return tab

    def create_common_widgets(self,frame):
        self.frame = frame

        frame1 = ttk.Frame(self.frame)
        frame1.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2)

        frame2 = ttk.Frame(self.frame)
        frame2.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2)

        frame3 = ttk.Frame(self.frame)
        frame3.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2)

        classwork_dir_label = ttk.Label(frame1,text='作业根目录')
        classwork_dir_label.pack(side=tk.LEFT,pady=2)

        classwork_dir_entry = ttk.Entry(frame1,width=50)
        classwork_dir_entry.insert(0,'/home/dd/Desktop/Repositories/Classwork-Statistic-App')
        classwork_dir_entry.pack(side=tk.LEFT,pady=2,padx=2)
        classwork_dir_button = ttk.Button(frame1,text='选择')
        classwork_dir_button.pack(side=tk.LEFT,padx=2,pady=2)

        classes_dir_label = ttk.Label(frame2,text='班级信息根目录')
        classes_dir_label.pack(side=tk.LEFT,pady=2)
        classes_dir_entry = ttk.Entry(frame2,width=50)
        classes_dir_entry.insert(0,'/home/dd/Desktop/Repositories/Classwork-Statistic-App')
        classes_dir_entry.pack(side=tk.LEFT,padx=2,pady=2)
        classes_dir_button = ttk.Button(frame2,text='选择')
        classes_dir_button.pack(side=tk.LEFT,padx=2,pady=2)

        style_switch =  ttk.Checkbutton(frame3,text='界面风格',style='Switch')
        style_switch.pack(side=tk.LEFT,padx=2,pady=2)

    def create_statistic_widgets(self,frame):
        self.frame = frame 
        frame1 = ttk.Frame(self.frame)
        frame1.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2)

        frame2 = ttk.Frame(self.frame)
        frame2.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2)

        frame3 = ttk.Frame(self.frame)
        frame3.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2)

        class_entry = ttk.Entry(frame1,width=5)
        class_entry.insert(0,'62')
        class_entry.bind('<FocusIn>',lambda e: class_entry.delete('0','end'))
        class_entry.pack(side=tk.LEFT,padx=2,pady=2)
        class_label = ttk.Label(frame1,text='班')
        class_label.pack(side=tk.LEFT,padx=2,pady=2)

        week_label = ttk.Label(frame1,text=' ,第')
        week_label.pack(side=tk.LEFT,padx=2,pady=2)

        week_entry = ttk.Entry(frame1,width=5)
        week_entry.insert(0,'1')
        week_entry.bind('<FocusIn>',lambda e: week_entry.delete('0','end'))
        week_entry.pack(side=tk.LEFT,padx=2,pady=2)

        week_label2 = ttk.Label(frame1,text='至')
        week_label2.pack(side=tk.LEFT,padx=2,pady=2)

        week_entry2 = ttk.Entry(frame1,width=5)
        week_entry2.insert(0,'')
        week_entry2.bind('<FocusIn>',lambda e: week_entry2.delete('0','end'))
        week_entry2.pack(side=tk.LEFT,padx=2,pady=2)

        week_label3 = ttk.Label(frame1,text='周')
        week_label3.pack(side=tk.LEFT,padx=2,pady=2)

        query_button = ttk.Button(frame3,text='统计')
        query_button.pack(side=tk.LEFT,padx=2,pady=5)
        save_button = ttk.Button(frame3,text='导出')
        save_button.pack(side=tk.RIGHT,padx=2,pady=5)




if __name__ == '__main__':
    cs = Classwork_statistic()
    cs.run()
