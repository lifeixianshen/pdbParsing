# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Apr 07 20:25:04 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(645, 491)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 491))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.Ln_Filename = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Ln_Filename.setText(_fromUtf8(""))
        self.Ln_Filename.setObjectName(_fromUtf8("Ln_Filename"))
        self.horizontalLayout.addWidget(self.Ln_Filename)
        self.Btn_Browser = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Btn_Browser.setObjectName(_fromUtf8("Btn_Browser"))
        self.horizontalLayout.addWidget(self.Btn_Browser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.Chk_State = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.Chk_State.setObjectName(_fromUtf8("Chk_State"))
        self.horizontalLayout_2.addWidget(self.Chk_State)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Btn_Submit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Btn_Submit.setObjectName(_fromUtf8("Btn_Submit"))
        self.horizontalLayout_2.addWidget(self.Btn_Submit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.Tbl_GPCR = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.Tbl_GPCR.setObjectName(_fromUtf8("Tbl_GPCR"))
        self.Tbl_GPCR.setColumnCount(15)
        self.Tbl_GPCR.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.Tbl_GPCR.setHorizontalHeaderItem(14, item)
        self.verticalLayout.addWidget(self.Tbl_GPCR)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Btn_Browser, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.browsefile)
        QtCore.QObject.connect(self.Btn_Submit, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.submitdata)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "PDB file name", None))
        self.Btn_Browser.setText(_translate("Dialog", "Browser", None))
        self.label.setText(_translate("Dialog", "Active State", None))
        self.Chk_State.setText(_translate("Dialog", "Yes", None))
        self.Btn_Submit.setText(_translate("Dialog", "Submit to database", None))
        self.label_2.setText(_translate("Dialog", "GPCR structure database", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "PDB ID", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Structure Name", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Jounal", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Author", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Published date", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Engineered", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Mutation", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Organism", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Experimental method", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Resolution", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "R Value", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "B Value", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "State", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(13)
        item.setText(_translate("Dialog", "Software used", None))
        item = self.Tbl_GPCR.horizontalHeaderItem(14)
        item.setText(_translate("Dialog", "Biomolecule number", None))

