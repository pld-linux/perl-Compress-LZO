%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	LZO
Summary:	Compress::LZO Perl module - interface to LZO compression library
Summary(pl):	Modu³ Perla Compress::LZO - interfejs do biblioteki kompresji LZO
Name:		perl-Compress-LZO
Version:	1.00
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	lzo-devel >= 1.03
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory. perl-LZO provides LZO bindings for
Perl - i.e. you can access the LZO library from your Perl scripts
thereby compressing ordinary Perl strings.

%description -l pl
LZO jest przeno¶n± bibliotek± do bezstratnej kompresji danych,
napisan± w ANSI C. Oferuje szybk± kompresjê i bardzo szybk±, nie
wymagaj±c± pamiêci, dekompresjê. perl-LZO udostêpnia interfejs dla
Perla - pozwalaj±cy na dostêp do biblioteki LZO ze skryptów perlowych,
do kompresji zwyk³ych ³añcuchów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{perl_sitearch}/Compress/LZO.pm
%dir %{perl_sitearch}/auto/Compress/LZO
%{perl_sitearch}/auto/Compress/LZO/autosplit.ix
%{perl_sitearch}/auto/Compress/LZO/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Compress/LZO/*.so
%{_mandir}/man3/*
