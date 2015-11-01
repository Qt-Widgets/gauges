# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/estan/Projekt/gauges/gauges/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(False)
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, 20, 20, -1)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.bigFellaLayout = QtWidgets.QVBoxLayout()
        self.bigFellaLayout.setSpacing(0)
        self.bigFellaLayout.setObjectName("bigFellaLayout")
        self.bigFellaLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bigFellaLabel.setFont(font)
        self.bigFellaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bigFellaLabel.setObjectName("bigFellaLabel")
        self.bigFellaLayout.addWidget(self.bigFellaLabel)
        self.bigFellaDial = Gauge(self.centralwidget)
        self.bigFellaDial.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bigFellaDial.sizePolicy().hasHeightForWidth())
        self.bigFellaDial.setSizePolicy(sizePolicy)
        self.bigFellaDial.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bigFellaDial.setMaximum(100)
        self.bigFellaDial.setNotchesVisible(True)
        self.bigFellaDial.setObjectName("bigFellaDial")
        self.bigFellaLayout.addWidget(self.bigFellaDial)
        self.bigFellaSlider = QtWidgets.QSlider(self.centralwidget)
        self.bigFellaSlider.setMaximum(100)
        self.bigFellaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.bigFellaSlider.setObjectName("bigFellaSlider")
        self.bigFellaLayout.addWidget(self.bigFellaSlider)
        self.gridLayout.addLayout(self.bigFellaLayout, 0, 0, 2, 1)
        self.smallBuddyLayout = QtWidgets.QVBoxLayout()
        self.smallBuddyLayout.setObjectName("smallBuddyLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.smallBuddyLayout.addItem(spacerItem)
        self.smallBuddyLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.smallBuddyLabel.setFont(font)
        self.smallBuddyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.smallBuddyLabel.setObjectName("smallBuddyLabel")
        self.smallBuddyLayout.addWidget(self.smallBuddyLabel)
        self.smallBuddyDial = Gauge(self.centralwidget)
        self.smallBuddyDial.setEnabled(False)
        self.smallBuddyDial.setFocusPolicy(QtCore.Qt.NoFocus)
        self.smallBuddyDial.setMaximum(100)
        self.smallBuddyDial.setNotchesVisible(True)
        self.smallBuddyDial.setObjectName("smallBuddyDial")
        self.smallBuddyLayout.addWidget(self.smallBuddyDial)
        self.gridLayout.addLayout(self.smallBuddyLayout, 0, 1, 1, 1)
        self.tinyLadLayout = QtWidgets.QVBoxLayout()
        self.tinyLadLayout.setObjectName("tinyLadLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tinyLadLayout.addItem(spacerItem1)
        self.tinyLadLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tinyLadLabel.setFont(font)
        self.tinyLadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tinyLadLabel.setObjectName("tinyLadLabel")
        self.tinyLadLayout.addWidget(self.tinyLadLabel)
        self.tinyLadDial = Gauge(self.centralwidget)
        self.tinyLadDial.setEnabled(False)
        self.tinyLadDial.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tinyLadDial.setMaximum(100)
        self.tinyLadDial.setNotchesVisible(True)
        self.tinyLadDial.setObjectName("tinyLadDial")
        self.tinyLadLayout.addWidget(self.tinyLadDial)
        self.gridLayout.addLayout(self.tinyLadLayout, 0, 2, 1, 1)
        self.littlePalLayout = QtWidgets.QVBoxLayout()
        self.littlePalLayout.setObjectName("littlePalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.littlePalLayout.addItem(spacerItem2)
        self.littlePalLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.littlePalLabel.setFont(font)
        self.littlePalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.littlePalLabel.setObjectName("littlePalLabel")
        self.littlePalLayout.addWidget(self.littlePalLabel)
        self.littlePalDial = Gauge(self.centralwidget)
        self.littlePalDial.setEnabled(False)
        self.littlePalDial.setFocusPolicy(QtCore.Qt.NoFocus)
        self.littlePalDial.setMaximum(100)
        self.littlePalDial.setNotchesVisible(True)
        self.littlePalDial.setObjectName("littlePalDial")
        self.littlePalLayout.addWidget(self.littlePalDial)
        self.gridLayout.addLayout(self.littlePalLayout, 0, 3, 1, 1)
        self.slidersLayout = QtWidgets.QHBoxLayout()
        self.slidersLayout.setSpacing(0)
        self.slidersLayout.setObjectName("slidersLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.slidersLayout.addItem(spacerItem3)
        self.smallBuddySlider = QtWidgets.QSlider(self.centralwidget)
        self.smallBuddySlider.setMaximum(100)
        self.smallBuddySlider.setOrientation(QtCore.Qt.Vertical)
        self.smallBuddySlider.setObjectName("smallBuddySlider")
        self.slidersLayout.addWidget(self.smallBuddySlider)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.slidersLayout.addItem(spacerItem4)
        self.tinyLadSlider = QtWidgets.QSlider(self.centralwidget)
        self.tinyLadSlider.setMaximum(100)
        self.tinyLadSlider.setOrientation(QtCore.Qt.Vertical)
        self.tinyLadSlider.setObjectName("tinyLadSlider")
        self.slidersLayout.addWidget(self.tinyLadSlider)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.slidersLayout.addItem(spacerItem5)
        self.littlePalSlider = QtWidgets.QSlider(self.centralwidget)
        self.littlePalSlider.setMaximum(100)
        self.littlePalSlider.setOrientation(QtCore.Qt.Vertical)
        self.littlePalSlider.setObjectName("littlePalSlider")
        self.slidersLayout.addWidget(self.littlePalSlider)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.slidersLayout.addItem(spacerItem6)
        self.slidersLayout.setStretch(2, 1)
        self.slidersLayout.setStretch(4, 1)
        self.gridLayout.addLayout(self.slidersLayout, 1, 1, 1, 3)
        self.channelLayout = QtWidgets.QHBoxLayout()
        self.channelLayout.setSpacing(6)
        self.channelLayout.setObjectName("channelLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.channelLayout.addItem(spacerItem7)
        self.channelLabel = QtWidgets.QLabel(self.centralwidget)
        self.channelLabel.setObjectName("channelLabel")
        self.channelLayout.addWidget(self.channelLabel)
        self.channelEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.channelEdit.setObjectName("channelEdit")
        self.channelLayout.addWidget(self.channelEdit)
        self.channelSwitchButton = QtWidgets.QPushButton(self.centralwidget)
        self.channelSwitchButton.setEnabled(False)
        self.channelSwitchButton.setObjectName("channelSwitchButton")
        self.channelLayout.addWidget(self.channelSwitchButton)
        self.channelCancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.channelCancelButton.setEnabled(False)
        self.channelCancelButton.setObjectName("channelCancelButton")
        self.channelLayout.addWidget(self.channelCancelButton)
        self.gridLayout.addLayout(self.channelLayout, 2, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.channelLabel.setBuddy(self.channelEdit)

        self.retranslateUi(MainWindow)
        self.channelEdit.returnPressed.connect(self.channelSwitchButton.animateClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.channelEdit, self.channelSwitchButton)
        MainWindow.setTabOrder(self.channelSwitchButton, self.channelCancelButton)
        MainWindow.setTabOrder(self.channelCancelButton, self.bigFellaSlider)
        MainWindow.setTabOrder(self.bigFellaSlider, self.smallBuddySlider)
        MainWindow.setTabOrder(self.smallBuddySlider, self.tinyLadSlider)
        MainWindow.setTabOrder(self.tinyLadSlider, self.littlePalSlider)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gauges Demo"))
        self.bigFellaLabel.setText(_translate("MainWindow", "Big Fella"))
        self.bigFellaSlider.setToolTip(_translate("MainWindow", "Adjust the Big Fella value."))
        self.smallBuddyLabel.setText(_translate("MainWindow", "Small Buddy"))
        self.tinyLadLabel.setText(_translate("MainWindow", "Tiny Lad"))
        self.littlePalLabel.setText(_translate("MainWindow", "Little Pal"))
        self.smallBuddySlider.setToolTip(_translate("MainWindow", "Adjust the Small Buddy value."))
        self.tinyLadSlider.setToolTip(_translate("MainWindow", "Adjust the Tiny Lad value."))
        self.littlePalSlider.setToolTip(_translate("MainWindow", "Adjust the Little Pal value."))
        self.channelLabel.setToolTip(_translate("MainWindow", "Enter a 6-digit controller channel."))
        self.channelLabel.setText(_translate("MainWindow", "Contro&ller Channel:"))
        self.channelEdit.setToolTip(_translate("MainWindow", "Enter a 6-digit controller channel."))
        self.channelSwitchButton.setToolTip(_translate("MainWindow", "Switch to the entered channel."))
        self.channelSwitchButton.setText(_translate("MainWindow", "Switch"))
        self.channelCancelButton.setToolTip(_translate("MainWindow", "Cancel controller channel editing."))
        self.channelCancelButton.setText(_translate("MainWindow", "Cancel"))

from gauges.gauges_qt import Gauge
