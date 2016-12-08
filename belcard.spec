%define oname Belcard
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Belledonne Communications' vCards and CardDAV library
Name:		belcard
Version:	1.0.0
Release:	1
License:	GPLv3+
Group:		Communications
URL:		https://github.com/BelledonneCommunications/%{name}
Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	cmake(BcToolbox)
BuildRequires:	cmake(Belr)
BuildRequires:	pkgconfig(libudev)

%description
Belledonne Communications' vCards library.

%files
%{_bindir}/%{name}*
%doc COPYING

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Belledonne Communications' vCards and CardDAV library
Group:		System/Libraries

%description -n	%{libname}
Belledonne Communications' vCards library.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*
%doc COPYING

#--------------------------------------------------------------------

%package -n	%{devname}
Summary:	Headers, libraries and docs for the %{oname} library
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains header files and development libraries needed to
develop programs using the %{oname} library.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
#%{_libdir}/pkgconfig/lib%{name}.pc
%{_datadir}/%{oname}/cmake/
#doc README
%doc NEWS
%doc AUTHORS
#doc ChangeLog
%doc COPYING

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Debug \
	-DENABLE_SHARED:BOOL=ON \
	-DENABLE_STATIC:BOOL=OFF \
	-DENABLE_TESTS:BOOL=OFF
%make

%install
%makeinstall_std -C build

