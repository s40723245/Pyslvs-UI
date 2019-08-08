# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/entities/edit_point.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from core.QtModules import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(354, 528)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/bearing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.name_box = QtWidgets.QComboBox(Dialog)
        self.name_box.setObjectName("name_box")
        self.verticalLayout.addWidget(self.name_box)
        self.color_label = QtWidgets.QLabel(Dialog)
        self.color_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.color_label.setObjectName("color_label")
        self.verticalLayout.addWidget(self.color_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.color_box = QtWidgets.QComboBox(Dialog)
        self.color_box.setObjectName("color_box")
        self.horizontalLayout_2.addWidget(self.color_box)
        self.color_pick_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_pick_button.sizePolicy().hasHeightForWidth())
        self.color_pick_button.setSizePolicy(sizePolicy)
        self.color_pick_button.setObjectName("color_pick_button")
        self.horizontalLayout_2.addWidget(self.color_pick_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.x_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.x_box.setDecimals(4)
        self.x_box.setMinimum(-999999.0)
        self.x_box.setMaximum(999999.0)
        self.x_box.setObjectName("x_box")
        self.gridLayout.addWidget(self.x_box, 1, 0, 1, 1)
        self.y_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.y_box.setDecimals(4)
        self.y_box.setMinimum(-999999.0)
        self.y_box.setMaximum(999999.0)
        self.y_box.setObjectName("y_box")
        self.gridLayout.addWidget(self.y_box, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.type_label = QtWidgets.QLabel(Dialog)
        self.type_label.setObjectName("type_label")
        self.verticalLayout.addWidget(self.type_label)
        self.type_box = QtWidgets.QComboBox(Dialog)
        self.type_box.setObjectName("type_box")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.verticalLayout.addWidget(self.type_box)
        self.angle_box_2 = QtWidgets.QLabel(Dialog)
        self.angle_box_2.setObjectName("angle_box_2")
        self.verticalLayout.addWidget(self.angle_box_2)
        self.angle_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.angle_box.setEnabled(False)
        self.angle_box.setMaximum(180.0)
        self.angle_box.setObjectName("angle_box")
        self.verticalLayout.addWidget(self.angle_box)
        self.links_label = QtWidgets.QLabel(Dialog)
        self.links_label.setObjectName("links_label")
        self.verticalLayout.addWidget(self.links_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.noSelected = QtWidgets.QListWidget(Dialog)
        self.noSelected.setDragEnabled(True)
        self.noSelected.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.noSelected.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.noSelected.setObjectName("noSelected")
        self.horizontalLayout.addWidget(self.noSelected)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.selected = QtWidgets.QListWidget(Dialog)
        self.selected.setDragEnabled(True)
        self.selected.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.selected.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.selected.setObjectName("selected")
        self.horizontalLayout.addWidget(self.selected)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setOrientation(QtCore.Qt.Vertical)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout_2.addWidget(self.button_box)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Point"))
        self.name_label.setText(_translate("Dialog", "Point Number"))
        self.color_label.setText(_translate("Dialog", "Color"))
        self.label.setText(_translate("Dialog", "x coordinate"))
        self.label_2.setText(_translate("Dialog", "y coordinate"))
        self.type_label.setText(_translate("Dialog", "Type:"))
        self.type_box.setItemText(0, _translate("Dialog", "R (pin)"))
        self.type_box.setItemText(1, _translate("Dialog", "P (slider block)"))
        self.type_box.setItemText(2, _translate("Dialog", "RP (pin in slot)"))
        self.angle_box_2.setText(_translate("Dialog", "Angle (Slider):"))
        self.links_label.setText(_translate("Dialog", "Links:"))
        self.label_4.setText(_translate("Dialog", ">>"))
import icons_rc
