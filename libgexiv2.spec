%define major 0
%define libname %mklibname gexiv2_ %major
%define develname %mklibname -d gexiv2
%define develnamest %mklibname -d -s gexiv2

Summary:	A GObject-based wrapper around the Exiv2 library
Name:		libgexiv2
Version:	0.3.92
Release:	1
License:	GPLv2+
Group:		Graphics
Source0:	http://yorba.org/download/gexiv2/0.3/%{name}-%{version}.tar.bz2
Url:		http://trac.yorba.org/wiki/gexiv2
BuildRequires:	libexiv-devel >= 0.21
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	sed
Patch0:		libgexiv2-0.2.1-link.patch

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %libname
Summary: A GObject-based wrapper around the Exiv2 library
Group: Graphics

%description -n %libname
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %develname
Group: Development/C
Summary: A GObject-based wrapper around the Exiv2 library
Requires: libexiv-devel  >= 0.21
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.



%package -n %develnamest
Group: Development/C
Summary: A GObject-based wrapper around the Exiv2 library
Requires: libexiv-devel  >= 0.21
Requires: %libname = %version-%release
Provides: %name-devel-static = %version-%release

%description -n %develnamest
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.



%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
sed -i -e 's#libdir=.*#libdir=${exec_prefix}/%{_lib}#' gexiv2.m4

%build
%configure2_5x
%make

%install
%makeinstall_std LIB=%{_lib}
rm -fr %buildroot%{_libdir}/*.la

%files -n %libname
%{_libdir}/*.so.%{major}*

%files -n %develname
%{_includedir}/gexiv2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/gexiv2.vapi

%files -n %develnamest
%{_libdir}/*.a
