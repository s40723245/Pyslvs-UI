# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/synthesis/dimensional_synthesis/dialogs/options.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from core.QtModules import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(461, 559)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/synthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.max_gen_option = QtWidgets.QRadioButton(Dialog)
        self.max_gen_option.setChecked(True)
        self.max_gen_option.setObjectName("max_gen_option")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.max_gen_option)
        self.max_gen = QtWidgets.QSpinBox(Dialog)
        self.max_gen.setMinimum(0)
        self.max_gen.setMaximum(5000)
        self.max_gen.setSingleStep(100)
        self.max_gen.setProperty("value", 1000)
        self.max_gen.setObjectName("max_gen")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.max_gen)
        self.min_fit_option = QtWidgets.QRadioButton(Dialog)
        self.min_fit_option.setObjectName("min_fit_option")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.min_fit_option)
        self.min_fit = QtWidgets.QDoubleSpinBox(Dialog)
        self.min_fit.setEnabled(False)
        self.min_fit.setMaximum(2000.0)
        self.min_fit.setProperty("value", 25.0)
        self.min_fit.setObjectName("min_fit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.min_fit)
        self.report_label = QtWidgets.QLabel(Dialog)
        self.report_label.setObjectName("report_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.report_label)
        self.report = QtWidgets.QSpinBox(Dialog)
        self.report.setProperty("value", 10)
        self.report.setObjectName("report")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.report)
        self.max_time_option = QtWidgets.QRadioButton(Dialog)
        self.max_time_option.setObjectName("max_time_option")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.max_time_option)
        self.max_time = QtWidgets.QWidget(Dialog)
        self.max_time.setEnabled(False)
        self.max_time.setObjectName("max_time")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.max_time)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.max_time_h = QtWidgets.QSpinBox(self.max_time)
        self.max_time_h.setObjectName("max_time_h")
        self.horizontalLayout_2.addWidget(self.max_time_h)
        self.label_2 = QtWidgets.QLabel(self.max_time)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.max_time_m = QtWidgets.QSpinBox(self.max_time)
        self.max_time_m.setMaximum(59)
        self.max_time_m.setProperty("value", 15)
        self.max_time_m.setObjectName("max_time_m")
        self.horizontalLayout_2.addWidget(self.max_time_m)
        self.label_3 = QtWidgets.QLabel(self.max_time)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.max_time_s = QtWidgets.QSpinBox(self.max_time)
        self.max_time_s.setMaximum(59)
        self.max_time_s.setSingleStep(10)
        self.max_time_s.setObjectName("max_time_s")
        self.horizontalLayout_2.addWidget(self.max_time_s)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.max_time)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pop_size = QtWidgets.QSpinBox(Dialog)
        self.pop_size.setMinimum(10)
        self.pop_size.setMaximum(10000)
        self.pop_size.setSingleStep(10)
        self.pop_size.setObjectName("pop_size")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pop_size)
        self.verticalLayout.addLayout(self.formLayout)
        self.splitter = QtWidgets.QSplitter(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.alg_table = QtWidgets.QTableWidget(self.splitter)
        self.alg_table.setObjectName("alg_table")
        self.alg_table.setColumnCount(2)
        self.alg_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.alg_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.alg_table.setHorizontalHeaderItem(1, item)
        self.alg_table.horizontalHeader().setDefaultSectionSize(150)
        self.alg_table.horizontalHeader().setMinimumSectionSize(150)
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reset_button = QtWidgets.QPushButton(Dialog)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout.addWidget(self.reset_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout.addWidget(self.button_box)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)
        self.max_gen_option.toggled['bool'].connect(self.max_gen.setEnabled)
        self.min_fit_option.toggled['bool'].connect(self.min_fit.setEnabled)
        self.max_time_option.toggled['bool'].connect(self.max_time.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.max_gen_option.setToolTip(_translate("Dialog", "<html><head/><body><p>This parameter determines the generations of evolution.</p><p>If the value set to 0, algorithm will stop only when you clicked the interrupt button.</p></body></html>"))
        self.max_gen_option.setText(_translate("Dialog", "Max generation: (?)"))
        self.min_fit_option.setToolTip(_translate("Dialog", "<html><head/><body><p>This parameter determines the last fitness of evolution.</p><p>If the value set to 0, algorithm will stop only when you clicked the interrupt button.</p></body></html>"))
        self.min_fit_option.setText(_translate("Dialog", "Minimum fitness: (?)"))
        self.report_label.setToolTip(_translate("Dialog", "<html><head/><body><p>If the value set to 0, algorithm will report in every 10 generations.</p></body></html>"))
        self.report_label.setText(_translate("Dialog", "Report in every: (?)"))
        self.max_time_option.setToolTip(_translate("Dialog", "<html><head/><body><p>This parameter determines the times of evolution.</p><p>If the value set to 0, algorithm will stop only when you clicked the interrupt button.</p></body></html>"))
        self.max_time_option.setText(_translate("Dialog", "Max time: (?)"))
        self.label_2.setText(_translate("Dialog", ":"))
        self.label_3.setText(_translate("Dialog", ":"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p>The greater the number will make possibilities more available, but will result in longer selection times.</p></body></html>"))
        self.label.setText(_translate("Dialog", "Initial population: (?)"))
        item = self.alg_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Parameter"))
        item = self.alg_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Value"))
        self.reset_button.setText(_translate("Dialog", "Reset to Default"))


import icons_rc
