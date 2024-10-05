from tkinter import *

window = Tk()

window.geometry('500x700')
window.title('food item list')

list = Listbox(window, height = 50, width = 25, font = 'Calibri')
gamelabel = Label(window, text = 'List of games: ')

list.insert(1, 'Jedi: Fallen Order')
list.insert(2, 'Jedi: Survivor')
list.insert(3, 'Viewfinder')
list.insert(4, 'Superliminal')
list.insert(5, 'EA FC 24')
list.insert(6, 'Fortnite')
list.insert(7, 'Karlson')
list.insert(8, 'Among Us')
list.insert(9, 'Minecraft')
list.insert(10, 'Forza Horizon 5')

gamelabel.pack()
list.pack()
window.mainloop()
