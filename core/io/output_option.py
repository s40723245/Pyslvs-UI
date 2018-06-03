# -*- coding: utf-8 -*-

"""Output dialog for slvs format."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import Tuple, Callable, Optional
from os.path import isdir, isfile
import shutil
from subprocess import Popen, DEVNULL
from core.QtModules import (
    pyqtSlot,
    Qt,
    QDialog,
    QDir,
    QMessageBox,
    QFileDialog,
    QTextEdit,
    QWidget,
)
from core.libs import VPoint
from .slvs import slvs_frame, slvs_part
from .dxf import dxf_frame, dxf_boundary
from .Ui_output_option import Ui_Dialog


def _getname(widget: QTextEdit, *, ispath: bool = False) -> str:
    """Return the file name of widget."""
    text = widget.text()
    if ispath:
        if isdir(text):
            return text
        else:
            return widget.placeholderText()
    if text:
        return "".join(x for x in text if x.isalnum() or (x in "._- "))
    else:
        return widget.placeholderText()


class _OutputDialog(QDialog, Ui_Dialog):
    
    """Output dialog template."""
    
    def __init__(self,
        format: str,
        env: str,
        file_name: str,
        vpoints: Tuple[VPoint],
        v_to_slvs: Callable[[], Tuple[int, int]],
        parent: QWidget
    ):
        """Comes in environment variable and workbook name."""
        super(_OutputDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.path_edit.setPlaceholderText(env)
        self.filename_edit.setPlaceholderText(file_name)
        self.setWindowTitle("Export {} project".format(format))
        self.vpoints = vpoints
        self.v_to_slvs = v_to_slvs
    
    @pyqtSlot()
    def on_choosedir_button_clicked(self):
        """Choose path and it will be set as environment variable if accepted."""
        path = self.path_edit.text()
        if not isdir(path):
            path = self.path_edit.placeholderText()
        path = QFileDialog.getExistingDirectory(self, "Choose a directory", path)
        if path:
            self.path_edit.setText(path)
    
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """Use the file path to export the project."""
        dir = QDir(_getname(self.path_edit, ispath=True))
        if self.newfolder_option.isChecked():
            new_folder = self.filename_edit.placeholderText()
            if (not dir.mkdir(new_folder)) and self.warn_radio.isChecked():
                self.exist_warning(new_folder, folder=True)
                return
            dir.cd(new_folder)
            del new_folder
        if self.do(dir):
            self.accept()
    
    def do(self) -> Optional[bool]:
        """Do the saving work here, return True if done."""
        raise NotImplementedError("virtual function")
    
    def exist_warning(self, name: str, *, folder: bool = False):
        """Show the "file is exist" message box."""
        QMessageBox.warning(self,
            "{} exist".format("Folder" if folder else "File"),
            "The folder named {} is exist.".format(name) if folder else
            "The file {} is exist.".format(name)
        )


class SlvsOutputDialog(_OutputDialog):
    
    """Solvespace format."""
    
    def __init__(self, *args):
        """Type name: "Solvespace module"."""
        super(SlvsOutputDialog, self).__init__("Solvespace module", *args)
    
    def do(self, dir: QDir) -> Optional[bool]:
        """Output types:
        
        + Assembly
        + Only wire frame
        """
        file_name = dir.filePath(_getname(self.filename_edit) + '.slvs')
        if isfile(file_name) and self.warn_radio.isChecked():
            self.exist_warning(file_name)
            return
        
        #Wire frame
        slvs_frame(self.vpoints, self.v_to_slvs, file_name)
        
        #Open Solvespace by commend line if available.
        cmd = shutil.which("solvespace")
        if cmd:
            Popen([cmd , file_name], stdout=DEVNULL, stderr=DEVNULL)
        
        if self.frame_radio.isChecked():
            self.accept()
            return
        
        #Assembly
        vlinks = {}
        for i, vpoint in enumerate(self.vpoints):
            for link in vpoint.links:
                if link in vlinks:
                    vlinks[link].add(i)
                else:
                    vlinks[link] = {i}
        for name, points in vlinks.items():
            if name == 'ground':
                continue
            file_name = dir.filePath(name + '.slvs')
            if isfile(file_name) and self.warn_radio.isChecked():
                self.exist_warning(file_name)
                return
            slvs_part([
                self.vpoints[i] for i in points
            ], self.link_radius.value(), file_name)
        
        return True


class DxfOutputDialog(_OutputDialog):
    
    """DXF format."""
    
    def __init__(self, *args):
        """Type name: "Solvespace module"."""
        super(DxfOutputDialog, self).__init__("Solvespace module", *args)
    
    def do(self, dir: QDir) -> Optional[bool]:
        """Output types:
        
        + Boundary
        + Frame
        """
        file_name = dir.filePath(_getname(self.filename_edit) + '.dxf')
        if isfile(file_name) and self.warn_radio.isChecked():
            self.exist_warning(file_name)
            return
        
        if self.frame_radio.isChecked():
            #Frame
            dxf_frame(self.vpoints, self.v_to_slvs, file_name)
        elif self.assembly_radio.isChecked():
            #Boundary
            dxf_boundary(self.vpoints, file_name)
        return True