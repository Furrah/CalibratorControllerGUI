# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controllerUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 2, 0, 1, 1)
        self.graphicsView_2_Offset = PlotWidget(self.centralwidget)
        self.graphicsView_2_Offset.setObjectName("graphicsView_2_Offset")
        self.gridLayout_3.addWidget(self.graphicsView_2_Offset, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Pulse_Delay_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Pulse_Delay_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Pulse_Delay_Button.setObjectName("Pulse_Delay_Button")
        self.gridLayout.addWidget(self.Pulse_Delay_Button, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(200, 20))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.V4_Label = QtWidgets.QLabel(self.centralwidget)
        self.V4_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.V4_Label.setObjectName("V4_Label")
        self.gridLayout.addWidget(self.V4_Label, 8, 1, 1, 1)
        self.Pulse_Length_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Pulse_Length_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Pulse_Length_lineEdit.setObjectName("Pulse_Length_lineEdit")
        self.gridLayout.addWidget(self.Pulse_Length_lineEdit, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(200, 20))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.V3_Label = QtWidgets.QLabel(self.centralwidget)
        self.V3_Label.setMaximumSize(QtCore.QSize(200, 20))
        self.V3_Label.setObjectName("V3_Label")
        self.gridLayout.addWidget(self.V3_Label, 8, 0, 1, 1)
        self.V2_Label = QtWidgets.QLabel(self.centralwidget)
        self.V2_Label.setMaximumSize(QtCore.QSize(100, 20))
        self.V2_Label.setObjectName("V2_Label")
        self.gridLayout.addWidget(self.V2_Label, 7, 1, 1, 1)
        self.Temperature_label = QtWidgets.QLabel(self.centralwidget)
        self.Temperature_label.setMaximumSize(QtCore.QSize(200, 20))
        self.Temperature_label.setObjectName("Temperature_label")
        self.gridLayout.addWidget(self.Temperature_label, 6, 0, 1, 1)
        self.Pulse_Length_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pulse_Length_Button.sizePolicy().hasHeightForWidth())
        self.Pulse_Length_Button.setSizePolicy(sizePolicy)
        self.Pulse_Length_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Pulse_Length_Button.setObjectName("Pulse_Length_Button")
        self.gridLayout.addWidget(self.Pulse_Length_Button, 3, 2, 1, 1)
        self.checkBox_DisableSwitching = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_DisableSwitching.setMinimumSize(QtCore.QSize(220, 0))
        self.checkBox_DisableSwitching.setMaximumSize(QtCore.QSize(300, 16777215))
        self.checkBox_DisableSwitching.setObjectName("checkBox_DisableSwitching")
        self.gridLayout.addWidget(self.checkBox_DisableSwitching, 2, 0, 1, 1)
        self.V1_Label = QtWidgets.QLabel(self.centralwidget)
        self.V1_Label.setMaximumSize(QtCore.QSize(200, 20))
        self.V1_Label.setObjectName("V1_Label")
        self.gridLayout.addWidget(self.V1_Label, 7, 0, 1, 1)
        self.Pulse_Delay_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Pulse_Delay_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Pulse_Delay_lineEdit.setObjectName("Pulse_Delay_lineEdit")
        self.gridLayout.addWidget(self.Pulse_Delay_lineEdit, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(200, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.checkBox_EnableCircuitOne = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_EnableCircuitOne.sizePolicy().hasHeightForWidth())
        self.checkBox_EnableCircuitOne.setSizePolicy(sizePolicy)
        self.checkBox_EnableCircuitOne.setMaximumSize(QtCore.QSize(200, 16777215))
        self.checkBox_EnableCircuitOne.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_EnableCircuitOne.setAutoFillBackground(False)
        self.checkBox_EnableCircuitOne.setObjectName("checkBox_EnableCircuitOne")
        self.gridLayout.addWidget(self.checkBox_EnableCircuitOne, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 4, 1, 1)
        self.label_DAC_Value = QtWidgets.QLabel(self.centralwidget)
        self.label_DAC_Value.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_DAC_Value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DAC_Value.setObjectName("label_DAC_Value")
        self.gridLayout.addWidget(self.label_DAC_Value, 6, 2, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 5, 1, 1, 3)
        self.checkBox_EnableCircuitTwo = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_EnableCircuitTwo.setObjectName("checkBox_EnableCircuitTwo")
        self.gridLayout.addWidget(self.checkBox_EnableCircuitTwo, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.pushButton_ADC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ADC.setObjectName("pushButton_ADC")
        self.gridLayout_3.addWidget(self.pushButton_ADC, 1, 0, 1, 1)
        self.label_offset_average = QtWidgets.QLabel(self.centralwidget)
        self.label_offset_average.setAlignment(QtCore.Qt.AlignCenter)
        self.label_offset_average.setObjectName("label_offset_average")
        self.gridLayout_3.addWidget(self.label_offset_average, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Pulse_Delay_Button.setText(_translate("MainWindow", "Send"))
        self.label_7.setText(_translate("MainWindow", "Pulse Delay (uS)"))
        self.V4_Label.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "Pulse Length (uS)"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset I2C"))
        self.V3_Label.setText(_translate("MainWindow", "TextLabel"))
        self.V2_Label.setText(_translate("MainWindow", "TextLabel"))
        self.Temperature_label.setText(_translate("MainWindow", "TextLabel"))
        self.Pulse_Length_Button.setText(_translate("MainWindow", "Send"))
        self.checkBox_DisableSwitching.setText(_translate("MainWindow", "Disable Differential Switching"))
        self.V1_Label.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "DAC"))
        self.checkBox_EnableCircuitOne.setText(_translate("MainWindow", "Enable 1"))
        self.label_DAC_Value.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_EnableCircuitTwo.setText(_translate("MainWindow", "Enable 2"))
        self.pushButton_ADC.setText(_translate("MainWindow", "ADC Acquire"))
        self.label_offset_average.setText(_translate("MainWindow", "TextLabel"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
