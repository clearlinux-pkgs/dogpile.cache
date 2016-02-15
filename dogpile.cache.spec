#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dogpile.cache
Version  : 0.5.7
Release  : 22
URL      : https://pypi.python.org/packages/source/d/dogpile.cache/dogpile.cache-0.5.7.tar.gz
Source0  : https://pypi.python.org/packages/source/d/dogpile.cache/dogpile.cache-0.5.7.tar.gz
Summary  : A caching front-end based on the Dogpile lock.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dogpile.cache-python
BuildRequires : Mako
BuildRequires : MarkupSafe
BuildRequires : dogpile.core
BuildRequires : funcsigs-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pytest-cov-python
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python

%description
dogpile.cache
=============
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread generates a
new value.

%package python
Summary: python components for the dogpile.cache package.
Group: Default

%description python
python components for the dogpile.cache package.


%prep
%setup -q -n dogpile.cache-0.5.7

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
