%define major	3
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}
# Disabled by default because dawg-triple-pattern fails when running
# inside ABF (works fine locally though).
# Please run a --with-testsuite build when modifying the package.
%bcond_with testsuite

Name: 	 	rasqal
Summary: 	RDF querying library
Group:		Databases
Version: 	0.9.31
Release: 	1
License:	LGPL
URL:		http://librdf.org/rasqal/
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
Patch0:		rasqal-0.9.28-linkm.patch
BuildRequires:	pkgconfig(raptor2) >= 2.0.9
# For the "rapper" tool
BuildRequires:	raptor2 >= 2.0.9
BuildRequires:	mpfr-devel

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

%track
prog %name = {
	url = http://librdf.org/rasqal/
	regex = "Latest version: (__VER__) \("
	version = %version
}

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

%if %{with testsuite}
%check
make check
%endif

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
%doc %{_datadir}/gtk-doc/html/%{name}
