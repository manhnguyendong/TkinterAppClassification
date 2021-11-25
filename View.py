from tkinter import *
from tkinter import font
from tkinter.ttk import *


class VIEW:
    def __init__(self) -> None:
        self._width_col = 60
        self._height_treeView = 30
        self._list_name = ['CL', 'PL', 'Loai I', 'Loai II', 'Loai III', 'Loai IV', 'Loai V', 'Loai VI', 'Loai VII', 'Loai', 'Result']
        self.InitWindow()

    def InitWindow(self):
        self.root = Tk()
        self.root.title("Skeleton Classification")
        self.root.geometry("1000x800")
        self.root.columnconfigure(0, weight=5)
        self.root.columnconfigure(1, weight=3)
        self.InitINPUT()

    def InitINPUT(self):
        self.CreateFrame()
        self.CreateLabel()
        self.CreateTreeView()
        self.CreateButton()

    def CreateFrame(self):
        self.inputFrame = Frame(self.root)
        self.inputFrame.grid(column=0, row=0, sticky='NSEW')
        self.outputFrame = Frame(self.root)
        self.outputFrame.grid(column=1, row=0, sticky='NSEW')
        self.treeViewFrame = Frame(self.inputFrame, height=400)
        self.treeViewFrame.grid(column=0, row=1, sticky='NSEW')
    
    def CreateLabel(self):
        self.LabelInput = Label(self.inputFrame, text='Input', font=('Helvetica', 20))
        self.LabelInput.grid(column=0, row=0)
        self.LabelOutput = Label(self.outputFrame, text='Output', font=('Helvetica', 20))
        self.LabelOutput.grid(column=1, row=0)
        self.LabelInputFrom = LabelFrame(self.inputFrame, text='Input From')
        self.LabelInputFrom.grid(column=0, row=2)

    def CreateButton(self):
        self.InputFromExcel = Button(self.LabelInputFrom, text='From Data', command=None)
        self.InputFromExcel.grid(column=0, row=0, ipady=10, ipadx=15, padx=10)

        self.InputFromDataset = Button(self.LabelInputFrom, text='From Dataset(.csv)', command=None)
        self.InputFromDataset.grid(column=1, row=0, ipady=10, ipadx=5)
        
        self.Generate = Button(self.LabelInputFrom, text='Generate', command=None)
        self.Generate.grid(column=2, row=0, ipady=10, ipadx=5, padx=10)

        self.Accuracy = Button(self.outputFrame, text='Accuracy', command=None)
        self.Accuracy.grid(column=0, row=1, ipadx=10, padx=5)

        self.Plot = Button(self.outputFrame, text='Plot', command=None)
        self.Plot.grid(column=0,row=2, ipadx=10, pady=20)

        self.ExportToPostgresql = Button(self.outputFrame, text='To Postgresql', command=None)
        self.ExportToPostgresql.grid(column=0, row=3)

        self.ExportToCSV = Button(self.outputFrame, text='To CSV', command=None)
        self.ExportToCSV.grid(column = 0, row=4, pady=20, ipadx=10)

        self.ExportToExcel = Button(self.outputFrame, text='To Excel', command=None)
        self.ExportToExcel.grid(column=0, row=5, ipadx=20)

        # self.SetStyleForButton()

    def CreateTreeView(self):

        self.treeview = Treeview(self.treeViewFrame, selectmode='browse', height=self._height_treeView)
        self.treeview.grid(column=0, row=1, sticky='W')

        self.verticalScrollBar = Scrollbar(self.inputFrame, orient='vertical', command=self.treeview.yview)
        self.verticalScrollBar.place(x='780', y='28', height=610)

        self.treeview.configure(yscrollcommand=self.verticalScrollBar.set)
        
        self.treeview['columns'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')
        self.treeview['show'] = 'headings'

        self.treeview.column('1', width=30, anchor='c')
        self.treeview.heading('1', text='ID')
        self.treeview.column('2', width=80, anchor='c')
        self.treeview.heading('2', text='Sample')
        self.treeview.column('13', width=80, anchor='c')
        self.treeview.heading('13', text='Result')

        for (i, heading) in zip(range(3, 13), self._list_name):
            self.treeview.column(str(i), width=self._width_col, anchor='c')
            self.treeview.heading(str(i), text=heading)


def main():
    view = VIEW()
    mainloop()

if __name__ == "__main__":
    main()