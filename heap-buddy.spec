#
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
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
Obsoletes:	heap-buddy-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heap-buddy is a heap profiler for mono. It attaches to special hooks
in the mono runtime and tracks all of the managed memory allocations,
every garbage collection and every heap resize.

%description -l pl.UTF-8
Heap-buddy jest profilerem sterty dla mono. Dołącza się do specjalnych
haków w środowisku uruchomieniowym mono i śledzi wszystkie alokacje
zarządzanej pamięci, każde odśmiecanie oraz zmianę rozmiaru sterty.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# mono dlopens profiler library by libmono-profiler-NAME.so
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/heap-buddy
%attr(755,root,root) %{_libdir}/libmono-profiler-heap-buddy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmono-profiler-heap-buddy.so.0
%attr(755,root,root) %{_libdir}/libmono-profiler-heap-buddy.so
%{_prefix}/lib/%{name}
