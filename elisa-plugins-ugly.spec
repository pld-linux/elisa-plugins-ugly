Summary:	"Ugly" plugins for elisa
Summary(pl.UTF-8):	"Ochydne" wtyczki dla elisy
Name:		elisa-plugins-ugly
Version:	0.5.31
Release:	3
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	e07faae0cc518c35da9b73453125c032
URL:		http://www.fluendo.com/elisa/
BuildRequires:	elisa = %{version}
BuildRequires:	rpm-pythonprov
Requires:	twill
Provides:	elisa-plugins = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Ugly" plugins for elisa

%description -l pl.UTF-8
"Ochydne" wtyczki dla elisy

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

#py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.pth
%{py_sitescriptdir}/elisa/plugins/*
