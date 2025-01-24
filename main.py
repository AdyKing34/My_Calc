from PyQt6 import QtCore, QtWidgets
import yaml

# Defining the User Interface (UI) class for the calculator application
class Ui_Form(object):
    # Method to set up the user interface for the form
    def setupUi(self, Form):
        # Setting up the main window of the application
        Form.setObjectName("Form")
        Form.resize(379, 552)
        Form.setStyleSheet("background-color:black\n"
"")

        # Creating buttons for the calculator, setting their styles, and placing them in the correct locations
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 390, 75, 61))
        self.pushButton.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 390, 75, 61))
        self.pushButton_2.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 310, 75, 61))
        self.pushButton_4.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 230, 75, 61))
        self.pushButton_7.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 310, 75, 61))
        self.pushButton_6.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 390, 75, 61))
        self.pushButton_3.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 230, 75, 61))
        self.pushButton_8.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 310, 75, 61))
        self.pushButton_5.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 230, 75, 61))
        self.pushButton_9.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_10.setGeometry(QtCore.QRect(110, 470, 75, 61))
        self.pushButton_10.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 470, 75, 61))
        self.pushButton_11.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 390, 75, 141))
        self.pushButton_12.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_13.setGeometry(QtCore.QRect(290, 230, 75, 141))
        self.pushButton_13.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_14.setGeometry(QtCore.QRect(290, 150, 75, 61))
        self.pushButton_14.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_15.setGeometry(QtCore.QRect(200, 150, 75, 61))
        self.pushButton_15.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_16.setGeometry(QtCore.QRect(110, 150, 75, 61))
        self.pushButton_16.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_17.setGeometry(QtCore.QRect(20, 150, 75, 61))
        self.pushButton_17.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_18.setGeometry(QtCore.QRect(200, 470, 75, 61))
        self.pushButton_18.setStyleSheet("background-color:rgb(25,25,25);\n"
"color:white;\n"
"border-radius: 5px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.pushButton_18.setObjectName("pushButton_18")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 341, 111))
        self.label.setStyleSheet("color:white;\n"
"font: 28pt \"Bahnschrift SemiLight Condensed\";")
        self.label.setObjectName("label")

        # Connecting buttons to their respective functions
        self.pushButton.clicked.connect(self.num1)
        self.pushButton_2.clicked.connect(self.num2)
        self.pushButton_3.clicked.connect(self.num3)
        self.pushButton_4.clicked.connect(self.num4)
        self.pushButton_5.clicked.connect(self.num5)
        self.pushButton_6.clicked.connect(self.num6)
        self.pushButton_7.clicked.connect(self.num7)
        self.pushButton_8.clicked.connect(self.num8)
        self.pushButton_9.clicked.connect(self.num9)
        self.pushButton_10.clicked.connect(self.num0)
        self.pushButton_12.clicked.connect(self.evaluate)
        self.pushButton_13.clicked.connect(self.add)
        self.pushButton_14.clicked.connect(self.subtract)
        self.pushButton_15.clicked.connect(self.multiply)
        self.pushButton_16.clicked.connect(self.divide)
        self.pushButton_17.clicked.connect(self.back)
        self.pushButton_18.clicked.connect(self.AC)
        self.pushButton_11.clicked.connect(self.point)

        # Method to handle setting text on UI elements
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        # Setting labels and button text dynamically for localization
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_10.setText(_translate("Form", "0"))
        self.pushButton_11.setText(_translate("Form", "."))
        self.pushButton_12.setText(_translate("Form", "="))
        self.pushButton_13.setText(_translate("Form", "+"))
        self.pushButton_14.setText(_translate("Form", "-"))
        self.pushButton_15.setText(_translate("Form", "*"))
        self.pushButton_16.setText(_translate("Form", "/"))
        self.pushButton_17.setText(_translate("Form", "Back"))
        self.pushButton_18.setText(_translate("Form", "AC"))
        self.label.setText(_translate("Form", ""))

# Define functions to append
    def num1(self):
        number = self.label.text()
        self.label.setText(number + "1")

    def num2(self):
        number = self.label.text()
        self.label.setText(number + "2")

    def num3(self):
        number = self.label.text()
        self.label.setText(number + "3")

    def num4(self):
        number = self.label.text()
        self.label.setText(number + "4")

    def num5(self):
        number = self.label.text()
        self.label.setText(number + "5")

    def num6(self):
        number = self.label.text()
        self.label.setText(number + "6")

    def num7(self):
        number = self.label.text()
        self.label.setText(number + "7")

    def num8(self):
        number = self.label.text()
        self.label.setText(number + "8")

    def num9(self):
        number = self.label.text()
        self.label.setText(number + "9")

    def num0(self):
        number = self.label.text()
        self.label.setText(number + "0")

    def evaluate(self):
        number = self.label.text()
        try:
            number = eval(number)
            self.label.setText(str(number))
        except Exception as e:
            self.label.setText("Error")

    def add(self):
        number = self.label.text()
        self.label.setText(number + "+")

    def subtract(self):
        number = self.label.text()
        self.label.setText(number + "-")

    def multiply(self):
        number = self.label.text()
        self.label.setText(number + "*")

    def divide(self):
        number = self.label.text()
        self.label.setText(number + "/")

    def back(self):
        number = self.label.text()
        number = number[1:]
        self.label.setText(number)

    def AC(self):
        self.label.setText("")

    def point(self):
        number = self.label.text()
        self.label.setText(number + ".")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
