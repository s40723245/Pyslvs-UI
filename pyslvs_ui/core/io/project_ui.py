# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/core/io/project.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 781)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/id.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.main_layout = QtWidgets.QVBoxLayout(Form)
        self.main_layout.setObjectName("main_layout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.file_name_title = QtWidgets.QLabel(Form)
        self.file_name_title.setObjectName("file_name_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.file_name_title)
        self.file_name_label = QtWidgets.QLineEdit(Form)
        self.file_name_label.setReadOnly(True)
        self.file_name_label.setObjectName("file_name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.file_name_label)
        self.path_title = QtWidgets.QLabel(Form)
        self.path_title.setObjectName("path_title")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.path_title)
        self.path_label = QtWidgets.QLineEdit(Form)
        self.path_label.setReadOnly(True)
        self.path_label.setObjectName("path_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.path_label)
        self.owner_title = QtWidgets.QLabel(Form)
        self.owner_title.setObjectName("owner_title")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.owner_title)
        self.owner_label = QtWidgets.QLabel(Form)
        self.owner_label.setObjectName("owner_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.owner_label)
        self.last_modified_title = QtWidgets.QLabel(Form)
        self.last_modified_title.setObjectName("last_modified_title")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.last_modified_title)
        self.last_modified_label = QtWidgets.QLabel(Form)
        self.last_modified_label.setObjectName("last_modified_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.last_modified_label)
        self.file_size_title = QtWidgets.QLabel(Form)
        self.file_size_title.setObjectName("file_size_title")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.file_size_title)
        self.file_size_label = QtWidgets.QLabel(Form)
        self.file_size_label.setObjectName("file_size_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.file_size_label)
        self.type_title = QtWidgets.QLabel(Form)
        self.type_title.setObjectName("type_title")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.type_title)
        self.type_label = QtWidgets.QLabel(Form)
        self.type_label.setObjectName("type_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.type_label)
        self.main_layout.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_layout.addWidget(self.line)
        self.overview_button = QtWidgets.QPushButton(Form)
        self.overview_button.setIcon(icon)
        self.overview_button.setObjectName("overview_button")
        self.main_layout.addWidget(self.overview_button)
        self.ex_expression_button = QtWidgets.QPushButton(Form)
        self.ex_expression_button.setIcon(icon)
        self.ex_expression_button.setObjectName("ex_expression_button")
        self.main_layout.addWidget(self.ex_expression_button)
        self.export_group = QtWidgets.QGroupBox(Form)
        self.export_group.setObjectName("export_group")
        self.gridLayout = QtWidgets.QGridLayout(self.export_group)
        self.gridLayout.setObjectName("gridLayout")
        self.ex_dxf_button = QtWidgets.QPushButton(self.export_group)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/dxf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_dxf_button.setIcon(icon1)
        self.ex_dxf_button.setIconSize(QtCore.QSize(100, 50))
        self.ex_dxf_button.setObjectName("ex_dxf_button")
        self.gridLayout.addWidget(self.ex_dxf_button, 0, 0, 1, 1)
        self.ex_slvs_button = QtWidgets.QPushButton(self.export_group)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/solvespace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_slvs_button.setIcon(icon2)
        self.ex_slvs_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_slvs_button.setObjectName("ex_slvs_button")
        self.gridLayout.addWidget(self.ex_slvs_button, 0, 1, 1, 1)
        self.ex_py_button = QtWidgets.QPushButton(self.export_group)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/script.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_py_button.setIcon(icon3)
        self.ex_py_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_py_button.setObjectName("ex_py_button")
        self.gridLayout.addWidget(self.ex_py_button, 1, 0, 1, 1)
        self.ex_image_button = QtWidgets.QPushButton(self.export_group)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_image_button.setIcon(icon4)
        self.ex_image_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_image_button.setObjectName("ex_image_button")
        self.gridLayout.addWidget(self.ex_image_button, 1, 1, 1, 1)
        self.ex_pmks_button = QtWidgets.QPushButton(self.export_group)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/pmks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_pmks_button.setIcon(icon5)
        self.ex_pmks_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_pmks_button.setObjectName("ex_pmks_button")
        self.gridLayout.addWidget(self.ex_pmks_button, 0, 2, 1, 1)
        self.ex_capture_button = QtWidgets.QPushButton(self.export_group)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/capture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_capture_button.setIcon(icon6)
        self.ex_capture_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_capture_button.setObjectName("ex_capture_button")
        self.gridLayout.addWidget(self.ex_capture_button, 1, 2, 1, 1)
        self.main_layout.addWidget(self.export_group)
        self.import_group = QtWidgets.QGroupBox(Form)
        self.import_group.setObjectName("import_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.import_group)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.im_example_button = QtWidgets.QPushButton(self.import_group)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/example.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.im_example_button.setIcon(icon7)
        self.im_example_button.setIconSize(QtCore.QSize(50, 50))
        self.im_example_button.setObjectName("im_example_button")
        self.gridLayout_2.addWidget(self.im_example_button, 0, 1, 1, 1)
        self.im_pmks_button = QtWidgets.QPushButton(self.import_group)
        self.im_pmks_button.setIcon(icon5)
        self.im_pmks_button.setIconSize(QtCore.QSize(50, 50))
        self.im_pmks_button.setObjectName("im_pmks_button")
        self.gridLayout_2.addWidget(self.im_pmks_button, 0, 0, 1, 1)
        self.main_layout.addWidget(self.import_group)
        self.history_tabs = QtWidgets.QTabWidget(Form)
        self.history_tabs.setObjectName("history_tabs")
        self.main_layout.addWidget(self.history_tabs)

        self.retranslateUi(Form)
        self.history_tabs.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.file_name_title.setText(_translate("Form", "File name:"))
        self.path_title.setText(_translate("Form", "Path:"))
        self.owner_title.setText(_translate("Form", "Owner:"))
        self.last_modified_title.setText(_translate("Form", "Last modified:"))
        self.file_size_title.setText(_translate("Form", "File size:"))
        self.type_title.setText(_translate("Form", "Type:"))
        self.overview_button.setText(_translate("Form", "Project overview"))
        self.ex_expression_button.setText(_translate("Form", "Mechanism expression"))
        self.export_group.setTitle(_translate("Form", "Export"))
        self.ex_dxf_button.setStatusTip(_translate("Form", "Export as DXF format."))
        self.ex_slvs_button.setStatusTip(_translate("Form", "Export as Solvespace format."))
        self.ex_py_button.setStatusTip(_translate("Form", "Export as Python script."))
        self.ex_image_button.setStatusTip(_translate("Form", "Export as image formats."))
        self.ex_pmks_button.setStatusTip(_translate("Form", "Export as PMKS URL."))
        self.ex_capture_button.setStatusTip(_translate("Form", "Capture the main canvas into clipboard."))
        self.import_group.setTitle(_translate("Form", "Import"))
        self.im_example_button.setStatusTip(_translate("Form", "Import from an example."))
        self.im_pmks_button.setStatusTip(_translate("Form", "Import from PMKS URL."))


from pyslvs_ui import icons_rc
