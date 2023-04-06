import database
from database import *

class Modifications():

    def insert(id, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employes VALUES (%s, %s, %s, %s, %s)"    
        val = ("{}".format(id),"{}".format(nom), "{}".format(prenom), "{}".format(salaire), "{}".format(id_service))
        database.cursor.execute(sql, val)
        database.mydb.commit()

    def read(colonne):
        sql = "SELECT {} FROM employes".format(colonne)
        database.cursor.execute(sql)
        affich = database.cursor.fetchall()
        print(affich)

    def  update(salaire, prenom):
        sql = "UPDATE employes SET salaire = {} WHERE prenom = {}".format(salaire, prenom)
        database.cursor.execute(sql)
        database.mydb.commit()

    def delete(id):
        sql = "DELETE FROM `employes` WHERE `id` = {}".format(id)
        database.cursor.execute(sql)
        database.mydb.commit()

    
