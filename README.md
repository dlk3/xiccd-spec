# Fedora RPM Package For xiccd Daemon

xiccd is a simple bridge between colord and X. It does the following tasks:

 * Enumerates displays and register them in colord;
 * Creates default ICC profiles based on EDID data;
 * Applies ICC profiles provided by colord;
 * Maintains user's private ICC storage directory.

xiccd is used to enable the xfce4-color-settings tool in the XFCE
desktop.  This allows for simple configuration of the color profiles 
that the colord daemon loads for displays attached to these systems.

This project contains a SPEC file for building xiccd RPMs that can be
used with the Fedora Linux distribution.  It also contains the scripts
that are used to build these RPMs in a podman container.

Copyright (C) 2020  David King <dave@daveking.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

