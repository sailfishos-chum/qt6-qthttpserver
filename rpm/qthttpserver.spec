%global  qt_version 6.7.2

Name:       qt6-qthttpserver
Version: 6.7.2
Release:    0%{?dist}
Summary:    Library to facilitate the creation of an http server with Qt
License:    BSD-3-Clause AND GFDL-1.3-no-invariants-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:        http://qt-project.org/
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  ninja
BuildRequires:  libxkbcommon-devel
BuildRequires:  qt6-qtwebsockets-devel >= %{qt_version}
BuildRequires:  qt6-qtbase-devel >= %{qt_version}
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires:  qt6-qtdeclarative-devel >= %{qt_version}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=OFF\
  -DQT_INSTALL_EXAMPLES_SOURCES=OFF

%cmake_build


%install
%cmake_install

%files
%license LICENSES/*.txt
%{_qt6_libdir}/libQt6HttpServer.so.6{,.*}

%files devel
%dir %{_qt6_headerdir}/QtHttpServer
%{_qt6_headerdir}/QtHttpServer/*
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtHttpServerTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6HttpServer
%{_qt6_libdir}/cmake/Qt6HttpServer/*
%{_qt6_libdir}/libQt6HttpServer.prl
%{_qt6_libdir}/libQt6HttpServer.so
%{_qt6_libdir}/pkgconfig/Qt6HttpServer.pc
%{_qt6_libdir}/qt6/metatypes/qt6httpserver_relwithdebinfo_metatypes.json
%{_qt6_libdir}/qt6/mkspecs/modules/qt_lib_httpserver.pri
%{_qt6_libdir}/qt6/mkspecs/modules/qt_lib_httpserver_private.pri
%{_qt6_libdir}/qt6/modules/HttpServer.json
