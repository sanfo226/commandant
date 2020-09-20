import time
class bilgisayar():
    def __init__(self,isim,marka,model,özellik,ekran):
        self.isim = isim
        self.marka = marka
        self.model = model
        self.özellik = özellik
        self.ekran = ekran


    def isimler(self):
         self.isim=["hp","toshiba,samsung,dell,monster,"]
    def modeller(self):
         self.model=["6570b","450a","a345","5890c","4536d"]
    def markalar(self):
        self.marka=["probook","notebook","gaming","work","child"]
    def özellikler(self):
        self.özellik=["1tb","500gb","2tb","500gb","600gb"]
    def ekranlar(self):
         self.ekran= [2345,5467,2345,5787,3896]

    def str(self):
        return "bilgisayarın ismi: {}\nbilgisayarın markası: {}\nbilgisayarın model: {}\nBilgisayarın özellikleri: {}\nBilgisayarın ekranı: {}".format(
            self.isim, self.marka, self.model, self.özellik, self.ekran)


laptop = bilgisayar()

print("""
1.isim
        
2.marka
        
3.model
        
4.özellik
        
5.ekran

çıkmak için "0" basınız
""")

while True:
    işlem = input("istediğiniz numarayı seçiniz")
    if(işlem == 1):
        bilgisayar.isim

    elif (işlem == 2):
        bilgisayar.marka
    elif (işlem == 3):
        bilgisayar.model
    elif (işlem == 4):
        bilgisayar.ekran
    elif (işlem == 5):
        bilgisayar.özellik
    elif (işlem == 0):
        print("çıkış yaptınız....")
        işlem.sleep(3)
    else:
        print("geçersiz işlem")










