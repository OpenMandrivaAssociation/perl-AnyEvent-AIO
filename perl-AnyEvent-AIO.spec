%define upstream_name    AnyEvent-AIO
%define upstream_version 1.1

%define _requires_exceptions Exporter

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Truly asynchronous file and directrory I/O
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/AnyEvent/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-AnyEvent
BuildRequires: perl-IO-AIO
BuildRequires: perl-devel

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is an the AnyEvent manpage user, you need to make sure that you
use and run a supported event loop.

Loading this module will install the necessary magic to seamlessly
integrate the IO::AIO manpage into the AnyEvent manpage, i.e. you no longer
need to concern yourself with calling 'IO::AIO::poll_cb' or any of that
stuff (you still can, but this module will do it in case you don't).

The AnyEvent watcher can be disabled by executing 'undef
$AnyEvent::AIO::WATCHER'. Please notify the author of when and why you
think this was necessary.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
