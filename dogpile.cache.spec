#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : dogpile.cache
Version  : 0.6.8
Release  : 39
URL      : https://files.pythonhosted.org/packages/73/bf/0cbed594e4f0f9360bfb98e7276131bf32e1af1d15e6c11a9dd8bd93a12f/dogpile.cache-0.6.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/73/bf/0cbed594e4f0f9360bfb98e7276131bf32e1af1d15e6c11a9dd8bd93a12f/dogpile.cache-0.6.8.tar.gz
Source99 : https://files.pythonhosted.org/packages/73/bf/0cbed594e4f0f9360bfb98e7276131bf32e1af1d15e6c11a9dd8bd93a12f/dogpile.cache-0.6.8.tar.gz.asc
Summary  : A caching front-end based on the Dogpile lock.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dogpile.cache-license = %{version}-%{release}
Requires: dogpile.cache-python = %{version}-%{release}
Requires: dogpile.cache-python3 = %{version}-%{release}
Requires: Sphinx
BuildRequires : Mako
BuildRequires : MarkupSafe
BuildRequires : buildreq-distutils3
BuildRequires : dogpile.core
BuildRequires : nose-python
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : tox
BuildRequires : virtualenv

%description
=======
        
        Dogpile consists of two subsystems, one building on top of the other.
        
        ``dogpile`` provides the concept of a "dogpile lock", a control structure
        which allows a single thread of execution to be selected as the "creator" of
        some resource, while allowing other threads of execution to refer to the previous
        version of this resource as the creation proceeds; if there is no previous
        version, then those threads block until the object is available.
        
        ``dogpile.cache`` is a caching API which provides a generic interface to
        caching backends of any variety, and additionally provides API hooks which
        integrate these cache backends with the locking mechanism of ``dogpile``.
        
        Overall, dogpile.cache is intended as a replacement to the `Beaker

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
%setup -q -n dogpile.cache-0.6.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543135857
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
