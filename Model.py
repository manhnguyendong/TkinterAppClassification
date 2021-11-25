from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *
from tkinter import messagebox
import pandas as pd
from scipy.stats.stats import ModeResult
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import os

class MODEL:
    def __init__(self) -> None:
        self.name_list = ['Loại I', 'Loại II', 'Loại III', 'Loại IV', 'Loại V', 'Loại VI', 'Loại VII', 'Loại', 'Trả Kết quả']
        self.alter_name_list = ['Loai I', 'Loai II', 'Loai III', 'Loai IV', 'Loai V', 'Loai VI','Loai VII', 'Loai', 'Result']

    def Plot(self, view):
        label = Label(view, text='Plot')
        label.grid(column=1, row=2)

    def toPostgresql(self, view):
        label = Label(view, text='To SQL')
        label.grid(column=1, row=3)

    def toCSV(self, view, data):
        label = Label(view, text='To CSV')
        label.grid(column=1, row=4)
        data.to_csv('out.csv')

    def toExcel(self, view, data):
        label = Label(view, text='To Excel')
        label.grid(column=1, row=5)
        data.to_excel('out.xlsx')

    def accuracy(self, view):
        data = pd.read_csv(self.folder)
        X = data.iloc[:, 2:-1]
        y = data.iloc[:, -1]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3333, random_state=1)

        KNNmodel = KNeighborsClassifier(n_neighbors=5)
        KNNmodel.fit(X_train, y_train)

        y_pred = KNNmodel.predict(X_test)
        accuracy = str(accuracy_score(y_test, y_pred) * 100) + '%'

        Accuracy = Label(view, text=accuracy)
        Accuracy.grid(column=1, row=1)
        # print(accuracy_score(y_test, y_pred))

    def openFile(self):
        self.file_types = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        self.file_name = fd.askopenfilename(
            title= 'Open a file',
            initialdir='/home',
            filetypes=self.file_types
        )

        messagebox.showinfo(
            title='Selected File',
            message=self.file_name
        )

    def PreprocessingData(self, data, alter_name_list, name_list):
        data = data.fillna('0')
        data = data.rename(columns = {x:y for (x, y) in zip(name_list, alter_name_list)})
        
        #covert quality to point
        data['CL'] = data['CL'].map({'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1})
        
        #convert class to Point
        class_lst = []

        for cls_unique in alter_name_list[0:7]:
            class_lst.append(data[cls_unique].unique())

        for cls, name_cls in zip(class_lst, alter_name_list[0:7]):
            cls_map = [int(x[-1]) for x in cls]
            data[name_cls] = data[name_cls].map({x:y for (x, y) in zip(cls, cls_map)})
            
        data['Loai'] = data['Loai'].map({'X' : 1, 'R' : 2})
        data['Result'] = data['Result'].map({'0' : 0, 'có' : 1})

        name_of_folder = self.file_name.split('/')
        self.folder = ''

        for item in name_of_folder[:-1]:
            self.folder = self.folder + item + '/'

        self.folder = self.folder + 'mauxuong.csv'

        data.to_csv(self.folder, index=None)


def main():
    model = MODEL()

if __name__ == "__main__":
    main()