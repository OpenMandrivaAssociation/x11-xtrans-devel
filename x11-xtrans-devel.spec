Name:		x11-xtrans-devel
Summary:	Abstract network code for X
Version:	1.3.5
Release:	5
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/xtrans-%{version}.tar.bz2
Source1:	%name.rpmlintrc
Patch0:		xtrans-1.2.7-tirpc.patch
Conflicts:	libxorg-x11-devel < 7.0
BuildRequires:	pkgconfig(xorg-macros) >= 1.12

%description
Abstract network code for X.

%prep
%setup -q -n xtrans-%{version}
%apply_patches
aclocal
automake -a
autoconf

%build
%configure
%make

%install
%makeinstall_std
rm %{buildroot}%_datadir/doc/xtrans/xtrans.*

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
