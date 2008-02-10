#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	LZO
Summary:	Compress::LZO Perl module - interface to LZO compression library
Summary(pl.UTF-8):	Moduł Perla Compress::LZO - interfejs do biblioteki kompresji LZO
Name:		perl-Compress-LZO
Version:	1.08
Release:	5
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Compress/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4266ea0cb23817dd02ead4f983c2604f
Patch0:		%{name}-lzo2.patch
URL:		http://search.cpan.org/dist/Compress-LZO/
BuildRequires:	lzo-devel >= 2.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory. perl-LZO provides LZO bindings for
Perl - i.e. you can access the LZO library from your Perl scripts
thereby compressing ordinary Perl strings.

%description -l pl.UTF-8
LZO jest przenośną biblioteką do bezstratnej kompresji danych,
napisaną w ANSI C. Oferuje szybką kompresję i bardzo szybką, nie
wymagającą pamięci, dekompresję. perl-LZO udostępnia interfejs dla
Perla - pozwalający na dostęp do biblioteki LZO ze skryptów perlowych,
do kompresji zwykłych łańcuchów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{perl_vendorarch}/Compress/LZO.pm
%dir %{perl_vendorarch}/auto/Compress/LZO
%{perl_vendorarch}/auto/Compress/LZO/autosplit.ix
%{perl_vendorarch}/auto/Compress/LZO/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/LZO/*.so
%{_mandir}/man3/*
