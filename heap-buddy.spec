#
%include        /usr/lib/rpm/macros.mono
#
Summary:	A heap profiler for mono
Summary(pl.UTF-8):	Profiler sterty dla mono
Name:		heap-buddy
Version:	0.2
Release:	0.1
License:	MIT
Group:		Development/Tools
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/heap-buddy/%{name}-%{version}.tar.gz
# Source0-md5:	619981c2596aec70eda6069489e6392b
URL:		http://www.mono-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heap-buddy is a heap profiler for mono. It attaches to special hooks
in the mono runtime and tracks all of the managed memory allocations,
every garbage collection and every heap resize.

%description -l pl.UTF-8
Heap-buddy jest profilerem sterty dla mono. Dołącza się do specjalnych
haków w środowisku uruchomieniowym mono i śledzi wszystkie alokacje
zarządzanej pamięci, każde odśmiecanie oraz zmianę rozmiaru sterty.

%package static
Summary:	Static heap-buddy library
Summary(pl.UTF-8):	Statyczna biblioteka heap-buddy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static heap-buddy library.

%description static -l pl.UTF-8
Statyczna biblioteka heap-buddy

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/%{name}
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
