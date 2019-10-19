# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/io/project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(326, 588)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/id.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.background_label = QtWidgets.QLabel(Form)
        self.background_label.setObjectName("background_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.background_label)
        self.background_layout = QtWidgets.QHBoxLayout()
        self.background_layout.setObjectName("background_layout")
        self.background_option = QtWidgets.QLineEdit(Form)
        self.background_option.setClearButtonEnabled(True)
        self.background_option.setObjectName("background_option")
        self.background_layout.addWidget(self.background_option)
        self.background_choose_dir = QtWidgets.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/loadfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.background_choose_dir.setIcon(icon1)
        self.background_choose_dir.setObjectName("background_choose_dir")
        self.background_layout.addWidget(self.background_choose_dir)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.background_layout)
        self.background_scale_label = QtWidgets.QLabel(Form)
        self.background_scale_label.setObjectName("background_scale_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.background_scale_label)
        self.background_scale_option = QtWidgets.QDoubleSpinBox(Form)
        self.background_scale_option.setMinimum(0.01)
        self.background_scale_option.setMaximum(10.0)
        self.background_scale_option.setSingleStep(0.02)
        self.background_scale_option.setObjectName("background_scale_option")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.background_scale_option)
        self.background_offset_label = QtWidgets.QLabel(Form)
        self.background_offset_label.setObjectName("background_offset_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.background_offset_label)
        self.background_offset_layout = QtWidgets.QHBoxLayout()
        self.background_offset_layout.setObjectName("background_offset_layout")
        self.background_x_option = QtWidgets.QDoubleSpinBox(Form)
        self.background_x_option.setMinimum(-999999.0)
        self.background_x_option.setMaximum(999999.0)
        self.background_x_option.setObjectName("background_x_option")
        self.background_offset_layout.addWidget(self.background_x_option)
        self.background_y_option = QtWidgets.QDoubleSpinBox(Form)
        self.background_y_option.setMinimum(-999999.0)
        self.background_y_option.setMaximum(999999.0)
        self.background_y_option.setObjectName("background_y_option")
        self.background_offset_layout.addWidget(self.background_y_option)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.background_offset_layout)
        self.background_opacity_label = QtWidgets.QLabel(Form)
        self.background_opacity_label.setObjectName("background_opacity_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.background_opacity_label)
        self.background_opacity_option = QtWidgets.QDoubleSpinBox(Form)
        self.background_opacity_option.setMaximum(1.0)
        self.background_opacity_option.setSingleStep(0.1)
        self.background_opacity_option.setProperty("value", 1.0)
        self.background_opacity_option.setObjectName("background_opacity_option")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.background_opacity_option)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.overview_button = QtWidgets.QPushButton(Form)
        self.overview_button.setIcon(icon)
        self.overview_button.setObjectName("overview_button")
        self.horizontalLayout_2.addWidget(self.overview_button)
        self.ex_expression_button = QtWidgets.QPushButton(Form)
        self.ex_expression_button.setIcon(icon)
        self.ex_expression_button.setObjectName("ex_expression_button")
        self.horizontalLayout_2.addWidget(self.ex_expression_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.export_group = QtWidgets.QGroupBox(Form)
        self.export_group.setObjectName("export_group")
        self.gridLayout = QtWidgets.QGridLayout(self.export_group)
        self.gridLayout.setObjectName("gridLayout")
        self.ex_dxf_button = QtWidgets.QPushButton(self.export_group)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/dxf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_dxf_button.setIcon(icon2)
        self.ex_dxf_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_dxf_button.setObjectName("ex_dxf_button")
        self.gridLayout.addWidget(self.ex_dxf_button, 0, 0, 1, 1)
        self.ex_slvs_button = QtWidgets.QPushButton(self.export_group)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/solvespace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_slvs_button.setIcon(icon3)
        self.ex_slvs_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_slvs_button.setObjectName("ex_slvs_button")
        self.gridLayout.addWidget(self.ex_slvs_button, 0, 1, 1, 1)
        self.ex_py_button = QtWidgets.QPushButton(self.export_group)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/script.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_py_button.setIcon(icon4)
        self.ex_py_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_py_button.setObjectName("ex_py_button")
        self.gridLayout.addWidget(self.ex_py_button, 1, 0, 1, 1)
        self.ex_image_button = QtWidgets.QPushButton(self.export_group)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_image_button.setIcon(icon5)
        self.ex_image_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_image_button.setObjectName("ex_image_button")
        self.gridLayout.addWidget(self.ex_image_button, 1, 1, 1, 1)
        self.ex_pmks_button = QtWidgets.QPushButton(self.export_group)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/pmks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_pmks_button.setIcon(icon6)
        self.ex_pmks_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_pmks_button.setObjectName("ex_pmks_button")
        self.gridLayout.addWidget(self.ex_pmks_button, 0, 2, 1, 1)
        self.ex_capture_button = QtWidgets.QPushButton(self.export_group)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/capture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ex_capture_button.setIcon(icon7)
        self.ex_capture_button.setIconSize(QtCore.QSize(50, 50))
        self.ex_capture_button.setObjectName("ex_capture_button")
        self.gridLayout.addWidget(self.ex_capture_button, 1, 2, 1, 1)
        self.horizontalLayout.addWidget(self.export_group)
        self.import_group = QtWidgets.QGroupBox(Form)
        self.import_group.setObjectName("import_group")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.import_group)
        self.verticalLayout.setObjectName("verticalLayout")
        self.im_example_button = QtWidgets.QPushButton(self.import_group)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/example.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.im_example_button.setIcon(icon8)
        self.im_example_button.setIconSize(QtCore.QSize(50, 50))
        self.im_example_button.setObjectName("im_example_button")
        self.verticalLayout.addWidget(self.im_example_button)
        self.im_pmks_button = QtWidgets.QPushButton(self.import_group)
        self.im_pmks_button.setIcon(icon6)
        self.im_pmks_button.setIconSize(QtCore.QSize(50, 50))
        self.im_pmks_button.setObjectName("im_pmks_button")
        self.verticalLayout.addWidget(self.im_pmks_button)
        self.horizontalLayout.addWidget(self.import_group)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.history_tabs = QtWidgets.QTabWidget(Form)
        self.history_tabs.setObjectName("history_tabs")
        self.verticalLayout_2.addWidget(self.history_tabs)

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
        self.background_label.setText(_translate("Form", "Background"))
        self.background_option.setPlaceholderText(_translate("Form", "Disabled"))
        self.background_scale_label.setText(_translate("Form", "Background scale"))
        self.background_offset_label.setText(_translate("Form", "Background offset"))
        self.background_opacity_label.setText(_translate("Form", "Background opacity"))
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