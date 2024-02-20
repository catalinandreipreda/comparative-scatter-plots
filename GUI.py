from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data import *

class GUI:
    def __init__(self, dataset):
        """
        Constructor creating the root window.
        :param dataset: (pandas dataframe) dataset with student marks (Student ID x Module Name)
        """
        # Setting up the GUI window
        self.window = Tk()
        self.window.title("Comparative Scatter Plots")
        self.window.geometry("800x500")
        # Initialise variables
        self.dataset = dataset
        """Adding two identical frames holding a combobox and a scatter plot """
        # Adding content on the left
        left_frame = Frame(self.window)
        self.add_scatter(left_frame)
        left_frame.grid(row=0, column= 0)
        # Adding content on the right
        right_frame = Frame(self.window)
        self.add_scatter(right_frame)
        right_frame.grid(row=0, column=1)
        
        # Display everything
        self.window.mainloop()







    def add_scatter(self, frame):

        marks = module_marks("CSE110", self.dataset)
        averages = exclusive_averages("CSE110", self.dataset)

        def diplay_plot(x, y):
            figure = plt.Figure(figsize=(4, 4), dpi=100)
            scatter_plt= figure.add_subplot(111)
            scatter_plt.scatter(x, y)


            # Regression line

            # x.dropna(inplace=True)
            # y.dropna(inplace=True)
            # slope, intercept = np.polyfit(x, y, deg=1)
            # reg_seq = np.linspace(0, 10, num=100)
            # figure.add_subplot(111).plot(reg_seq, intercept + slope * reg_seq, color="k", lw=2.5)

            canvas = FigureCanvasTkAgg(figure, frame)
            canvas.get_tk_widget().grid(row=1)
        diplay_plot(averages, marks)

        def comboclick(event):
            try:
                y = module_marks(selector.get(), self.dataset)
                x = exclusive_averages(selector.get(), self.dataset)
            except ValueError:
                y = module_marks("CSE101", self.dataset)
                x = exclusive_averages("CSE101", self.dataset)
            finally:
               diplay_plot(x, y)




        content = self.dataset.columns.tolist()
        content.remove('Student IDs')
        value = StringVar()
        selector = ttk.Combobox(frame,  value = content)
        selector.set( "Select module")
        selector['state'] = 'readonly'
        selector.grid(row=0)
        selector.bind("<<ComboboxSelected>>", comboclick)












