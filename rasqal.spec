%define major	3
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}
# Disabled by default because dawg-triple-pattern fails when running
# inside ABF (works fine locally though).
# Please run a --with-testsuite build when modifying the package.
%bcond_with testsuite

Summary:	RDF querying library
Name:		rasqal
Group:		Databases
Version:	0.9.32
Release:	2
License:	LGPLv2
Url:		http://librdf.org/rasqal/
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
Patch0:		rasqal-0.9.28-linkm.patch
# For the "rapper" tool
BuildRequires:	raptor2 >= 2.0.9
BuildRequires:	mpfr-devel
BuildRequires:	pkgconfig(raptor2) >= 2.0.9

%description
Rasqal handles Resource Description Framework (RDF) query syntaxes, query
construction and query execution returning result bindings. The supported
query languages are RDQL and SPARQL.  Rasqal was designed to work closely
with the Redland RDF library but is entirely separate. It is intended to be
a portable library working across many POSIX systems (Unix, GNU/Linux,
BSDs, OSX, cygwin) win32 and others.

%package -n 	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{devname}
Summary:	Header files and development libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%track
prog %{name} = {
	url = http://librdf.org/rasqal/
	regex = "Latest version: (__VER__) \("
	version = %{version}
}

%prep
%setup -q
%apply_patches

%build
%configure2_5x --disable-static
%make
										
%install
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
%{_libdir}/librasqal.so.%{major}*

%files -n %{devname}
%{_bindir}/%{name}-config
%{multiarch_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/rasqal*
%{_mandir}/man3/lib*
%doc %{_datadir}/gtk-doc/html/%{name}

