import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("İNDEKS")
        self.setGeometry(200,200,1200,300)
        self.initUI()  
        self.setWindowIcon(QIcon('indir.png'))

    def initUI(self):
        self.lbl_Bilgilendirme = QtWidgets.QLabel(self)
        self.lbl_Bilgilendirme.setText("Analiz: ")
        self.lbl_Bilgilendirme.move(250,170)
        

        self.txt_Bilgilendirme = QtWidgets.QLineEdit(self)
        self.txt_Bilgilendirme.move(300,170)
        self.txt_Bilgilendirme.resize(1000,50)
        
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız: ")
        self.lbl_name.move(50,30)
        
        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50,70)

        self.weight = QtWidgets.QLabel(self)
        self.weight.setText("Kilo: ")
        self.weight.move(250,30)

        self.tall = QtWidgets.QLabel(self)
        self.tall.setText("Boy:")
        self.tall.move(250,70)

        self.txt_name =  QtWidgets.QLineEdit(self)
        self.txt_name.move(100, 30)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(100, 70)

        self.txt_weight = QtWidgets.QLineEdit(self)
        self.txt_weight.move(300,30)
        self.txt_tall = QtWidgets.QLineEdit(self)
        self.txt_tall.move(300,70)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText(" BMI: ")
        self.lbl_sonuc.move(250,130)

        self.txt_sonuc = QtWidgets.QLineEdit(self)
        self.txt_sonuc.move(300,130)

        self.hesapla = QtWidgets.QPushButton(self)
        self.hesapla.setText("Hesapla")
        self.hesapla.move(50,130)
        self.hesapla.clicked.connect(self.hesaplama)


        self.analız1 = QtWidgets.QPushButton(self)
        self.analız1.setText("Analiz")
        self.analız1.move(50,170)
        self.analız1.clicked.connect(self.hesaplama)
        

    def hesaplama(self):
        sender = self.sender()
        result2 = 0

        if sender.text() == 'Hesapla' :
            result1 = (float(self.txt_tall.text())) *  (float(self.txt_tall.text()))
            result2 = ((int(self.txt_weight.text()))) / result1
            self.txt_sonuc.setText(str(result2))
        elif sender.text() == "Analiz":
            result1 = (float(self.txt_tall.text())) *  (float(self.txt_tall.text()))
            result2 = ((int(self.txt_weight.text()))) / result1
            isim = (str(self.txt_name.text())) + (str(self.txt_surname.text()))
            if result2 <= 18.4:
                self.txt_Bilgilendirme.setText("Sayın " + str(isim) + " Zayıf. Kişinin boyuna oranla ağırlığının yetersiz olduğunu ifade eden bu değer ile karşılaşılması durumunda kişinin diyetisyen eşliğinde sağlıklı bir şekilde kilo alması önerilir.")
            elif 18.5<= result2 <= 24.9:
                self.txt_Bilgilendirme.setText("Sayın " + str(isim) + " Normal. Bu değer aralığı kişinin ideal kiloda olduğunu gösterir. Bu değere sahip olan kişilerin düzenli, dengeli ve sağlıklı beslenmeye devam etmeleri önerilir.")
            elif 25<= result2 <= 29.9:
                self.txt_Bilgilendirme.setText("Sayın " + str(isim) + " Fazla Kilolu. Kişinin boyuna oranla kilosunun fazla olduğunu gösteren bu değer aralığında kişinin uygun diyet ile fazla kilolarından kurtulması önerilir.")
            elif 30<= result2 <= 34.9:
                self.txt_Bilgilendirme.setText("Sayın " + str(isim) + " Şişman. Birinci derece obez kategorisinde değerlendiren değer aralığında, kişinin kilosunun sağlık açısından risk oluşturabilecek düzeyde olduğu anlaşılır. Bu kişilerin diyetisyen yardımıyla kilo vermesi önerilir.")
            elif 35<= result2 <= 44.9:
                self.txt_Bilgilendirme.setText("Sayın " + str(isim) + " Şişman. İkinci derece obez olarak tanımlanan bu değerlere sahip olan kişilerde kalp ve damar hastalıkları bakımından risk artar. Kişinin kilo vermek için diyetisyene başvurması önerilir.")
            elif result2 >= 45:
                self.txt_Bilgilendirme.setText("Sayın " + str(isim) + " Aşırı Şişman. Üçüncü derece obez kategorisinde olan bu kişilerde hastalık gelişme riski çok yüksektir. Hekim ve diyetisyen eşliğinde kilo verilmesi önerilir.")
            else:
                self.txt_Bilgilendirme.setText("LÜTFEN UYGUN İFADELER GİRİNİZ")

        
    

        


        

        



def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())


app()



