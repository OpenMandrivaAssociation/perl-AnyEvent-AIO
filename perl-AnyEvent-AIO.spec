%define upstream_name    AnyEvent-AIO
%define upstream_version 1.1

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Exporter(.*)\\)'
%else
%define _requires_exceptions Exporter
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary: 	Truly asynchronous file and directrory I/O
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/AnyEvent/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-AnyEvent
BuildRequires:	perl-IO-AIO
BuildRequires:	perl-devel

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue Apr 17 2012 Götz Waschk <waschk@mandriva.org> 1.100.0-3mdv2012.0
+ Revision: 791440
- yearly rebuild

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.100.0-2
+ Revision: 653387
- rebuild for updated spec-helper

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 503921
- rebuild using %%perl_convert_version

* Sun Aug 02 2009 Götz Waschk <waschk@mandriva.org> 1.1-1mdv2010.0
+ Revision: 407572
- new version
- use perl version macro

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 268362
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Götz Waschk <waschk@mandriva.org> 1.0-2mdv2009.0
+ Revision: 217080
- add exception to make it installable

* Mon Jun 09 2008 Götz Waschk <waschk@mandriva.org> 1.0-1mdv2009.0
+ Revision: 217056
- import perl-AnyEvent-AIO


