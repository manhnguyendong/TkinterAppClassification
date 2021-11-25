from os import read
from tkinter import Label, mainloop, messagebox
from tkinter.constants import END, LAST
from tkinter.filedialog import test

from pandas.io.parsers import read_csv
from Model import MODEL
from View import VIEW
import pandas as pd
import csv


class CONTROLLER:
    def __init__(self) -> None:
        self.model = MODEL()
        self.view = VIEW()
        self.checkGenerate = 0
        self.check = 0
        self.SetupCONTROLLER()

    def SetupCONTROLLER(self):
        self.SetupCommand()

    def SetupCommand(self):
        self.view.Accuracy['command'] = self.accuracy
        self.view.Plot['command'] = self.plot
        self.view.ExportToPostgresql['command'] = self.toPostgresql
        self.view.ExportToCSV['command'] = self.toCSV
        self.view.ExportToExcel['command'] = self.toExcel
        self.view.InputFromDataset['command'] = self.fromDataset
        self.view.InputFromExcel['command'] = self.fromExcel
        self.view.Generate['command'] = self.GenerateData

    def accuracy(self):
        if (self.checkGenerate):
            self.model.accuracy(self.view.outputFrame)
        else:
            messagebox.showerror(title='Error', message='Please generate data !')

    def plot(self):
        if (self.checkGenerate):
            self.model.Plot(self.view.outputFrame)
        else:
            messagebox.showerror(title='Error', message='Please generate data !')

    def toPostgresql(self):
        if (self.checkGenerate):
            self.model.toPostgresql(self.view.outputFrame)
        else:
            messagebox.showerror(title='Error', message='Please generate data !')

    def toCSV(self):
        if (self.checkGenerate):
            data_set = pd.read_csv(self.folder)
            self.model.toCSV(self.view.outputFrame, data=data_set)
        else:
            messagebox.showerror(title='Error', message='Please generate data !')

    def toExcel(self):
        if (self.checkGenerate):
            data_set = pd.read_csv(self.folder)
            self.model.toExcel(self.view.outputFrame, data=data_set)
        else:
            messagebox.showerror(title='Error', message='Please generate data !')

    def fromDataset(self):
        self.model.openFile()
        self.check = 1
        self.displayDataToTreeview_FileDataset()

    def displayDataToTreeview_FileDataset(self):
        self.view.treeview.delete(*self.view.treeview.get_children())
        if ('.csv' in self.model.file_name):
            with open(self.model.file_name) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    id = row['Unnamed: 0']
                    sample = row['Sample']
                    cl = row['CL']
                    pl = row['PL']
                    loai1 = row['Loai I']
                    loai2 = row['Loai II']
                    loai3 = row['Loai III']
                    loai4 = row['Loai IV']
                    loai5 = row['Loai V']
                    loai6 = row['Loai VI']
                    loai7 = row['Loai VII']
                    loai = row['Loai']
                    result = row['Result']
                    self.view.treeview.insert("", 'end', values=(id, sample, cl, pl, loai1, loai2, loai3, loai4,
                                                                    loai5, loai6, loai7, loai, result))
        else:
            messagebox.showerror(title='Invalid file', message='Please select CSV file! Thank you !')

    def fromExcel(self):
        self.model.openFile()
        self.check = 1
        self.displayDataToTreeView_ExcelFile()
        
    def displayDataToTreeView_ExcelFile(self):
        self.view.treeview.delete(*self.view.treeview.get_children())
        if ('.xlms' in self.model.file_name):
            df = pd.read_excel(self.model.file_name)
            df_rows = df.to_numpy().tolist()
            for row in df_rows:
                self.view.treeview.insert("", "end", values=row)
        elif('.ods' in self.model.file_name):
            df = pd.read_excel(self.model.file_name, engine='odf')
            df.insert(0, 'ID', range(df.shape[0]))
            df_rows = df.to_numpy().tolist()
            # i = 0
            for row in df_rows:
                # self.view.treeview.insert('', 'end', values=i)
                self.view.treeview.insert("", "end", values=(row))
        else:
            messagebox.showerror(title='Invalid file', message='Please select .xlms if Window, .ods if Linux(Ubuntu) file! Thank you !')

    def GenerateData(self):
        if(self.check):
            if ('.csv' in self.model.file_name):
                data = pd.read_csv(self.model.file_name)
            elif ('.xlms' in self.model.file_name):
                data = pd.read_excel(self.model.file_name)
            elif ('.ods' in self.model.file_name):
                data = pd.read_excel(self.model.file_name, engine='odf')

            self.model.PreprocessingData(data=data, alter_name_list=self.model.alter_name_list, name_list=self.model.name_list)

            messagebox.showinfo(title='Successfully', message='Finished preprocessing data and click OK to display result on Treeview !!!')

            self.view.treeview.delete(*self.view.treeview.get_children())

            self.folder = self.model.folder

            data = pd.read_csv(self.folder)
            data.insert(0, 'ID', value=range(data.shape[0]))

            data.to_csv(self.folder, index=None)

            list_name = list(data.columns)

            with open(self.folder) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    values = []
                    for name in list_name:
                        values.append(row[name])
                    self.view.treeview.insert('', 'end', values=values)

            self.checkGenerate = 1
        else:
            messagebox.showerror(title='File not found', message='Make sure that address of file which you choose is not empty')

def main():
    control = CONTROLLER()
    mainloop()

if __name__ == "__main__":
    main()