#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dogpile.cache
Version  : 0.6.6
Release  : 35
URL      : https://files.pythonhosted.org/packages/48/ca/604154d835c3668efb8a31bd979b0ea4bf39c2934a40ffecc0662296cb51/dogpile.cache-0.6.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/48/ca/604154d835c3668efb8a31bd979b0ea4bf39c2934a40ffecc0662296cb51/dogpile.cache-0.6.6.tar.gz
Summary  : A caching front-end based on the Dogpile lock.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dogpile.cache-python3
Requires: dogpile.cache-license
Requires: dogpile.cache-python
Requires: Sphinx
BuildRequires : Mako
BuildRequires : MarkupSafe
BuildRequires : buildreq-distutils3
BuildRequires : dogpile.core
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
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
Requires: dogpile.cache-python3

%description python
python components for the dogpile.cache package.


%package python3
Summary: python3 components for the dogpile.cache package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dogpile.cache package.


%prep
%setup -q -n dogpile.cache-0.6.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532241186
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/dogpile.cache
cp LICENSE %{buildroot}/usr/share/doc/dogpile.cache/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/dogpile.cache/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
