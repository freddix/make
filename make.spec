Summary:	GNU Make
Name:		make
Version:	3.82
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Building
Source0:	ftp://ftp.gnu.org/gnu/make/%{name}-%{version}.tar.bz2
# Source0-md5:	1a11100f3c63fcf5753818e59d63088f
Patch0:		%{name}-arg-list-length.patch
Patch1:		%{name}-bug30612.patch
Patch2:		%{name}-bug30723.patch
Patch3:		%{name}-dont-prune-intermediate.patch
Patch4:		%{name}-expensive_glob.patch
Patch5:		%{name}-makeflags.patch
Patch6:		%{name}-sort-blank.patch
URL:		http://www.gnu.org/software/make/
BuildRequires:	automake
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files. Make
allows users to build and install packages without any significant
knowledge about the details of the build process. The details about
how the program should be built are provided for make in the program's
makefile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf make $RPM_BUILD_ROOT%{_bindir}/gmake

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_infodir}/make.info*
%{_mandir}/man1/*

