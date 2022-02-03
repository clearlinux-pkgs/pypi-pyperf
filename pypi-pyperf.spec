#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyperf
Version  : 2.3.1
Release  : 24
URL      : https://files.pythonhosted.org/packages/d6/4d/a1bc52b347c6bc63adcfe162ebb27948d36dc754e330c4032122a94b215d/pyperf-2.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/4d/a1bc52b347c6bc63adcfe162ebb27948d36dc754e330c4032122a94b215d/pyperf-2.3.1.tar.gz
Summary  : Python module to run and analyze benchmarks
Group    : Development/Tools
License  : MIT
Requires: pypi-pyperf-bin = %{version}-%{release}
Requires: pypi-pyperf-license = %{version}-%{release}
Requires: pypi-pyperf-python = %{version}-%{release}
Requires: pypi-pyperf-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
******
pyperf
******
.. image:: https://img.shields.io/pypi/v/pyperf.svg
:alt: Latest release on the Python Cheeseshop (PyPI)
:target: https://pypi.python.org/pypi/pyperf

%package bin
Summary: bin components for the pypi-pyperf package.
Group: Binaries
Requires: pypi-pyperf-license = %{version}-%{release}

%description bin
bin components for the pypi-pyperf package.


%package license
Summary: license components for the pypi-pyperf package.
Group: Default

%description license
license components for the pypi-pyperf package.


%package python
Summary: python components for the pypi-pyperf package.
Group: Default
Requires: pypi-pyperf-python3 = %{version}-%{release}

%description python
python components for the pypi-pyperf package.


%package python3
Summary: python3 components for the pypi-pyperf package.
Group: Default
Requires: python3-core
Provides: pypi(pyperf)

%description python3
python3 components for the pypi-pyperf package.


%prep
%setup -q -n pyperf-2.3.1
cd %{_builddir}/pyperf-2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643907136
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyperf
cp %{_builddir}/pyperf-2.3.1/COPYING %{buildroot}/usr/share/package-licenses/pypi-pyperf/0c885fb5d06bf65019b498d9cef9641983dd58ad
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyperf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyperf/0c885fb5d06bf65019b498d9cef9641983dd58ad

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
