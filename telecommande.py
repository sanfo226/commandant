import random
import time

class commande():

     def __init__(self,etat_TV ="fermer",volume = 0,liste_de_chaine = ["rtb"], chaine="rtb"):
         self.etat_TV = etat_TV
         self.liste_de_chaine = liste_de_chaine
         self.volume = volume
         self.chaine = chaine

     def tv_ouvert(self):
         if (self.etat_TV =="ouvert"):
             print("la televison est deja ouverte")
         else:
             print("ouverture de la television...")
             self.etat_TV = "ouvert"

     def tv_fermer(self):
         if(self.etat_TV =="fermer"):
             print ("la television est deja fermer")
         else:
             print("fermeture de la televison...")
             self.etat_TV = "fermer"

     def para_volume(self):
         while True:
             reponse=input("augmentez le volume:'+'\nbaissez le volume:'-'\nsortir:sortir")
             if (reponse== "+"):
                 if(self.volume !=32):
                     self.volume+=1
                     print("volume:",self.volume)
             elif(reponse =="-"):
                    if(self.volume !=0):
                     self.volume-=1
                     print("volume:",self.volume)
             else:
                 print("le volume a ete mis a jour:",self.volume)
                 break

             def ajout_chaine(self,nom_de_chaine):
                 print("ajout du nom de la chaine...")
                 time.sleep(2)

                 self.liste_de_chaine.append(nom_de_chaine)
                 print ("chaine ajoutee")

             def choix_aleatoire(self):
                 aleatoire = random.randint(0,len(self.liste_de_chaine)-1)
                 self.liste_de_chaine=self.liste_de_chaine[aleatoire]
                 print("la chaine actuel",self.liste_de_chaine)

             def __len__(self):
                  return len(self.liste_de_chaine)
             def str(self):
                  return "etat de la tv: {}\nvolume: {} \n liste de chaine: {}\nla chaine actuelle: {}".format(self.etat_TV,self.volume,self.liste_de_chaine,self.chaine)
commande=commande()

print ("""
 programe de tele
              
1.ouvrez la tele
              
2.fermez la tele
              
3.ajustez le volume
              
4.ajoutez de chaine
              
5.le nombre de chaine
              
6.chaine aleatoire   
                         
7.les infos tv
              
 pour terminer cliqué sur "q" """)
while True:

    proceder= input("choisissez un numero")

    if (proceder== "1"):
        commande.tv_ouvert()
    elif  (proceder == "2"):
        commande.tv_fermer()
    elif  (proceder == "3"):
        commande.volume()

    elif (proceder == "4"):
        nom_des_chaine=input("le nom des chaine avec une','")
        liste_de_chaine = nom_des_chaine.split(',')
        for ajout in liste_de_chaine:
            commande.ajout_chaine (ajout)

    elif  (proceder == "5"):
          print ("nombre de chaine".len(commande))
    elif  (proceder == "6"):
        commande.choix_aleatoire
    elif (proceder == "7"):
        print(commande)
    elif (proceder == "q"):
        print("session terminer")
        break

    else:
        print("geçersiz işlem....")
















