#
# spec file for package asio
#

# asio only ships headers, so no debuginfo package is needed

%global debug_package %{nil}

Summary:	A cross-platform C++ library for network and low-level I/O programming
Summary(pl.UTF-8):	Wieloplatformowa biblioteka C++ do programowania sieci i niskopoziomowych operacji we/wy
Name:		asio
Version:	1.26.0
Release:	1
License:	Boost
Group:		Development/Libraries
URL:		https://think-async.com
Source0:	http://downloads.sourceforge.net/asio/%{name}-%{version}.tar.bz2
# Source0-md5:	5eff56aba0f54576f3d5f55b7730281b
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig

%description
Asio is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous
I/O model using a modern C++ approach.

%description -l pl.UTF-8
Asio to międzyplatformowa biblioteka C++ do programowania sieciowego i
niskopoziomowego we/wy, która zapewnia programistom spójny
synchroniczny model we/wy przy użyciu nowoczesnego podejścia C++.

%package devel
Summary:	A cross-platform C++ library for network and low-level I/O programming
Summary(pl.UTF-8):	Wieloplatformowa biblioteka C++ do programowania sieci i niskopoziomowych operacji we/wy
Group:		Development/Libraries
Requires:	boost-devel
Requires:	openssl-devel

%description devel
Header files you can use to develop applications with asio.

Asio is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous
I/O model using a modern C++ approach.

%description -l pl.UTF-8
Header files you can use to develop applications with asio.

Asio to międzyplatformowa biblioteka C++ do programowania sieciowego i
niskopoziomowego we/wy, która zapewnia programistom spójny
synchroniczny model we/wy przy użyciu nowoczesnego podejścia C++.

%prep
%setup -q

%build
autoreconf -fvi
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING LICENSE_1_0.txt
%doc doc/*
%{_includedir}/asio
%{_includedir}/asio.hpp
%{_pkgconfigdir}/asio.pc

%clean
rm -rf $RPM_BUILD_ROOT
