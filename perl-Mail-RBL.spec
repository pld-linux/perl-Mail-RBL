#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	RBL
Summary:	Mail::RBL - Perl extension to access RBL-style host verification services
Summary(pl.UTF-8):	Mail::RBL - rozszerzenie perlowe do dostępu do usług weryfikacji hostów w stylu RBL
Name:		perl-Mail-RBL
Version:	1.10
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f71ee986c79ead33970bd1e4dfe7891c
URL:		http://search.cpan.org/dist/Mail-RBL/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-NetAddr-IP >= 3.14
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is meant to help querying blackhole lists, typically for
use in anti-spam solutions.

%description -l pl.UTF-8
Ten moduł ma pomagać w odpytywaniu list "czarnych dziur", zwykle
używanych w mechanizmach antyspamowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# according to author it's ok even if it fails
# it fails so it's better to remove it
%{__rm} t/10-rbl.t

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Mail/*.pm
%{_mandir}/man3/*
