# TODO: Finish polishing, package builds and seems to work

%define 	module	meliae
Summary:	library meant to help people understand how their memory is being used in Python
Summary(pl.UTF-8):	TODO: library meant to help people understand how their memory is being used in Python.
Name:		python-%{module}
Version:	0.4.0
Release:	0.1
License:	GPL v3
Group:		Development/Languages/Python
# http://launchpad.net/meliae/trunk/0.4/+download/meliae-0.4.0.tar.gz
Source0:	http://launchpad.net/meliae/trunk/0.4/+download/%{module}-%{version}.tar.gz
# Source0-md5:	c704f4a314927fe96919018f67b2d3f3
URL:		-
BuildRequires:	python-Cython
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# remove BR: python-devel for 'noarch' packages.
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TODO

%description -l pl.UTF-8
TODO

%prep
%setup -q -n %{module}-%{version}


%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%dir %{py_sitedir}/%{module}

%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}*.egg-info
%endif

%attr(755,root,root) %{_bindir}/strip_duplicates.py
