#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-openzwave
Version  : 0.4.19
Release  : 30
URL      : https://github.com/OpenZWave/python-openzwave/archive/v0.4.19/python-openzwave-0.4.19.tar.gz
Source0  : https://github.com/OpenZWave/python-openzwave/archive/v0.4.19/python-openzwave-0.4.19.tar.gz
Source1  : https://raw.githubusercontent.com/OpenZWave/python-openzwave/master/archives/open-zwave-master-0.4.9.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 ISC LGPL-3.0
Requires: python-openzwave-bin = %{version}-%{release}
Requires: python-openzwave-license = %{version}-%{release}
Requires: python-openzwave-python = %{version}-%{release}
Requires: python-openzwave-python3 = %{version}-%{release}
Requires: Cython
Requires: PyDispatcher
Requires: pyserial
Requires: six
BuildRequires : Cython
BuildRequires : Cython-python
BuildRequires : PyDispatcher
BuildRequires : buildreq-distutils3
BuildRequires : libopenzwave-dev
BuildRequires : pip
BuildRequires : pyserial
BuildRequires : six
Patch1: 0001-Relax-Cython-version-pinning.patch

%description
.. image:: https://travis-ci.org/OpenZWave/python-openzwave.svg?branch=master
:target: https://travis-ci.org/OpenZWave/python-openzwave
:alt: Travis status

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
%setup -q -n python-openzwave-0.4.19
cd %{_builddir}
unzip -q %{_sourcedir}/open-zwave-master-0.4.9.zip
cd %{_builddir}/python-openzwave-0.4.19
mkdir -p openzwave-embed/open-zwave-master
cp -r %{_builddir}/open-zwave-master/* %{_builddir}/python-openzwave-0.4.19/openzwave-embed/open-zwave-master
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590866651
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-openzwave
cp %{_builddir}/open-zwave-master/cpp/hidapi/LICENSE-bsd.txt %{buildroot}/usr/share/package-licenses/python-openzwave/7dde42b4c6fdafae722d8d07556b6d9dba4d2963
cp %{_builddir}/open-zwave-master/cpp/hidapi/LICENSE-gpl3.txt %{buildroot}/usr/share/package-licenses/python-openzwave/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/open-zwave-master/cpp/hidapi/LICENSE-orig.txt %{buildroot}/usr/share/package-licenses/python-openzwave/66047dbcf3fd689c99472266f5ad141c53d6f2c6
cp %{_builddir}/open-zwave-master/cpp/hidapi/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-openzwave/07ee706ea70d84685d8ee57557052a7ab00c960a
cp %{_builddir}/open-zwave-master/debian/copyright %{buildroot}/usr/share/package-licenses/python-openzwave/c9cb6e1003d94c0123949178f34321343e9115a6
cp %{_builddir}/open-zwave-master/license/gpl.txt %{buildroot}/usr/share/package-licenses/python-openzwave/2a0d409439280c8cfc806f890b757d9bd8a19a09
cp %{_builddir}/open-zwave-master/license/license.txt %{buildroot}/usr/share/package-licenses/python-openzwave/2b26df014bec35b26b16f333522989336e24e488
cp %{_builddir}/python-openzwave-0.4.19/COPYRIGHT.txt %{buildroot}/usr/share/package-licenses/python-openzwave/f0cb7c2c2db59bd17a620fd5070dffe7aa8acdb6
cp %{_builddir}/python-openzwave-0.4.19/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-openzwave/f0cb7c2c2db59bd17a620fd5070dffe7aa8acdb6
cp %{_builddir}/python-openzwave-0.4.19/debian/copyright %{buildroot}/usr/share/package-licenses/python-openzwave/215fd18143ce0317e4e689997e898cfbc9b68196
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
/usr/share/package-licenses/python-openzwave/07ee706ea70d84685d8ee57557052a7ab00c960a
/usr/share/package-licenses/python-openzwave/215fd18143ce0317e4e689997e898cfbc9b68196
/usr/share/package-licenses/python-openzwave/2a0d409439280c8cfc806f890b757d9bd8a19a09
/usr/share/package-licenses/python-openzwave/2b26df014bec35b26b16f333522989336e24e488
/usr/share/package-licenses/python-openzwave/66047dbcf3fd689c99472266f5ad141c53d6f2c6
/usr/share/package-licenses/python-openzwave/7dde42b4c6fdafae722d8d07556b6d9dba4d2963
/usr/share/package-licenses/python-openzwave/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/python-openzwave/c9cb6e1003d94c0123949178f34321343e9115a6
/usr/share/package-licenses/python-openzwave/f0cb7c2c2db59bd17a620fd5070dffe7aa8acdb6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
