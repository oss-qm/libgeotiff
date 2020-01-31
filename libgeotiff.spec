Name:		libgeotiff
Version:	1.6.0
Release:	mtx.5%{?dist}
Summary:	GeoTIFF format library
License:	MIT
URL:		http://trac.osgeo.org/geotiff/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	proj-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
GeoTIFF represents an effort by over 160 different remote sensing,
GIS, cartographic, and surveying related companies and organizations
to establish a TIFF based interchange format for georeferenced
raster imagery.

%package devel
Summary:	Development Libraries for the GeoTIFF file format library
Requires:	pkgconfig libtiff-devel
Requires:	%{name} = %{version}-%{release}
Requires:	proj-devel

%description devel
The GeoTIFF library provides support for development of geotiff image format.

%prep
%setup -q -n %{name}-%{version}

%build

pushd libgeotiff

autoreconf -fi
./configure \
	--prefix=%{_prefix}		\
	--sysconfdir=%{_sysconfdir}	\
	--libdir=%{_libdir}		\
	--mandir=%{_mandir}		\
	--bindir=%{_bindir}		\
	--with-proj			\
	--with-jpeg			\
	--with-zip

%{__make} %{?_smp_mflags}

popd

%install
pushd libgeotiff
%{__make} install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
popd

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc libgeotiff/ChangeLog libgeotiff/LICENSE libgeotiff/README
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*.1.gz

%files devel
%dir %{_includedir}
%attr(0644,root,root) %{_includedir}/*.h
%attr(0644,root,root) %{_includedir}/*.inc
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Thu Feb 6 2020 Enrico Weigelt, metux IT consult <info@metux.net> - 1.5.1-3
- Rebased onto upstream and refactored specfile
