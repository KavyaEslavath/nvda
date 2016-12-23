# -*- coding: UTF-8 -*-
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2016 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""
Contains upgrade steps for the NVDA configuration files. These steps are run to ensure that a configuration file
complies with the latest schema (@see configSpec.py).

To add a new step (after modifying the schema and incrementing the schema version number) add a new method to this
module. The method name should be in the form "upgradeConfigFrom_X_to_Y" where X is the previous schema version, and Y
is the current schema version. The argument profile will be a configobj.ConfigObj object. The function should ensure 
that no information is lost, while updating the ConfigObj to meet the requirements of the new schema.
"""

from logHandler import log

# add upgrade steps here.