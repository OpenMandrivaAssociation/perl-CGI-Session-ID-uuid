%define upstream_name    CGI-Session-ID-uuid
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	UUID based CGI Session Identifiers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RS/RSE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
CGI::Session::ID::uuid is a CGI::Session 4.00 driver to generate identifiers
based on DCE 1.1 and ISO/IEC 11578:1996 compliant Universally Unique
Identifiers (UUID). This module requires a reasonable UUID generator. For this
it either requires the preferred OSSP::uuid module or alternatively the
Data::UUID, APR::UUID, DCE::UUID or UUID modules to be installed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%dir %{perl_vendorlib}/CGI/Session/ID
%{perl_vendorlib}/CGI/Session/ID/*
%{_mandir}/*/*
