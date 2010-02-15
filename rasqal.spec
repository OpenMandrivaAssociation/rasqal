%define name	rasqal
%define version 0.9.19
%define release %mkrel 1

%define major	2
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Name: 	 	%{name}
Summary: 	RDF querying library
Version: 	%{version}
Release: 	%{release}

Source:		http://librdf.org/dist/source/%{name}-%{version}.tar.gz
URL:		http://librdf.org/rasqal/
License:	LGPL
Group:		Databases
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	raptor-devel
BuildRequires:	c-ares-devel
BuildRequires:	libgnutls-devel
BuildRequires:	libmpfr-devel

%description
Rasqal handles Resource Description Framework (RDF) query syntaxes, query
construction and query execution returning result bindings. The supported
query languages are RDQL and SPARQL.  Rasqal was designed to work closely
with the Redland RDF library but is entirely separate. It is intended to be
a portable library working across many POSIX systems (Unix, GNU/Linux,
BSDs, OSX, cygwin) win32 and others.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
Obsoletes:	%{mklibname rasqal 0} >= 0.9.16

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel < %{version}-%{release}
Obsoletes:	%mklibname -d %name 0

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%multiarch_binaries %buildroot/%_bindir/%name-config

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog LICENSE* NEWS* NOTICE README*
%{_bindir}/roqet
%{_mandir}/man1/roqet*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/%name-config
%multiarch %{multiarch_bindir}/%name-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_mandir}/man1/rasqal*
%{_mandir}/man3/lib*
%{_datadir}/gtk-doc/html/%name
