Summary:	"Ugly" plugins for elisa
Summary(pl.UTF-8):	"Ochydne" wtyczki dla elisy
Name:		elisa-plugins-ugly
Version:	0.3.5
Release:	0.1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	a24fc586c88001ddf3324bf64d14ff69
URL:		http://www.fluendo.com/elisa/
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
