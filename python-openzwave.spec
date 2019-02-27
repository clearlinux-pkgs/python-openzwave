#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-openzwave
Version  : 1
Release  : 8
URL      : https://github.com/home-assistant/python-openzwave/archive/v0.1.2.zip
Source0  : https://github.com/home-assistant/python-openzwave/archive/v0.1.2.zip
Source1  : https://raw.githubusercontent.com/OpenZWave/python-openzwave/master/archives/open-zwave-master-0.4.9.zip
Summary  : Library to access Z-Wave interfaces
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 ISC LGPL-2.0+ LGPL-2.1+ LGPL-3.0
Requires: python-openzwave-bin = %{version}-%{release}
Requires: python-openzwave-license = %{version}-%{release}
Requires: python-openzwave-python = %{version}-%{release}
Requires: python-openzwave-python3 = %{version}-%{release}
Requires: Cython
Requires: PyDispatcher
Requires: six
BuildRequires : Cython
BuildRequires : PyDispatcher
BuildRequires : buildreq-distutils3
BuildRequires : libopenzwave-dev
BuildRequires : pip
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)

%description
OpenZWave is an open-source, cross-platform library designed to enable anyone to
add support for Z-Wave home-automation devices to their applications, without 
requiring any in depth knowledge of the Z-Wave protocol.

Z-Wave employs a proprietary protocol which the owners, Sigma Designs, have 
chosen not to release into the public domain. There is also no official free 
or low-cost SDK that can be used to develop applications (The ControlThink SDK
is now tied exclusively to their own Z-Wave PC interface). The only way to 
obtain the protocol documentation and sample code is to purchase an expensive 
development kit, and sign a non-disclosure agreement (NDA) preventing the 
release of that knowledge.

OpenZWave was created to fill that gap. We do not have the official 
documentation, have signed no NDA, and are free to develop the library as we 
see fit. Our knowledge comes from existing bodies of open-source code 
(principally the Z-Wave parts of LinuxMCE), and through examining the 
messages sent by Z-Wave devices.

The goal of the project is to make a positive contribution to the Z-Wave 
community by creating a library that supports as much of the Z-Wave 
specification as possible, and that can be used as a "black-box" solution 
by anyone wanting to add Z-Wave to their application. It is NOT our aim 
to publish alternative documentation of the Z-Wave protocol, or to 
attempt to "punish" Sigma Designs for their decision to keep the 
protocol closed.

%package bin
Summary: bin components for the python-openzwave package.
Group: Binaries
Requires: python-openzwave-license = %{version}-%{release}

%description bin
bin components for the python-openzwave package.


%package license
Summary: license components for the python-openzwave package.
Group: Default

%description license
license components for the python-openzwave package.


%package python
Summary: python components for the python-openzwave package.
Group: Default
Requires: python-openzwave-python3 = %{version}-%{release}

%description python
python components for the python-openzwave package.


%package python3
Summary: python3 components for the python-openzwave package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-openzwave package.


%prep
%setup -q -n python-openzwave-0.1.2
cd ..
%setup -q -T -D -n python-openzwave-0.1.2 -b 1
mkdir -p openzwave-embed/open-zwave-master
cp -r %{_topdir}/BUILD/open-zwave-master/* %{_topdir}/BUILD/python-openzwave-0.1.2/openzwave-embed/open-zwave-master

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551303815
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-openzwave
cp COPYRIGHT.txt %{buildroot}/usr/share/package-licenses/python-openzwave/COPYRIGHT.txt
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/python-openzwave/LICENSE.txt
cp debian/copyright %{buildroot}/usr/share/package-licenses/python-openzwave/debian_copyright
cp openzwave-embed/open-zwave-master/cpp/hidapi/LICENSE-bsd.txt %{buildroot}/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_cpp_hidapi_LICENSE-bsd.txt
cp openzwave-embed/open-zwave-master/cpp/hidapi/LICENSE-gpl3.txt %{buildroot}/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_cpp_hidapi_LICENSE-gpl3.txt
cp openzwave-embed/open-zwave-master/cpp/hidapi/LICENSE-orig.txt %{buildroot}/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_cpp_hidapi_LICENSE-orig.txt
cp openzwave-embed/open-zwave-master/cpp/hidapi/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_cpp_hidapi_LICENSE.txt
cp openzwave-embed/open-zwave-master/debian/copyright %{buildroot}/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_debian_copyright
cp openzwave-embed/open-zwave-master/license/gpl.txt %{buildroot}/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_license_gpl.txt
cp openzwave-embed/open-zwave-master/license/license.txt %{buildroot}/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_license_license.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyozw_check
/usr/bin/pyozw_shell

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-openzwave/COPYRIGHT.txt
/usr/share/package-licenses/python-openzwave/LICENSE.txt
/usr/share/package-licenses/python-openzwave/debian_copyright
/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_cpp_hidapi_LICENSE-bsd.txt
/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_cpp_hidapi_LICENSE-gpl3.txt
/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_cpp_hidapi_LICENSE-orig.txt
/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_cpp_hidapi_LICENSE.txt
/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_debian_copyright
/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_license_gpl.txt
/usr/share/package-licenses/python-openzwave/openzwave-embed_open-zwave-master_license_license.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
