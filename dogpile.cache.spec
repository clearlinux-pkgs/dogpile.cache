#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dogpile.cache
Version  : 0.6.2
Release  : 31
URL      : http://pypi.debian.net/dogpile.cache/dogpile.cache-0.6.2.tar.gz
Source0  : http://pypi.debian.net/dogpile.cache/dogpile.cache-0.6.2.tar.gz
Summary  : A caching front-end based on the Dogpile lock.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dogpile.cache-python
BuildRequires : Mako
BuildRequires : MarkupSafe
BuildRequires : dogpile.core
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-cov-python
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : tox
BuildRequires : virtualenv

%description
dogpile
=======
Dogpile consists of two subsystems, one building on top of the other.

%package python
Summary: python components for the dogpile.cache package.
Group: Default

%description python
python components for the dogpile.cache package.


%prep
%setup -q -n dogpile.cache-0.6.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484545109
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1484545109
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
