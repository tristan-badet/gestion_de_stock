import tkinter
from tkinter import *
import database
from database import *
from tkinter import ttk
#test boutons 
class boutons_modif():

    def addNewWindow(self):
        self.addWindow = Toplevel()
        self.addWindow.title('Ajouter un produit')
        self.addWindow.geometry("500x500")

        self.id_label = tkinter.Label(self.addWindow, text= "ID")
        self.id_label.grid(row=0, column=0, padx=20, pady=20)
        self.id_entry = tkinter.Entry(self.addWindow, font=('Times', 12))
        self.id_entry.grid(row=0, column=1, padx=20, pady=20)

        self.nom_label = tkinter.Label(self.addWindow, text= "NOM")
        self.nom_label.grid(row=1, column=0, padx=20, pady=20)
        self.nom_entry = tkinter.Entry(self.addWindow, font=('Times', 12))
        self.nom_entry.grid(row=1, column=1, padx=20, pady=20)

        self.descriptif_label = tkinter.Label(self.addWindow, text= "DESCRIPTION")
        self.descriptif_label.grid(row=2, column=0, padx=20, pady=20)
        self.description_entry = tkinter.Entry(self.addWindow, font=('Times', 12))
        self.description_entry.grid(row=2, column=1, padx=20, pady=20)

        self.prix_label = tkinter.Label(self.addWindow, text= "PRIX")
        self.prix_label.grid(row=3, column=0, padx=20, pady=20)
        self.prix_entry = tkinter.Entry(self.addWindow, font=('Times', 12))
        self.prix_entry.grid(row=3, column=1, padx=20, pady=20)

        self.quantite_label = tkinter.Label(self.addWindow, text= "QUANTITE")
        self.quantite_label.grid(row=4, column=0, padx=20, pady=20)
        self.quantite_entry = tkinter.Entry(self.addWindow, font=('Times', 12))
        self.quantite_entry.grid(row=4, column=1, padx=20, pady=20)

        self.id_categorie_label = tkinter.Label(self.addWindow, text= "ID_CATEGORIE")
        self.id_categorie_label.grid(row=5, column=0, padx=20, pady=20)
        self.id_categorie_entry = tkinter.Entry(self.addWindow, font=('Times', 12))
        self.id_categorie_entry.grid(row=5, column=1, padx=20, pady=20)

        self.validation_button = ttk.Button(self.addWindow, text="Valider", command=lambda: self.validationAdd())
        self.validation_button.grid(row= 6, column= 1, padx=20, pady=20)

    def validationAdd(self):
        check1 = self.id_entry.get()
        check2 = self.nom_entry.get()
        check3 = self.description_entry.get()
        check4 = self.prix_entry.get()
        check5 = self.quantite_entry.get()
        check6 = self.id_categorie_entry.get()

        if check1 != "" and check2 != "" and check3 != "" and check4 != "" and check5 != "" and check6 != "":
            sql = "INSERT INTO produit VALUES (%s, %s, %s, %s, %s, %s)"
            val = ("{}".format(check1),"{}".format(check2), "{}".format(check3), "{}".format(check4), "{}".format(check5), "{}".format(check6))
            database.cursor.execute(sql, val)
            database.mydb.commit()
            tree.insert('', 'end', text= "", values=(check1, check2, check3, check4, check5, check6))
            self.addWindow.destroy()
            database.cursor.close()
    
    def deleteRow(self):
        self.selected_item = tree.selection()[0]
        self.id_recup = tree.item(self.selected_item)['values'][0]
        self.sql2 = "DELETE FROM produit WHERE id = {}".format(self.id_recup)
        database.cursor.execute(self.sql2)
        database.mydb.commit()
        tree.delete(self.selected_item)

    def modifyNewWindow(self):
        self.selected_item2 = tree.selection()[0]
        self.modifyWindow = Toplevel()
        self.modifyWindow.title('Modifier le produit')
        self.modifyWindow.geometry('500x500')

        self.id_label2 = tkinter.Label(self.modifyWindow, text= "ID")
        self.id_label2.grid(row=0, column=0, padx=20, pady=20)
        self.id_entry2 = tkinter.Entry(self.modifyWindow, font=('Times', 12))
        self.id_entry2.insert(0, "{}".format(tree.item(self.selected_item2)['values'][0]))
        self.id_entry2.grid(row=0, column=1, padx=20, pady=20)

        self.nom_label2 = tkinter.Label(self.modifyWindow, text= "NOM")
        self.nom_label2.grid(row=1, column=0, padx=20, pady=20)
        self.nom_entry2 = tkinter.Entry(self.modifyWindow, font=('Times', 12))
        self.nom_entry2.insert(0, "{}".format(tree.item(self.selected_item2)['values'][1]))
        self.nom_entry2.grid(row=1, column=1, padx=20, pady=20)

        self.descriptif_label2 = tkinter.Label(self.modifyWindow, text= "DESCRIPTION")
        self.descriptif_label2.grid(row=2, column=0, padx=20, pady=20)
        self.description_entry2 = tkinter.Entry(self.modifyWindow, font=('Times', 12))
        self.description_entry2.insert(0, "{}".format(tree.item(self.selected_item2)['values'][2]))
        self.description_entry2.grid(row=2, column=1, padx=20, pady=20)

        self.prix_label2 = tkinter.Label(self.modifyWindow, text= "PRIX")
        self.prix_label2.grid(row=3, column=0, padx=20, pady=20)
        self.prix_entry2 = tkinter.Entry(self.modifyWindow, font=('Times', 12))
        self.prix_entry2.insert(0, "{}".format(tree.item(self.selected_item2)['values'][3]))
        self.prix_entry2.grid(row=3, column=1, padx=20, pady=20)

        self.quantite_label2 = tkinter.Label(self.modifyWindow, text= "QUANTITE")
        self.quantite_label2.grid(row=4, column=0, padx=20, pady=20)
        self.quantite_entry2 = tkinter.Entry(self.modifyWindow, font=('Times', 12))
        self.quantite_entry2.insert(0, "{}".format(tree.item(self.selected_item2)['values'][4]))
        self.quantite_entry2.grid(row=4, column=1, padx=20, pady=20)

        self.id_categorie_label2 = tkinter.Label(self.modifyWindow, text= "ID_CATEGORIE")
        self.id_categorie_label2.grid(row=5, column=0, padx=20, pady=20)
        self.id_categorie_entry2 = tkinter.Entry(self.modifyWindow, font=('Times', 12))
        self.id_categorie_entry2.insert(0, "{}".format(tree.item(self.selected_item2)['values'][5]))
        self.id_categorie_entry2.grid(row=5, column=1, padx=20, pady=20)

        self.validation_button2 = ttk.Button(self.modifyWindow, text="Valider", command=lambda: self.validationModify())
        self.validation_button2.grid(row= 6, column= 1, padx=20, pady=20)
    
    def validationModify(self):
        check2_1 = self.id_entry2.get()
        check2_2 = self.nom_entry2.get()
        check2_3 = self.description_entry2.get()
        check2_4 = self.prix_entry2.get()
        check2_5 = self.quantite_entry2.get()
        check2_6 = self.id_categorie_entry2.get()
        tree.item(self.selected_item2, values=(check2_1, check2_2, check2_3, check2_4, check2_5, check2_6))

        if check2_1 != "" and check2_2 != "" and check2_3 != "" and check2_4 != "" and check2_5 != "" and check2_6 != "":
            sql3 = "UPDATE produit SET id = {}, nom = '{}', description = '{}', prix = {}, quantité = {}, id_catégorie = {} WHERE id = {}".format(check2_1, check2_2, check2_3, check2_4, check2_5, check2_6, tree.item(self.selected_item2)['values'][0])
            database.cursor.execute(sql3)
            database.mydb.commit()
            self.modifyWindow.destroy()
            database.cursor.close()

bouton_modif = boutons_modif()

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

add_button = ttk.Button(Modify_frame, text= "Ajouter un produit", command=lambda :bouton_modif.addNewWindow())
add_button.grid(row =6, column=0, padx=70, pady=100)

modify_button = ttk.Button(Modify_frame, text= "Modifier un produit", command= lambda : bouton_modif.modifyNewWindow())
modify_button.grid(row =7, column=0, padx=70, pady=100)

delete_button = ttk.Button(Modify_frame, text= "Supprimer un produit", command=lambda: bouton_modif.deleteRow())
delete_button.grid(row =8, column=0, padx=70, pady=100)


window.mainloop()