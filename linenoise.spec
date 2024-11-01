%define	git_rev 7946e2c
%define	rel	3
Summary:	Minimal replacement for readline
Summary(pl.UTF-8):	Minimalny zamiennik readline
Name:		linenoise
Version:	0
Release:	0.git%{git_rev}.%{rel}
# The licenses are a bit of a mess here...
# utf8.{c,h} contain incomplete license headers. They refer to a "LICENSE" file
# which is actually from jimtcl. A copy is committed in dist-git as
# jimtcl-LICENSE, retrieved from
# <https://raw.github.com/msteveb/jimtcl/master/LICENSE>. I received a mail
# from the author, committed as steve-bennett-license-confirmation, confirming
# that that is indeed the LICENSE file referred to and therefore utf8.{c,h} are
# under a BSD-like license.
# linenoise.{c,h} contain complete BSD-like license headers so they are fine.
# And it means the whole library is definitely under a BSD-like license.
# But there is no separate license file shipped in the tarball. I queried Tad
# Marshall on 2013-01-10 to include one but never received a reply. So
# I synthesized one as Source1.
License:	BSD
Group:		Libraries
Source0:	https://github.com/tadmarshall/linenoise/tarball/%{git_rev}/%{name}-%{git_rev}.tar.gz
# Source0-md5:	7cb42d58db11bf3c33b8dd698ec92754
Patch0:		%{name}-build-shared-lib.patch
Patch1:		%{name}-symbol-visibility.patch
URL:		https://github.com/tadmarshall/linenoise
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linenoise is a replacement for the readline line-editing library with
the goal of being smaller.

%description -l pl.UTF-8
Linenoise to zamiennik biblioteki edycji linii readline, mający na
celu mniejszy rozmiar.

%package devel
Summary:	Development files for linenoise library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki linenoise
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains files needed for developing software that uses
linenoise library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do tworzenia oprogramowania
wykorzystującego bibliotekę linenoise.

%prep
%setup -q -n tadmarshall-%{name}-%{git_rev}
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{rpmcflags}"
%{__make} \
	CC="%{__cc}" \
	LIBDIR="%{_libdir}" \
	INCLUDEDIR="%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT

export CFLAGS="%{rpmcflags}"
%{__make} install \
	LIBDIR="%{_libdir}" \
	INCLUDEDIR="%{_includedir}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.markdown
%attr(755,root,root) %{_libdir}/liblinenoise.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liblinenoise.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/liblinenoise.so
%{_includedir}/linenoise.h
