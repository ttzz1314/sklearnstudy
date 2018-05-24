#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

sys_is_le = sys.byteorder == 'little'
native_code = sys_is_le and '<' or '>'
swapped_code = sys_is_le and '>' or '<'
native_dt = np.dtype(native_code+'i2')
swapped_dt = np.dtype(swapped_code+'i2')

native_dt.newbyteorder('S') == swapped_dt

native_dt.newbyteorder() == swapped_dt

native_dt == swapped_dt.newbyteorder('S')

native_dt == swapped_dt.newbyteorder('=')

native_dt == swapped_dt.newbyteorder('N')

native_dt == native_dt.newbyteorder('|')

np.dtype('<i2') == native_dt.newbyteorder('<')

np.dtype('<i2') == native_dt.newbyteorder('L')

np.dtype('>i2') == native_dt.newbyteorder('>')

np.dtype('>i2') == native_dt.newbyteorder('B')
