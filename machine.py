from tkinter import *
import csv

#écrire l'endroit ou se trouve le dossier du code + image
path = #mettez l'endroit où se trouve votre dossier

with open(path+'produit.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    dico = dict(list(reader)[0])

l_piece_rendre = [200,100,50,20,10,5,2,1]
l_piece_rendu = []
argent = 0

#affiche le nombre de pièce que la personne a mise
def piece_total(valeur):
    global argent
    argent += valeur
    nb_piece_texte.configure(text='Argents insérés : '+str(float(argent/100))+' €')

#réinitialise les variables
def reinitalisation():
    global l_piece_rendu
    global argent
    l_piece_rendu = []
    argent = 0
    nb_piece_texte.config(text='Argents insérés : '+str(float(argent/100))+' €')


def monnais(argent=0):
    #prend le texte de la listbox
    for i in lbx.curselection():
        choix = lbx.get(i)

    #la liste l_piece_rendu aura le nombre de pièce à rendre
    x = 0
    presence_piece = None
    global l_piece_rendu
    for i in range(len(l_piece_rendre)):
        l_piece_rendu.append(0)
    if argent-int(dico[choix]) >= 0:
        presence_piece = True
        valeur_a_rendre = argent-int(dico[choix])
        while valeur_a_rendre > 0:
            if valeur_a_rendre >= l_piece_rendre[x]:
                valeur_a_rendre -= l_piece_rendre[x]
                l_piece_rendu[x] += 1
            elif valeur_a_rendre < l_piece_rendre[x]:
                x += 1
    else:
        presence_piece = False
    
    #créer une nouvelle page
    new_page = Toplevel(page)
    #si argent suffisant alors...
    if presence_piece == True:
        texte_piece = Label(new_page, text='Pièces rendus :\n'
        'pièce 2.00 € : '+str(l_piece_rendu[0])+'\n'
        'pièce 1.00 € : '+str(l_piece_rendu[1])+'\n'
        'pièce 0.50 € : '+str(l_piece_rendu[2])+'\n'
        'pièce 0.20 € : '+str(l_piece_rendu[3])+'\n'
        'pièce 0.10 € : '+str(l_piece_rendu[4])+'\n'
        'pièce 0.05 € : '+str(l_piece_rendu[5])+'\n'
        'pièce 0.02 € : '+str(l_piece_rendu[6])+'\n'
        'pièce 0.01 € : '+str(l_piece_rendu[7])+'\n').pack()
        
        ok_button = Button(new_page, text='ok', command=lambda:[reinitalisation(),new_page.destroy()]).pack()
    #si argent pas suffisant alors...
    elif presence_piece == False:
        texte_piece = Label(new_page, text="Aucune pièce n'a été inséré").pack()
        
        ok_button = Button(new_page, text='ok', command=lambda:[reinitalisation(),new_page.destroy()]).pack()


#créer la page
page = Tk()
page.title('distributeur')
page.geometry('1250x600')

#affiche nombre total de pièces insérés
nb_piece_texte = Label(text='Argents insérés : '+str(float(argent/100))+' €')

#créer une listbox pour que la personne choisis son article
lbx = Listbox(page)
lbx.insert(1, 'Cafe')
lbx.insert(2, 'Bonbon')
lbx.insert(3, 'Enfant')

#avoir les images pour les utiliser
piece1 = PhotoImage(file=path+'assets/piece1.png')
piece2 = PhotoImage(file=path+'assets/piece2.png')
piece5 = PhotoImage(file=path+'assets/piece5.png')
piece10 = PhotoImage(file=path+'assets/piece10.png')
piece20 = PhotoImage(file=path+'assets/piece20.png')
piece50 = PhotoImage(file=path+'assets/piece50.png')
piece100 = PhotoImage(file=path+'assets/piece100.png')
piece200 = PhotoImage(file=path+'assets/piece200.png')

lbx.pack()
texte = Label(text='Prix :\nCafe : 0.50 €\nBonbon : 1.50 €\nEnfant : 2.00 €').pack()
nb_piece_texte.pack()
button_payer = Button(page, text='Payer', command=lambda:[monnais(argent)]).pack()

#les bouton seront sur la même ligne
frame = Frame(page)
frame.pack(expand=YES)

button_piece1 = Button(page, height = 150, width = 150, image=piece1, command=lambda:piece_total(1)).pack(side=LEFT)
button_piece2 = Button(page, height = 150, width = 150, image=piece2, command=lambda:piece_total(2)).pack(side=LEFT)
button_piece5 = Button(page, height = 150, width = 150, image=piece5, command=lambda:piece_total(5)).pack(side=LEFT)
button_piece10 = Button(page, height = 150, width = 150, image=piece10, command=lambda:piece_total(10)).pack(side=LEFT)
button_piece20 = Button(page, height = 150, width = 150, image=piece20, command=lambda:piece_total(20)).pack(side=LEFT)
button_piece50 = Button(page, height = 150, width = 150, image=piece50, command=lambda:piece_total(50)).pack(side=LEFT)
button_piece100 = Button(page, height = 150, width = 150, image=piece100, command=lambda:piece_total(100)).pack(side=LEFT)
button_piece200 = Button(page, height = 150, width = 150, image=piece200, command=lambda:piece_total(200)).pack(side=LEFT)

page.mainloop()
