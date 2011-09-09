Name:           perl-Sub-Uplevel
Version:        0.2002
Release:        4%{?dist}
Summary:        Apparently run a function in a higher stack frame
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sub-Uplevel/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Sub-Uplevel-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Like Tcl's uplevel() function, but not quite so dangerous. The idea is
just to fool caller(). All the really naughty bits of Tcl's uplevel()
are avoided.

%prep
%setup -q -n Sub-Uplevel-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
AUTHOR_TESTING=1 ./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README Todo examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.2002-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Steven Pritchard <steve@kspei.com> 0.2002-1
- Update to 0.2002.
- BR Test::More.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1901-2
- Rebuild for perl 5.10 (again)

* Wed Feb 20 2008 Steven Pritchard <steve@kspei.com> 0.1901-1
- Update to 0.1901.
- Use fixperms macro instead of our own chmod incantation.
- Reformat to match cpanspec output.

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.18-2
- rebuild for new perl

* Mon Dec 17 2007 Ralf Corsépius <rc040203@freenet.de> - 0.18-1
- Update to 0.18.

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.14-1
- Update to 0.14.

* Fri Jun 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.13-1
- Update to 0.13.

* Sat May 13 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.12-1
- Update to 0.12.
- Makefile.PL -> Build.PL.

* Fri Apr 21 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.10-1
- Update to 0.10.
- New upstream maintainer.
- Patch dropped.

* Wed Feb 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.09-4
- Uplevel.pm patch (perl 5.8.8). See bugzilla entry #182488.

* Thu Dec 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.09-3
- Dist tag.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.09-2
- rebuilt

* Thu Jul  8 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.09-1
- Update to 0.09 (with license info).

* Sun Jul  4 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.08-0.fdr.1
- First build.
