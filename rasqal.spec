%define major	3
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name: 	 	rasqal
Summary: 	RDF querying library
Group:		Databases
Version: 	0.9.29
Release: 	1
License:	LGPL
URL:		http://librdf.org/rasqal/
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
Patch0:		rasqal-0.9.28-linkm.patch
BuildRequires:	raptor2-devel > 2.0.4-2
BuildRequires:	libmpfr-devel

%description
Rasqal handles Resource Description Framework (RDF) query syntaxes, query
construction and query execution returning result bindings. The supported
query languages are RDQL and SPARQL.  Rasqal was designed to work closely
with the Redland RDF library but is entirely separate. It is intended to be
a portable library working across many POSIX systems (Unix, GNU/Linux,
BSDs, OSX, cygwin) win32 and others.

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
Obsoletes:	%{mklibname rasqal 0} >= 0.9.16

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%{name}-devel < %{version}-%{release}
Obsoletes:	%{mklibname -d %{name} 0}

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%patch0 -p1 -b .linkm~

%build
%configure2_5x --disable-static
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/%{name}-config

# Zé: clean .la files
rm -f %{buildroot}%{_libdir}/*.la

%check
#make check

%files
%doc AUTHORS COPYING* ChangeLog LICENSE* NEWS* NOTICE README*
%{_bindir}/roqet
%{_mandir}/man1/roqet*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_bindir}/%{name}-config
%{multiarch_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/rasqal*
%{_mandir}/man3/lib*
%{_datadir}/gtk-doc/html/%{name}


%changelog
* Sat May 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.29-1
+ Revision: 799701
- version update 0.9.29

* Sun Mar 04 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.9.28-1
+ Revision: 782083
- Update to 0.9.28
- Remove some obsolete rpm constructs

* Tue Sep 27 2011 Zé <ze@mandriva.org> 0.9.27-1
+ Revision: 701519
- version 0.9.27
- clean useless macros
- avoid use of both buildroot variables
- clean .la files
- remove raptor2 from buildrequires since isnt needed
- require raptor2 bigger than 2.0.4-1 that already requires gtk-doc
- rediff patch0
- clean patch
- version 0.9.27
- clean useless macros
- avoid use of both buildroot variables
- clean .la files
- remove raptor2 from buildrequires since isnt needed
- require raptor2 bigger than 2.0.4-1 that already requires gtk-doc
- rediff patch0

* Thu Aug 11 2011 Funda Wang <fwang@mandriva.org> 0.9.26-1
+ Revision: 693995
- new version 0.9.26

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 0.9.25-2
+ Revision: 662314
- check do no work due to perl problems
- New version 0.9.25

  + Oden Eriksson <oeriksson@mandriva.com>
    - multiarch fixes

* Wed Feb 09 2011 Funda Wang <fwang@mandriva.org> 0.9.24-1
+ Revision: 636981
- new version 0.9.24

* Sun Dec 05 2010 Funda Wang <fwang@mandriva.org> 0.9.21-1mdv2011.0
+ Revision: 609735
- update to new version 0.9.21

* Mon Aug 23 2010 Funda Wang <fwang@mandriva.org> 0.9.20-1mdv2011.0
+ Revision: 572096
- update to new version 0.9.20

* Mon Feb 15 2010 Frederik Himpe <fhimpe@mandriva.org> 0.9.19-1mdv2010.1
+ Revision: 506381
- update to new version 0.9.19

* Mon Feb 15 2010 Funda Wang <fwang@mandriva.org> 0.9.18-1mdv2010.1
+ Revision: 506060
- new version 0.9.18

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.17-2mdv2010.1
+ Revision: 484179
- Update to new version 0.9.17 (new major)
- Fix BuildRequires

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.16-3mdv2010.0
+ Revision: 426876
- rebuild

* Thu Jul 10 2008 Funda Wang <fwang@mandriva.org> 0.9.16-2mdv2009.0
+ Revision: 233242
- new devel package policy
- fix libmajor

* Thu Jul 10 2008 Austin Acton <austin@mandriva.org> 0.9.16-1mdv2009.0
+ Revision: 233216
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9.15-2mdv2009.0
+ Revision: 225311
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 28 2007 Austin Acton <austin@mandriva.org> 0.9.15-1mdv2008.1
+ Revision: 138739
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 10 2007 Austin Acton <austin@mandriva.org> 0.9.14-1mdv2008.0
+ Revision: 25990
- new version

