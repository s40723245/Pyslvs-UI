# -*- coding: utf-8 -*-

from __future__ import annotations

"""HDF5 format processing function."""

from typing import TYPE_CHECKING, Dict, Union, Any
from h5py import File, Dataset, Group
from numpy import array, int8
from pyslvs import __version__
from pyslvs_ui.core.QtModules import QMessageBox
from .format_editor import FormatEditor
if TYPE_CHECKING:
    from pyslvs_ui.core.widgets import MainWindowBase


def _h5py_dump(f: File, d: Dict[str, Any], *, prefix: str = ''):
    """Dump function for h5py."""
    for k, v in d.items():
        if prefix:
            key = prefix + '/' + k
        else:
            key = k
        if type(v) is dict:
            _h5py_dump(f, v, prefix=key)
        elif type(v) in {int, float, str, bytes}:
            f[key] = v
        else:
            try:
                a = array(v, dtype=int8)
            except (ValueError, TypeError):
                # Use eval function
                a = f"!{v!r}"
            f[key] = a


def _h5py_load(f: Group) -> Dict[str, Any]:
    """Load function for h5py."""
    data = {}
    for k, v in f.items():  # type: str, Union[Group, Dataset]
        if type(v) is Group:
            data[k] = _h5py_load(v)
        elif type(v) is Dataset:
            value = v[()]
            if (type(value) is str) and value.startswith('!'):
                value = eval(value[1:])
            data[k] = value
    return data


class HDF5Editor(FormatEditor):

    """HDF5 reader and writer."""

    def __init__(self, parent: MainWindowBase):
        super(HDF5Editor, self).__init__(parent)

    @staticmethod
    def test(file_name: str) -> bool:
        """Test the file is valid."""
        try:
            File(file_name, 'r')
        except OSError:
            return False
        else:
            return True

    def save(self, file_name: str) -> None:
        """Save HDF5 file."""
        data = self.save_data()
        with File(file_name, 'w') as f:
            f['pyslvs_ver'] = __version__
            _h5py_dump(f, data)

    def load(self, file_name: str) -> None:
        """Load HDF5 file."""
        with File(file_name, 'r') as f:
            if 'pyslvs_ver' not in f:
                QMessageBox.warning(
                    self,
                    "Invalid file format",
                    f"The file {file_name} is not a Pyslvs project."
                )
                return
            data = _h5py_load(f)
        self.load_data(file_name, data)
