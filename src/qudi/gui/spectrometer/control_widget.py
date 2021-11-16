# -*- coding: utf-8 -*-
"""
This module contains the spectrometer control widget for SpectrometerGui.

Qudi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Qudi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Qudi. If not, see <http://www.gnu.org/licenses/>.

Copyright (c) the Qudi Developers. See the COPYRIGHT.txt file at the
top-level directory of this distribution and at <https://github.com/Ulm-IQO/qudi/>
"""

__all__ = ['SpectrometerControlWidget']

from PySide2 import QtCore
from PySide2 import QtWidgets

from qudi.util.widgets.toggle_switch import ToggleSwitch


class SpectrometerControlWidget(QtWidgets.QWidget):
    """ Widget for the spectrometer controls in SpectrometerGui """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        main_layout = QtWidgets.QGridLayout()
        self.setLayout(main_layout)
        # main_layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        # main_layout.setContentsMargins(1, 1, 1, 1)
        # main_layout.setSpacing(5)

        # Control buttons
        self.acquire_button = QtWidgets.QPushButton('Acquire Spectrum')
        self.acquire_button.setToolTip('Acquire a new spectrum.')
        main_layout.addWidget(self.acquire_button, 0, 0)

        self.spectrum_continue_button = QtWidgets.QPushButton('Continue Spectrum')
        self.spectrum_continue_button.setToolTip(
            'If continuous spectrum is activated, continue averaging.'
        )
        main_layout.addWidget(self.spectrum_continue_button, 0, 1)

        self.save_spectrum_button = QtWidgets.QToolButton()
        self.save_spectrum_button.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )
        self.save_spectrum_button.setSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.Fixed)
        main_layout.addWidget(self.save_spectrum_button, 0, 2)

        self.background_button = QtWidgets.QPushButton('Acquire Background')
        self.background_button.setToolTip('Acquire a new background spectrum.')
        main_layout.addWidget(self.background_button, 1, 0)

        self.save_background_button = QtWidgets.QToolButton()
        self.save_background_button.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )
        self.save_background_button.setSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                                  QtWidgets.QSizePolicy.Fixed)
        main_layout.addWidget(self.save_background_button, 1, 2)

        # Control switches
        switch_layout = QtWidgets.QGridLayout()

        constant_acquisition_label = QtWidgets.QLabel('Constant Acquisition:')
        constant_acquisition_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.constant_acquisition_switch = ToggleSwitch(state_names=('Off', 'On'))
        switch_layout.addWidget(constant_acquisition_label, 0, 0)
        switch_layout.addWidget(self.constant_acquisition_switch, 0, 1)

        background_correction_label = QtWidgets.QLabel('Background Correction:')
        background_correction_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.background_correction_switch = ToggleSwitch(state_names=('Off', 'On'))
        switch_layout.addWidget(background_correction_label, 1, 0)
        switch_layout.addWidget(self.background_correction_switch, 1, 1)

        differential_spectrum_label = QtWidgets.QLabel('Differential Spectrum:')
        differential_spectrum_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.differential_spectrum_switch = ToggleSwitch(state_names=('Off', 'On'))
        switch_layout.addWidget(differential_spectrum_label, 2, 0)
        switch_layout.addWidget(self.differential_spectrum_switch, 2, 1)

        switch_layout.setColumnStretch(2, 1)

        main_layout.addLayout(switch_layout, 2, 0, 1, 3)

        main_layout.setRowStretch(3, 1)
        main_layout.setColumnStretch(3, 1)