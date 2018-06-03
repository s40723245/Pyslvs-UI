# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/io/output_option.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 641)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Solvespace.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.path_label = QtWidgets.QLabel(Dialog)
        self.path_label.setObjectName("path_label")
        self.horizontalLayout_2.addWidget(self.path_label)
        self.path_edit = QtWidgets.QLineEdit(Dialog)
        self.path_edit.setObjectName("path_edit")
        self.horizontalLayout_2.addWidget(self.path_edit)
        self.choosedir_button = QtWidgets.QToolButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/loadfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.choosedir_button.setIcon(icon1)
        self.choosedir_button.setObjectName("choosedir_button")
        self.horizontalLayout_2.addWidget(self.choosedir_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.newfolder_option = QtWidgets.QCheckBox(Dialog)
        self.newfolder_option.setChecked(True)
        self.newfolder_option.setObjectName("newfolder_option")
        self.verticalLayout_4.addWidget(self.newfolder_option)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filename_label = QtWidgets.QLabel(Dialog)
        self.filename_label.setObjectName("filename_label")
        self.horizontalLayout_3.addWidget(self.filename_label)
        self.filename_edit = QtWidgets.QLineEdit(Dialog)
        self.filename_edit.setObjectName("filename_edit")
        self.horizontalLayout_3.addWidget(self.filename_edit)
        self.filename_suffix_label = QtWidgets.QLabel(Dialog)
        self.filename_suffix_label.setObjectName("filename_suffix_label")
        self.horizontalLayout_3.addWidget(self.filename_suffix_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.output_group = QtWidgets.QGroupBox(Dialog)
        self.output_group.setObjectName("output_group")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.output_group)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.assembly_radio = QtWidgets.QRadioButton(self.output_group)
        self.assembly_radio.setChecked(True)
        self.assembly_radio.setObjectName("assembly_radio")
        self.verticalLayout_5.addWidget(self.assembly_radio)
        self.assembly_group = QtWidgets.QWidget(self.output_group)
        self.assembly_group.setObjectName("assembly_group")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.assembly_group)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.assembly_label = QtWidgets.QLabel(self.assembly_group)
        self.assembly_label.setWordWrap(True)
        self.assembly_label.setObjectName("assembly_label")
        self.verticalLayout_3.addWidget(self.assembly_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.link_radius_label = QtWidgets.QLabel(self.assembly_group)
        self.link_radius_label.setObjectName("link_radius_label")
        self.horizontalLayout_5.addWidget(self.link_radius_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.link_radius = QtWidgets.QDoubleSpinBox(self.assembly_group)
        self.link_radius.setMinimum(0.01)
        self.link_radius.setProperty("value", 10.0)
        self.link_radius.setObjectName("link_radius")
        self.horizontalLayout_5.addWidget(self.link_radius)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.assembly_group)
        self.frame_radio = QtWidgets.QRadioButton(self.output_group)
        self.frame_radio.setObjectName("frame_radio")
        self.verticalLayout_5.addWidget(self.frame_radio)
        self.frame_group = QtWidgets.QWidget(self.output_group)
        self.frame_group.setEnabled(False)
        self.frame_group.setObjectName("frame_group")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_group)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_label = QtWidgets.QLabel(self.frame_group)
        self.frame_label.setWordWrap(True)
        self.frame_label.setObjectName("frame_label")
        self.verticalLayout.addWidget(self.frame_label)
        self.verticalLayout_5.addWidget(self.frame_group)
        self.verticalLayout_4.addWidget(self.output_group)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.overwrite_radio = QtWidgets.QRadioButton(self.groupBox)
        self.overwrite_radio.setChecked(True)
        self.overwrite_radio.setObjectName("overwrite_radio")
        self.verticalLayout_2.addWidget(self.overwrite_radio)
        self.warn_radio = QtWidgets.QRadioButton(self.groupBox)
        self.warn_radio.setObjectName("warn_radio")
        self.verticalLayout_2.addWidget(self.warn_radio)
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 158, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.assembly_radio.toggled['bool'].connect(self.assembly_group.setEnabled)
        self.frame_radio.toggled['bool'].connect(self.frame_group.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.path_label.setText(_translate("Dialog", "Directory:"))
        self.choosedir_button.setText(_translate("Dialog", "..."))
        self.newfolder_option.setText(_translate("Dialog", "Create a new folder with workbook name"))
        self.filename_label.setText(_translate("Dialog", "Main file name:"))
        self.filename_suffix_label.setText(_translate("Dialog", ".slvs"))
        self.output_group.setTitle(_translate("Dialog", "Output types"))
        self.assembly_radio.setText(_translate("Dialog", "Assembly"))
        self.assembly_label.setText(_translate("Dialog", "The part sketchs file will be generated automatically with target directory."))
        self.link_radius_label.setText(_translate("Dialog", "Fillet radius:"))
        self.frame_radio.setText(_translate("Dialog", "Only wire frame"))
        self.frame_label.setText(_translate("Dialog", "There is only sketch file of main mechanism will be generated."))
        self.groupBox.setTitle(_translate("Dialog", "Write mode"))
        self.overwrite_radio.setText(_translate("Dialog", "Always overwrite"))
        self.warn_radio.setText(_translate("Dialog", "Warning me then back to this dialog"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
