Name: x11-xtrans-devel
Summary:  Abstract network code for X
Version: 1.2.7
Release: 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/xtrans-%{version}.tar.bz2
Source1: %name.rpmlintrc
Patch0: xtrans-1.2.7-tirpc.patch
Patch1:	xtrans-aarch64.patch
Conflicts: libxorg-x11-devel < 7.0
BuildRequires: pkgconfig(xorg-macros) >= 1.12

%description
Abstract network code for X

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

%pre 
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files
%doc doc/xtrans.xml
%{_datadir}/pkgconfig/xtrans.pc
%{_datadir}/aclocal/xtrans.m4
%{_includedir}/X11/Xtrans/Xtransint.h
%{_includedir}/X11/Xtrans/Xtrans.h
%{_includedir}/X11/Xtrans/Xtrans.c
%{_includedir}/X11/Xtrans/Xtranslcl.c
%{_includedir}/X11/Xtrans/Xtranssock.c
%{_includedir}/X11/Xtrans/Xtranstli.c
%{_includedir}/X11/Xtrans/Xtransutil.c
%{_includedir}/X11/Xtrans/transport.c


%changelog
* Thu Oct 04 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.7-3
+ Revision: 818376
- Teach xtrans to find authdes_create and friends in tirpc, not glibc

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.7-1
+ Revision: 786721
- version update 1.2.7

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-2
+ Revision: 671232
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.6-1mdv2011.0
+ Revision: 595704
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.5-1mdv2010.1
+ Revision: 464649
- New version: 1.2.5

* Sat Aug 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2.4-1mdv2010.0
+ Revision: 407073
- update to new version 1.2.4

* Mon Jan 12 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.3-1mdv2009.1
+ Revision: 328597
- New version

* Mon Dec 22 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.2-1mdv2009.1
+ Revision: 317651
- Update to version 1.2.2

* Wed Jul 16 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.1-1mdv2009.0
+ Revision: 236559
- Update to version 1.2.1

* Mon May 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1mdv2009.0
+ Revision: 206235
- Update to upstream release version 1.2.

* Mon Apr 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1mdv2009.0
+ Revision: 192900
- Update to version 1.1.

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.4-1mdv2008.1
+ Revision: 98583
- new upstream version: 1.0.4 (typo fix for 1.0.3)
- minor spec cleanup

