from sorter import Sorter
import tkinter as tk

# Would be nice to add a button to open the file explores and select a file

class App:
    '''A simple GUI application for the sorting system of a folder'''
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x300")
        self.root.resizable(False,False)
        
        #Main frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        #Top title
        self.titleLabel = tk.Label(self.frame, 
                                text="Sortie Sorter",
                                font=("Helvetica", 20))
        self.titleLabel.place(relx=0.5, rely=0, anchor="n")

        # Main directory entry
        self.directoryEntry = tk.Entry(self.frame, 
                                    width=40, 
                                    font=("Helvetica",15))
        self.directoryEntry.place(relx=0.5,rely=0.4, anchor="n")

        # Button for the sorting
        self.sortingButton = tk.Button(self.frame, 
                                    text="Sort folder",
                                    font=("Helvetica",12),
                                    command=self.sortFolder)
        self.sortingButton.place(relx=0.5,rely=0.8, anchor="n")

        #Bindes the Enter key with the sortFolder function
        self.root.bind("<Return>", lambda event: self.sortFolder(event))
        #Error Label
        self.errorLabel = tk.Label(self.frame, text="")
        self.errorLabel.place(relx=0.5,rely=1, anchor="s")

    def sortFolder(self, event):
        #Gets the entry input for the dir
        directory = self.directoryEntry.get()
        if not directory:
            self.errorLabel.config(text="Please enter a directory to be sorted")
            return 
        try:
            sorter = Sorter(directory)
            sorter.sort_files()
            self.errorLabel.config(text="The directory was sorted successfully")
        except Exception as e:
            print(str(e))
            self.errorLabel.config(text=str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()