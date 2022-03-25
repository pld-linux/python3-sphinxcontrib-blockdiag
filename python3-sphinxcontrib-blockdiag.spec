#
# Conditional build:
%bcond_with	tests	# unit tests (missing in sdist)

Summary:	Sphinx "blockdiag" extension
Summary(pl.UTF-8):	Rozszerzenie "blockdiag" dla Sphinksa
Name:		python3-sphinxcontrib-blockdiag
Version:	2.0.0
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-blockdiag/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-blockdiag/sphinxcontrib-blockdiag-%{version}.tar.gz
# Source0-md5:	0c8acbb74f2d92235ec917ba69298f03
URL:		https://pypi.org/project/sphinxcontrib-blockdiag/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 2.0
BuildRequires:	python3-blockdiag >= 1.5.0
BuildRequires:	python3-sphinx_testing
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
Requires:	python3-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Sphinx extension for embedding block diagram using blockdiag module.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do osadzania diagramów blokowych przy użyciu
modułu blockdiag.

%prep
%setup -q -n sphinxcontrib-blockdiag-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/blockdiag.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/blockdiag.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_blockdiag-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_blockdiag-%{version}-py*-nspkg.pth
