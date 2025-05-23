#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v25
# autospec commit: 9594167
#
Name     : minizip-ng
Version  : 4.0.10
Release  : 3
URL      : https://github.com/zlib-ng/minizip-ng/archive/4.0.10/minizip-ng-4.0.10.tar.gz
Source0  : https://github.com/zlib-ng/minizip-ng/archive/4.0.10/minizip-ng-4.0.10.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Zlib
Requires: minizip-ng-lib = %{version}-%{release}
Requires: minizip-ng-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libbsd-overlay)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(openssl)
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# minizip-ng
minizip-ng is a zip manipulation library written in C that is supported on Windows, macOS, and Linux.

%package dev
Summary: dev components for the minizip-ng package.
Group: Development
Requires: minizip-ng-lib = %{version}-%{release}
Provides: minizip-ng-devel = %{version}-%{release}
Requires: minizip-ng = %{version}-%{release}

%description dev
dev components for the minizip-ng package.


%package lib
Summary: lib components for the minizip-ng package.
Group: Libraries
Requires: minizip-ng-license = %{version}-%{release}

%description lib
lib components for the minizip-ng package.


%package license
Summary: license components for the minizip-ng package.
Group: Default

%description license
license components for the minizip-ng package.


%prep
%setup -q -n minizip-ng-4.0.10
cd %{_builddir}/minizip-ng-4.0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1746455205
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1746455205
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/minizip-ng
cp %{_builddir}/minizip-ng-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/minizip-ng/17a2d397e441ba04378b9b47274bb487adf66c44 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/minizip/ioapi.h
/usr/include/minizip/mz.h
/usr/include/minizip/mz_crypt.h
/usr/include/minizip/mz_os.h
/usr/include/minizip/mz_strm.h
/usr/include/minizip/mz_strm_buf.h
/usr/include/minizip/mz_strm_bzip.h
/usr/include/minizip/mz_strm_lzma.h
/usr/include/minizip/mz_strm_mem.h
/usr/include/minizip/mz_strm_os.h
/usr/include/minizip/mz_strm_pkcrypt.h
/usr/include/minizip/mz_strm_split.h
/usr/include/minizip/mz_strm_wzaes.h
/usr/include/minizip/mz_strm_zlib.h
/usr/include/minizip/mz_strm_zstd.h
/usr/include/minizip/mz_zip.h
/usr/include/minizip/mz_zip_rw.h
/usr/include/minizip/unzip.h
/usr/include/minizip/zip.h
/usr/lib64/cmake/minizip/minizip-config-version.cmake
/usr/lib64/cmake/minizip/minizip-config.cmake
/usr/lib64/cmake/minizip/minizip-relwithdebinfo.cmake
/usr/lib64/cmake/minizip/minizip.cmake
/usr/lib64/libminizip.so
/usr/lib64/pkgconfig/minizip.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libminizip.so.1
/usr/lib64/libminizip.so.4.0.10

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/minizip-ng/17a2d397e441ba04378b9b47274bb487adf66c44
