Summary:	Ttyrec is a tty recorder
Summary(pl):	Ttyrec nagrywa obraz z konsoli
Name:		ttyrec
Version:	1.0.5
Release:	1
License:	GPL
Group:		Applications/Console
Group(de):	Applikationen/Konsole
Group(pl):	Aplikacje/Konsola
Source0:	http://namazu.org/~satoru/%{name}/%{name}-%{version}.tar.gz
URL:		http://namazu.org/~satoru/ttyrec
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ttyrec records evens from a tty. Provides is also ttyplay, for playing
recorded data.

%description -l pl
Ttyrec nagrywa obraz z konsoliprep. W pakiecie jest program ttyplay,
s�u��cy do odtwarzania powsta�ych nagra�.

%prep
%setup  -q

%build
%{__make} CC=%{__cc} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install ttyrec ttyplay ttytime $RPM_BUILD_ROOT%{_bindir}
install ttyrec.1 ttyplay.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/tty*
%{_mandir}/man*/*