#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : dogpile.cache
Version  : 1.0.1
Release  : 56
URL      : https://files.pythonhosted.org/packages/8a/d7/89c3115c0420cdea892fe4ed004ee94a9af130f3dcf60d8f55f6b3521a1a/dogpile.cache-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8a/d7/89c3115c0420cdea892fe4ed004ee94a9af130f3dcf60d8f55f6b3521a1a/dogpile.cache-1.0.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/8a/d7/89c3115c0420cdea892fe4ed004ee94a9af130f3dcf60d8f55f6b3521a1a/dogpile.cache-1.0.1.tar.gz.asc
Summary  : A caching front-end based on the Dogpile lock.
Group    : Development/Tools
License  : MIT
Requires: dogpile.cache-license = %{version}-%{release}
Requires: dogpile.cache-python = %{version}-%{release}
Requires: dogpile.cache-python3 = %{version}-%{release}
Requires: decorator
Requires: stevedore
BuildRequires : Mako
BuildRequires : MarkupSafe
BuildRequires : buildreq-distutils3
BuildRequires : decorator
BuildRequires : dogpile.core
BuildRequires : nose-python
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : stevedore
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
Provides: pypi(dogpile.cache)
Requires: pypi(decorator)
Requires: pypi(stevedore)

%description python3
python3 components for the dogpile.cache package.


%prep
%setup -q -n dogpile.cache-1.0.1
cd %{_builddir}/dogpile.cache-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595428650
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dogpile.cache
cp %{_builddir}/dogpile.cache-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/dogpile.cache/36f7c292180b27f76a08c269d3f77cdf8f7da681
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dogpile.cache/36f7c292180b27f76a08c269d3f77cdf8f7da681

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
