Summary:	Video extraction utility for YouTube
Name:		youtube-dl
Version:	2012.10.09
Release:	1
License:	MIT, Public Domain
Group:		Applications/System
Source0:	https://github.com/rg3/youtube-dl/raw/%{version}/youtube-dl
# Source0-md5:	02c2a961099f067a8595ac771baed12a
URL:		http://rg3.github.com/youtube-dl/
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
youtube-dl is a small command-line program to download videos from
YouTube.com and a few more sites.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/youtube-dl

