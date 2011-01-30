%define major 0
%define libname %mklibname gexiv2_ %major
%define develname %mklibname -d gexiv2

Summary:	A GObject-based wrapper around the Exiv2 library
Name:		libgexiv2
Version:	0.2.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphics
Source0:	http://yorba.org/download/gexiv2/0.2/%{name}-%{version}.tar.bz2
Patch0:		libgexiv2-0.1.0-exv2-0.21.patch
Patch1:		libgexiv2-0.2.1-link.patch
Url:		http://trac.yorba.org/wiki/gexiv2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libexiv-devel
BuildRequires:	libglib2.0-devel
BuildRequires:	libtool
BuildRequires:	sed

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
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0
sed -i -e 's#libdir=.*#libdir=${exec_prefix}/%{_lib}#' gexiv2.m4

%build
%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std LIB=%{_lib}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/gexiv2
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/gexiv2.vapi
