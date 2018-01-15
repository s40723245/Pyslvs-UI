# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/synthesis/Collections/Structure.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(481, 787)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/collection-structure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph_engine_text = QtWidgets.QLabel(Form)
        self.graph_engine_text.setObjectName("graph_engine_text")
        self.horizontalLayout.addWidget(self.graph_engine_text)
        self.graph_engine = QtWidgets.QComboBox(Form)
        self.graph_engine.setObjectName("graph_engine")
        self.horizontalLayout.addWidget(self.graph_engine)
        self.reload_atlas = QtWidgets.QPushButton(Form)
        self.reload_atlas.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/dataupdate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload_atlas.setIcon(icon1)
        self.reload_atlas.setObjectName("reload_atlas")
        self.horizontalLayout.addWidget(self.reload_atlas)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.add_by_files_button = QtWidgets.QPushButton(Form)
        self.add_by_files_button.setObjectName("add_by_files_button")
        self.horizontalLayout_5.addWidget(self.add_by_files_button)
        self.add_by_edges_button = QtWidgets.QPushButton(Form)
        self.add_by_edges_button.setObjectName("add_by_edges_button")
        self.horizontalLayout_5.addWidget(self.add_by_edges_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.collection_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.collection_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.collection_list.setIconSize(QtCore.QSize(100, 100))
        self.collection_list.setMovement(QtWidgets.QListView.Static)
        self.collection_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.collection_list.setViewMode(QtWidgets.QListView.IconMode)
        self.collection_list.setUniformItemSizes(True)
        self.collection_list.setObjectName("collection_list")
        self.verticalLayout_3.addWidget(self.collection_list)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.save_atlas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_atlas.setIcon(icon2)
        self.save_atlas.setObjectName("save_atlas")
        self.horizontalLayout_7.addWidget(self.save_atlas)
        self.save_edges = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/properties.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_edges.setIcon(icon3)
        self.save_edges.setObjectName("save_edges")
        self.horizontalLayout_7.addWidget(self.save_edges)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clear_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon4)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_6.addWidget(self.clear_button)
        self.delete_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_button.setEnabled(False)
        self.delete_button.setIcon(icon4)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_6.addWidget(self.delete_button)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selection_window = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.selection_window.setMinimumSize(QtCore.QSize(210, 230))
        self.selection_window.setMaximumSize(QtCore.QSize(210, 230))
        self.selection_window.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.selection_window.setIconSize(QtCore.QSize(200, 200))
        self.selection_window.setMovement(QtWidgets.QListView.Static)
        self.selection_window.setViewMode(QtWidgets.QListView.IconMode)
        self.selection_window.setObjectName("selection_window")
        self.horizontalLayout_2.addWidget(self.selection_window)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 230))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Expression_edges = QtWidgets.QLineEdit(self.widget)
        self.Expression_edges.setReadOnly(True)
        self.Expression_edges.setObjectName("Expression_edges")
        self.horizontalLayout_3.addWidget(self.Expression_edges)
        self.Expression_copy = QtWidgets.QPushButton(self.widget)
        self.Expression_copy.setObjectName("Expression_copy")
        self.horizontalLayout_3.addWidget(self.Expression_copy)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.NL_text = QtWidgets.QLabel(self.widget)
        self.NL_text.setObjectName("NL_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NL_text)
        self.NL = QtWidgets.QLabel(self.widget)
        self.NL.setObjectName("NL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NL)
        self.NJ_text = QtWidgets.QLabel(self.widget)
        self.NJ_text.setObjectName("NJ_text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.NJ_text)
        self.NJ = QtWidgets.QLabel(self.widget)
        self.NJ.setObjectName("NJ")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NJ)
        self.DOF_text = QtWidgets.QLabel(self.widget)
        self.DOF_text.setObjectName("DOF_text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.DOF_text)
        self.DOF = QtWidgets.QLabel(self.widget)
        self.DOF.setObjectName("DOF")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.DOF)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.triangle_button = QtWidgets.QPushButton(self.widget)
        self.triangle_button.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/collection-triangular-iteration.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.triangle_button.setIcon(icon5)
        self.triangle_button.setObjectName("triangle_button")
        self.verticalLayout_2.addWidget(self.triangle_button)
        self.grounded_button = QtWidgets.QPushButton(self.widget)
        self.grounded_button.setEnabled(False)
        self.grounded_button.setIcon(icon1)
        self.grounded_button.setObjectName("grounded_button")
        self.verticalLayout_2.addWidget(self.grounded_button)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.grounded_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.grounded_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.grounded_list.setIconSize(QtCore.QSize(150, 150))
        self.grounded_list.setMovement(QtWidgets.QListView.Static)
        self.grounded_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.grounded_list.setViewMode(QtWidgets.QListView.IconMode)
        self.grounded_list.setUniformItemSizes(True)
        self.grounded_list.setObjectName("grounded_list")
        self.horizontalLayout_4.addWidget(self.grounded_list)
        self.grounded_merge = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.grounded_merge.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grounded_merge.sizePolicy().hasHeightForWidth())
        self.grounded_merge.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.grounded_merge.setIcon(icon6)
        self.grounded_merge.setObjectName("grounded_merge")
        self.horizontalLayout_4.addWidget(self.grounded_merge)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.graph_engine.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.graph_engine_text.setText(_translate("Form", "Engine: "))
        self.graph_engine.setStatusTip(_translate("Form", "Layout engine from NetworkX and Pydot (Graphviz)."))
        self.reload_atlas.setToolTip(_translate("Form", "Add to collection."))
        self.add_by_files_button.setStatusTip(_translate("Form", "Add the chain by edge expression from text files."))
        self.add_by_files_button.setText(_translate("Form", "Append by text files"))
        self.add_by_edges_button.setStatusTip(_translate("Form", "Add the chain by edge expression."))
        self.add_by_edges_button.setText(_translate("Form", "Add by edges"))
        self.save_atlas.setStatusTip(_translate("Form", "Save the atlas to image file."))
        self.save_atlas.setText(_translate("Form", "Save atlas"))
        self.save_edges.setStatusTip(_translate("Form", "Save the edges of atlas to text file."))
        self.save_edges.setText(_translate("Form", "Save edges"))
        self.clear_button.setText(_translate("Form", "Clear all"))
        self.delete_button.setStatusTip(_translate("Form", "Delete this chain."))
        self.delete_button.setText(_translate("Form", "Delete"))
        self.Expression_copy.setStatusTip(_translate("Form", "Copy expression."))
        self.Expression_copy.setText(_translate("Form", "Copy"))
        self.NL_text.setText(_translate("Form", "Number of links:"))
        self.NL.setText(_translate("Form", "0"))
        self.NJ_text.setText(_translate("Form", "Number of joints:"))
        self.NJ.setText(_translate("Form", "0"))
        self.DOF_text.setText(_translate("Form", "Degree of freedom:"))
        self.DOF.setText(_translate("Form", "0"))
        self.triangle_button.setStatusTip(_translate("Form", "Use trangular formula to do dimentional synthesis."))
        self.triangle_button.setText(_translate("Form", "Triangular modeling"))
        self.grounded_button.setStatusTip(_translate("Form", "Re-layout the grounded chains."))
        self.grounded_button.setText(_translate("Form", "Generate layout"))
        self.grounded_merge.setStatusTip(_translate("Form", "Merge the specified chain to canvas with current layout."))
        self.grounded_merge.setText(_translate("Form", "Merge"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

