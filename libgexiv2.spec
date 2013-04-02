%define major 2
%define libname %mklibname gexiv2_ %major
%define develname %mklibname -d gexiv2

Summary:	A GObject-based wrapper around the Exiv2 library
Name:		libgexiv2
Version:	0.6.1
Release:	1
License:	GPLv2+
Group:		Graphics
Source0:	http://yorba.org/download/gexiv2/0.3/%{name}-%{version}.tar.xz
Url:		http://trac.yorba.org/wiki/gexiv2
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	libtool
BuildRequires:	sed
BuildRequires:  girepository-devel
Patch0:		libgexiv2-0.6.1-link.patch

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %{libname}
Summary:	A GObject-based wrapper around the Exiv2 library
Group:		Graphics

%description -n %{libname}
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %{develname}
Group:		Development/C
Summary:	A GObject-based wrapper around the Exiv2 library
Requires:	pkgconfig(exiv2)
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d -s gexiv2} < 0.3.92-2

%description -n %{develname}
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
sed -i -e 's#libdir=.*#libdir=${exec_prefix}/%{_lib}#' gexiv2.m4

%build
./configure --release --enable-introspection --prefix=%{_prefix}
%make

%install
%makeinstall_std LIB=%{_lib}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/gexiv2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/gexiv2.vapi

%changelog
* Tue May 08 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.92-1
+ Revision: 797352
- version update 0.3.92

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for new pcre

* Sun Oct 09 2011 Andrey Bondrov <abondrov@mandriva.org> 0.3.1-4
+ Revision: 703908
- Update configure and patch1 (add library search path)
- Rebuild
- Fix configure
- New version 0.3.1

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.3.0-2
+ Revision: 640542
- update BR
- rebuild to obsolete old packages

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 0.3.0-1
+ Revision: 634101
- New version 0.3.0

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 0.2.2-1
+ Revision: 634083
- update to new version 0.2.2

* Sun Dec 05 2010 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 609601
- new version 0.2.1

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 0.1.0-2mdv2011.0
+ Revision: 565536
- bump rel
- import libgexiv2

