Summary:	"Ugly" plugins for elisa
Summary(pl.UTF-8):	"Ochydne" wtyczki dla elisy
Name:		elisa-plugins-ugly
Version:	0.5.6
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	1815dcc9d3760e6f84df90f49df04434
URL:		http://www.fluendo.com/elisa/
BuildRequires:	elisa = %{version}
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.pth
%{py_sitescriptdir}/elisa/plugins/*
