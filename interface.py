import tkinter
from tkinter import *
import database
from database import *
from tkinter import ttk
#test boutons 



#Configuration de la fenêtre 

window = tkinter.Tk()
window.geometry('1200x720')
window.title('Gestion de Stock')
icon = PhotoImage(file= 'boite-en-carton.png')
window.iconphoto(False, icon)

#Frame de gauche qui comporte les informations des produits du stock

frame = tkinter.Frame(window)
frame.pack()

Gestion_stock = tkinter.LabelFrame(frame, text="Produits en stock", width= 900, height=700)
Gestion_stock.grid(row=0, column=0, sticky='w')

#Le Tree qui comporte les informations

tree = ttk.Treeview(Gestion_stock, columns= (1,2,3,4,5,6), height= 5, show="headings")
tree.place(width=890, height=680)


tree.heading(1, text= "ID")
tree.heading(2, text= "NOM")
tree.heading(3, text= "DESCRIPTION")
tree.heading(4, text= "PRIX")
tree.heading(5, text= "QUANTITE")
tree.heading(6, text= "ID_CATEGORIE")

tree.column(1, width=20)
tree.column(2, width=150)
tree.column(3, width=600)
tree.column(4, width=30)
tree.column(5, width=30)
tree.column(6, width=20)

affich = 'SELECT * FROM produit'
database.cursor.execute(affich)

for row in database.cursor:
    tree.insert('', END, values = row)

#Frame de droite avec les boutons qui permettent 

Modify_frame = tkinter.LabelFrame(frame, text="Modificateur", width= 230, height=700)
Modify_frame.grid(row=0, column=1, padx=10, pady=10, sticky='e')

add_button = tkinter.Button(Modify_frame, text= "Ajouter un produit")
add_button.grid(row =6, column=0, padx=70, pady=100)

modify_button = tkinter.Button(Modify_frame, text= "Modifier un produit")
modify_button.grid(row =7, column=0, padx=70, pady=100)

delete_button = tkinter.Button(Modify_frame, text= "Supprimer un produit")
delete_button.grid(row =8, column=0, padx=70, pady=100)





window.mainloop()