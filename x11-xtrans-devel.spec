%global debug_package %{nil}

Name:		x11-xtrans-devel
Summary:	Abstract network code for X
Version:	1.5.2
Release:	1
Group:		Development/X11
License:	MIT
URL:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/lib/xtrans-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch0:		xtrans-1.2.7-tirpc.patch
Conflicts:	libxorg-x11-devel < 7.0
BuildRequires:	pkgconfig(xorg-macros) >= 1.12

%description
Abstract network code for X.

%prep
%autosetup -n xtrans-%{version} -p1
aclocal
automake -a
autoconf

%build
%configure
%make_build

%install
%make_install
rm %{buildroot}%{_datadir}/doc/xtrans/xtrans.*

%files
%doc doc/xtrans.xml
%{_datadir}/pkgconfig/xtrans.pc
%{_datadir}/aclocal/xtrans.m4
%{_includedir}/X11/Xtrans/Xtransint.h
%{_includedir}/X11/Xtrans/Xtrans.h
%{_includedir}/X11/Xtrans/Xtrans.c
%{_includedir}/X11/Xtrans/Xtranslcl.c
%{_includedir}/X11/Xtrans/Xtranssock.c
%{_includedir}/X11/Xtrans/Xtransutil.c
%{_includedir}/X11/Xtrans/transport.c
