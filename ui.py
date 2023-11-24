from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 420)
        self.create_circle = QtWidgets.QPushButton(Form)
        self.create_circle.setGeometry(QtCore.QRect(140, 20, 120, 70))
        self.create_circle.setObjectName("create_circle")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.create_circle.setText(
            _translate(
                "Form", "Создать окружность"
                )
            )
