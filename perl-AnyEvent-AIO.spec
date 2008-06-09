
%define realname   AnyEvent-AIO
%define version    1.0
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Truly asynchronous file and directrory I/O
Source:     http://www.cpan.org/modules/by-module/AnyEvent/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl-AnyEvent
BuildRequires: perl-IO-AIO
BuildArch: noarch
%define _requires_exceptions Exporter

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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



