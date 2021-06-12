from tkinter import *
import queue
import threading
from tkinter.ttk import *
class ThreadedTask(object):
    def __init__(self, parent):
        self.parent = parent
        self.queue = queue.Queue()
        self.gui = MyGui(parent, self.queue)
        self.work_queue()
    def work_queue(self):
        """ Check every 100 ms if there is something new in the queue. """
        try:
            self.parent.after(200, self.work_queue)
            print('working queue with task {}...'.format(self.queue.get_nowait()))
        except queue.Empty:
            pass
# Gui class
class MyGui(Frame):
    def __init__(self, parent, queue):
        super().__init__(parent)
        self.parent = parent
        self.queue = queue
        self.init_ui()
    # define a button to fulfill long task
    def init_ui(self):
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.grid(row=0, column=0, columnspan=1, sticky='ns')
        self.status_frame = Frame(self, relief=RAISED, borderwidth=1, height=20)
        self.status_frame.grid(row=1, column=0, columnspan=3, sticky='nesw')
        self.status_frame.grid_configure(padx=3, pady=3)
        self.button = Button(self.frame, text='do Stuff', command=self.init_button_loop)
        self.button.grid(padx=3, pady=3)
        self.progress = Progressbar(self.status_frame, orient="horizontal", length=80, mode="determinate")
        self.progress.grid(row=1, column=0, pady=3, sticky='nesw')
        self.grid()
    def start_thread(self, function_name, queue):
        t = threading.Thread(target=function_name, args=(queue,))
        # close thread automatically after finishing task
        t.setDaemon(True)
        t.start()
    # execute button push by spawning a new thread
    def init_button_loop(self):
        self.start_thread(self.exec_button_loop, self.queue)
    # execute long task
    def exec_button_loop(self, queue):
        self.progress['maximum'] = 10000
        for i in range(10000):
            # update progressbar
            queue.put(self.progress.step())
# main
root = Tk()
root.geometry("150x80+50+50")
client = ThreadedTask(root)
root.mainloop()