#multichoice task

from select import select
from tkinter import *





class Quiz:
    def __init__(self, parent):
        self.selected_footballer = StringVar()
      

        f1 = Frame(parent)
        
        

        Label( text = "Question:").grid(column=0,row=0,sticky=W)
        Label(parent, text= "Who is the best Footballer of all time?",font=('Helvatical bold',16)).grid(column=0,row=1,sticky=W,pady=6)

        footballer_list = ["Cristiano Ronaldo", "Harry Maguire", "Lionel Messi", "Pele"]
        
        r = 2
        for i in(footballer_list):
            Radiobutton(f1, text=i, value=i, variable=self.selected_footballer, command=self.display_choice).grid(column=0, row=r, sticky=W,pady=5)
            r += 1

    
        f1.grid()

        
        self.output_label = Label(parent, text="Answer")
        self.output_label.grid(padx=10,pady=10)
   

    def display_choice(self):
        if self.selected_footballer.get() == "Harry Maguire":
            self.output_label.configure(text="Correct")

        else:
            self.output_label.configure(text="Incorect")
           



if __name__ == "__main__":
    root = Tk()
    buttons = Quiz(root)
    root.mainloop()

