%define upstream_name    CGI-Session-ID-uuid
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	UUID based CGI Session Identifiers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RS/RSE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
CGI::Session::ID::uuid is a CGI::Session 4.00 driver to generate identifiers
based on DCE 1.1 and ISO/IEC 11578:1996 compliant Universally Unique
Identifiers (UUID). This module requires a reasonable UUID generator. For this
it either requires the preferred OSSP::uuid module or alternatively the
Data::UUID, APR::UUID, DCE::UUID or UUID modules to be installed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README
%dir %{perl_vendorlib}/CGI/Session/ID
%{perl_vendorlib}/CGI/Session/ID/*
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 680697
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 405782
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.03-3mdv2009.0
+ Revision: 255828
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.03-1mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 15 2007 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdv2008.0
+ Revision: 26914
- Import perl-CGI-Session-ID-uuid



* Tue May 15 2007 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdv2007.1
- initial Mandriva package
