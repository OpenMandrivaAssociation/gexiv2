%define major 0
%define libname %mklibname gexiv2_ %{major}
%define develname %mklibname -d gexiv2

Summary:	A GObject-based wrapper around the Exiv2 library
Name:		libgexiv2
Version:	0.3.1
Release:	%mkrel 4
License:	GPLv2+
Group:		Graphics
Source0:	http://yorba.org/download/gexiv2/0.3/%{name}-%{version}.tar.bz2
Patch1:		libgexiv2-0.2.1-link.patch
Url:		http://trac.yorba.org/wiki/gexiv2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libexiv-devel >= 0.21
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	sed

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %{libname}
Summary: A GObject-based wrapper around the Exiv2 library
Group: Graphics

%description -n %{libname}
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %{develname}
Group: Development/C
Summary: A GObject-based wrapper around the Exiv2 library
Requires:	%{libname} = %{version}-%{release}
Requires:	libexiv-devel >= 0.21
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p0
sed -i -e 's#libdir=.*#libdir=${exec_prefix}/%{_lib}#' gexiv2.m4

%build
./configure --prefix=%{prefix} LIB=%{_lib}
%make

%install
rm -rf %{buildroot}
%makeinstall_std LIB=%{_lib}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/gexiv2
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/gexiv2.vapi
