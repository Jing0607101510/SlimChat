# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddGroup_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_For_AddGroup(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 432)
        self.top = QtWidgets.QLabel(Dialog)
        self.top.setGeometry(QtCore.QRect(0, 0, 541, 81))
        self.top.setText("")
        self.top.setPixmap(QtGui.QPixmap("img/top.png"))
        self.top.setObjectName("top")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 541, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(90, 50, 101, 31))
        self.label_3.setObjectName("label_3")
        self.editName = QtWidgets.QLineEdit(self.tab)
        self.editName.setGeometry(QtCore.QRect(200, 40, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.editName.setFont(font)
        self.editName.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.editName.setText("")
        self.editName.setPlaceholderText("请输入群名称")
        self.editName.setClearButtonEnabled(False)
        self.editName.setObjectName("editName")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(90, 130, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lblhead = QtWidgets.QLabel(self.tab)
        self.lblhead.setGeometry(QtCore.QRect(280, 120, 111, 111))
        self.lblhead.setText("")
        self.lblhead.setPixmap(QtGui.QPixmap("img/群众.png"))
        self.lblhead.setScaledContents(True)
        self.lblhead.setObjectName("lblhead")
        self.scanPic = QtWidgets.QPushButton(self.tab)
        self.scanPic.setGeometry(QtCore.QRect(90, 200, 93, 28))
        self.scanPic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scanPic.setFlat(False)
        self.scanPic.setObjectName("scanPic")
        self.btDone = QtWidgets.QPushButton(self.tab)
        self.btDone.setGeometry(QtCore.QRect(160, 280, 251, 41))
        self.btDone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btDone.setDefault(True)
        self.btDone.setFlat(False)
        self.btDone.setObjectName("btDone")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.editId = QtWidgets.QLineEdit(self.tab_2)
        self.editId.setGeometry(QtCore.QRect(190, 70, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.editId.setFont(font)
        self.editId.setPlaceholderText("请输入所要加入的群组账号")
        self.editId.setClearButtonEnabled(False)
        self.editId.setObjectName("editId")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 101, 31))
        self.label_2.setObjectName("label_2")
        self.pbAdd = QtWidgets.QPushButton(self.tab_2)
        self.pbAdd.setGeometry(QtCore.QRect(140, 190, 251, 41))
        self.pbAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbAdd.setDefault(True)
        self.pbAdd.setObjectName("pbAdd")
        self.tabWidget.addTab(self.tab_2, "")
        self.closeBt = QtWidgets.QToolButton(Dialog)
        self.closeBt.setGeometry(QtCore.QRect(510, 0, 31, 41))
        self.closeBt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/blueclose.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBt.setIcon(icon)
        self.closeBt.setCheckable(False)
        self.closeBt.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.closeBt.setAutoRaise(True)
        self.closeBt.setArrowType(QtCore.Qt.NoArrow)
        self.closeBt.setObjectName("closeBt")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setToolTip(_translate("Dialog", "加入群组"))
        self.label_3.setText(_translate("Dialog", "群组名称"))
        self.editName.setToolTip(_translate("Dialog", "请输入新的昵称"))
        self.label_4.setText(_translate("Dialog", "设置头像"))
        self.scanPic.setToolTip(_translate("Dialog", "浏览"))
        self.scanPic.setText(_translate("Dialog", "浏览"))
        self.btDone.setToolTip(_translate("Dialog", "完成"))
        self.btDone.setText(_translate("Dialog", "完成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "新建群组"))
        self.editId.setToolTip(_translate("Dialog", "请输入用户账号"))
        self.label_2.setText(_translate("Dialog", "群组账号"))
        self.pbAdd.setText(_translate("Dialog", "确认"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "加入群组"))
        self.closeBt.setToolTip(_translate("Dialog", "关闭"))

