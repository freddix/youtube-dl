Summary:	Video extraction utility for YouTube
Name:		youtube-dl
Version:	2015.03.28
Release:	1
License:	MIT, Public Domain
Group:		Applications/System
Source0:	http://youtube-dl.org/downloads/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	162b0e9ffb9eafa24e3b0b23cb2c58e2
URL:		http://rg3.github.com/youtube-dl/
BuildRequires:	python3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python3-libs
Requires:	python3-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
youtube-dl is a small command-line program to download videos from
YouTube.com and a few more sites.

%prep
%setup -qn %{name}

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.txt
%attr(755,root,root) %{_bindir}/youtube-dl
%{py3_sitescriptdir}/youtube_dl
%{py3_sitescriptdir}/*.egg-info
%{_mandir}/man1/youtube-dl.1*

