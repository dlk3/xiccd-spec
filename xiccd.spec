#  A RPM SPEC File For Building xiccd RPM Packages
#
#  Copyright (C) 2020  David King <dave@daveking.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

Name:		xiccd
Version:	0.3.0
Release:	1%{?dist}
Summary:	A simple bridge between colord and X

License:	GPLv3
URL:		https://github.com/agalakhov/xiccd
Source0:	%{name}-%{version}.tar.gz
BuildArch:	x86_64

Requires: xfce4-settings >= 4.14
Requires: colord >= 1.4.4

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: glib2-devel
BuildRequires: colord-devel

%description
xiccd is a simple bridge between colord and X. It is used to enable the 
xfce4-color-settings tool in the XFCE desktop.  This allows for simple 
configuration of the color profiles that the colord daemon loads for 
displays, printers and scanners attached to these systems.

%prep
%setup

%build
autoreconf -i
./configure --prefix=/usr
make PREFIX=/usr %{?_smp_mflags}

%install
make PREFIX=/usr DESTDIR=%{?buildroot} install

%files
%license COPYING
/usr/bin/xiccd
/usr/etc/xdg/autostart/xiccd.desktop
/usr/share/man/man8/xiccd.8.gz

%changelog
* Fri Feb 28 2020 David King <dave@daveking.com> - 0.3.0-1
	Initial Version
