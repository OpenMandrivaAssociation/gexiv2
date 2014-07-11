%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	0.4
%define major	2
%define libname %mklibname gexiv2_ %{major}
%define girname %mklibname gexiv2-gir %{api}
%define devname %mklibname -d gexiv2

Summary:	A GObject-based wrapper around the Exiv2 library
Name:		libgexiv2
Version:	0.6.1
Release:	8
License:	GPLv2+
Group:		Graphics
Url:		http://trac.yorba.org/wiki/gexiv2
Source0:	http://yorba.org/download/gexiv2/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		libgexiv2-0.6.1-link.patch

BuildRequires:	libtool
BuildRequires:	sed
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %{libname}
Summary:	A GObject-based wrapper around the Exiv2 library
Group:		Graphics

%description -n %{libname}
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gexiv2_2 < 0.6.1-2

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	A GObject-based wrapper around the Exiv2 library
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d -s gexiv2} < 0.3.92-2

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches
sed -i -e 's#libdir=.*#libdir=${exec_prefix}/%{_lib}#' gexiv2.m4

%build
./configure \
	--release \
	--enable-introspection \
	--prefix=%{_prefix}
%make

%install
%makeinstall_std LIB=%{_lib}

%files -n %{libname}
%{_libdir}/libgexiv2.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GExiv2-%{api}.typelib

%files -n %{devname}
%{_includedir}/gexiv2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/gexiv2.vapi
%{_datadir}/gir-1.0/GExiv2-%{api}.gir

