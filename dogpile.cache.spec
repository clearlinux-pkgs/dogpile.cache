#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : dogpile.cache
Version  : 0.7.1
Release  : 45
URL      : https://files.pythonhosted.org/packages/84/3e/dbf1cfc5228f1d3dca80ef714db2c5aaec5cd9efaf54d7e3daef6bc48b19/dogpile.cache-0.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/84/3e/dbf1cfc5228f1d3dca80ef714db2c5aaec5cd9efaf54d7e3daef6bc48b19/dogpile.cache-0.7.1.tar.gz
Source99 : https://files.pythonhosted.org/packages/84/3e/dbf1cfc5228f1d3dca80ef714db2c5aaec5cd9efaf54d7e3daef6bc48b19/dogpile.cache-0.7.1.tar.gz.asc
Summary  : A caching front-end based on the Dogpile lock.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dogpile.cache-license = %{version}-%{release}
Requires: dogpile.cache-python = %{version}-%{release}
Requires: dogpile.cache-python3 = %{version}-%{release}
Requires: decorator
BuildRequires : Mako
BuildRequires : MarkupSafe
BuildRequires : buildreq-distutils3
BuildRequires : decorator
BuildRequires : dogpile.core
BuildRequires : nose-python
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-cov
BuildRequires : pytest-cov-python
BuildRequires : python-mock
BuildRequires : tox
BuildRequires : virtualenv

%description
Individual per-changelog files go here in .rst format, which are pulled in by
changelog (version 0.4.0 or higher) to be rendered into the changelog.rst file.
At release time, the files here are removed and written directly into the
changelog.

%package license
Summary: license components for the dogpile.cache package.
Group: Default

%description license
license components for the dogpile.cache package.


%package python
Summary: python components for the dogpile.cache package.
Group: Default
Requires: dogpile.cache-python3 = %{version}-%{release}

%description python
python components for the dogpile.cache package.


%package python3
Summary: python3 components for the dogpile.cache package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dogpile.cache package.


%prep
%setup -q -n dogpile.cache-0.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551028806
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dogpile.cache
cp LICENSE %{buildroot}/usr/share/package-licenses/dogpile.cache/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dogpile.cache/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
