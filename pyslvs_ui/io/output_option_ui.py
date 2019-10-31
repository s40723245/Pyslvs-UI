# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/io/output_option.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 663)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.main_layout = QtWidgets.QVBoxLayout(Dialog)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.path_label = QtWidgets.QLabel(Dialog)
        self.path_label.setObjectName("path_label")
        self.horizontalLayout_2.addWidget(self.path_label)
        self.path_edit = QtWidgets.QLineEdit(Dialog)
        self.path_edit.setObjectName("path_edit")
        self.horizontalLayout_2.addWidget(self.path_edit)
        self.choose_dir_button = QtWidgets.QToolButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/loadfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.choose_dir_button.setIcon(icon)
        self.choose_dir_button.setObjectName("choose_dir_button")
        self.horizontalLayout_2.addWidget(self.choose_dir_button)
        self.main_layout.addLayout(self.horizontalLayout_2)
        self.newfolder_option = QtWidgets.QCheckBox(Dialog)
        self.newfolder_option.setChecked(True)
        self.newfolder_option.setObjectName("newfolder_option")
        self.main_layout.addWidget(self.newfolder_option)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filename_label = QtWidgets.QLabel(Dialog)
        self.filename_label.setObjectName("filename_label")
        self.horizontalLayout_3.addWidget(self.filename_label)
        self.filename_edit = QtWidgets.QLineEdit(Dialog)
        self.filename_edit.setClearButtonEnabled(True)
        self.filename_edit.setObjectName("filename_edit")
        self.horizontalLayout_3.addWidget(self.filename_edit)
        self.filename_suffix_label = QtWidgets.QLabel(Dialog)
        self.filename_suffix_label.setObjectName("filename_suffix_label")
        self.horizontalLayout_3.addWidget(self.filename_suffix_label)
        self.main_layout.addLayout(self.horizontalLayout_3)
        self.output_group = QtWidgets.QGroupBox(Dialog)
        self.output_group.setObjectName("output_group")
        self.output_layout = QtWidgets.QVBoxLayout(self.output_group)
        self.output_layout.setObjectName("output_layout")
        self.assembly_radio = QtWidgets.QRadioButton(self.output_group)
        self.assembly_radio.setChecked(True)
        self.assembly_radio.setObjectName("assembly_radio")
        self.output_layout.addWidget(self.assembly_radio)
        self.assembly_group = QtWidgets.QWidget(self.output_group)
        self.assembly_group.setObjectName("assembly_group")
        self.assembly_layout = QtWidgets.QVBoxLayout(self.assembly_group)
        self.assembly_layout.setObjectName("assembly_layout")
        self.assembly_label = QtWidgets.QLabel(self.assembly_group)
        self.assembly_label.setWordWrap(True)
        self.assembly_label.setObjectName("assembly_label")
        self.assembly_layout.addWidget(self.assembly_label)
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
        self.assembly_layout.addLayout(self.horizontalLayout_5)
        self.output_layout.addWidget(self.assembly_group)
        self.frame_radio = QtWidgets.QRadioButton(self.output_group)
        self.frame_radio.setObjectName("frame_radio")
        self.output_layout.addWidget(self.frame_radio)
        self.frame_group = QtWidgets.QWidget(self.output_group)
        self.frame_group.setEnabled(False)
        self.frame_group.setObjectName("frame_group")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_group)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_label = QtWidgets.QLabel(self.frame_group)
        self.frame_label.setWordWrap(True)
        self.frame_label.setObjectName("frame_label")
        self.verticalLayout.addWidget(self.frame_label)
        self.output_layout.addWidget(self.frame_group)
        self.main_layout.addWidget(self.output_group)
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
        self.main_layout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 158, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_layout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout.addWidget(self.button_box)
        self.main_layout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.button_box.rejected.connect(Dialog.reject)
        self.assembly_radio.toggled['bool'].connect(self.assembly_group.setEnabled)
        self.frame_radio.toggled['bool'].connect(self.frame_group.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.path_label.setText(_translate("Dialog", "Directory:"))
        self.choose_dir_button.setText(_translate("Dialog", "..."))
        self.newfolder_option.setText(_translate("Dialog", "Export to a folder with project name (it will be create if not exist)"))
        self.filename_label.setText(_translate("Dialog", "Main file name:"))
        self.filename_suffix_label.setText(_translate("Dialog", ".slvs"))
        self.output_group.setTitle(_translate("Dialog", "Output types"))
        self.assembly_radio.setText(_translate("Dialog", "&Assembly"))
        self.link_radius_label.setText(_translate("Dialog", "Fillet radius:"))
        self.frame_radio.setText(_translate("Dialog", "O&nly wire frame"))
        self.groupBox.setTitle(_translate("Dialog", "Write mode"))
        self.overwrite_radio.setText(_translate("Dialog", "A&lways overwrite"))
        self.warn_radio.setText(_translate("Dialog", "Warning &me then back to this dialog"))
from pyslvs_ui import icons_rc
