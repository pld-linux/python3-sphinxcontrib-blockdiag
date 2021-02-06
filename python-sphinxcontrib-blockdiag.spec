#
# Conditional build:
%bcond_with	tests	# unit tests (missing data)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx "blockdiag" extension
Summary(pl.UTF-8):	Rozszerzenie "blockdiag" dla Sphinksa
Name:		python-sphinxcontrib-blockdiag
Version:	1.5.5
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-blockdiag/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-blockdiag/sphinxcontrib-blockdiag-%{version}.tar.gz
# Source0-md5:	a867f4f392d2c47816b958bfba034c6e
URL:		https://pypi.org/project/sphinxcontrib-blockdiag/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 0.6
BuildRequires:	python-blockdiag >= 1.5.0
BuildRequires:	python-mock
BuildRequires:	python-sphinx_testing
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 0.6
BuildRequires:	python3-blockdiag >= 1.5.0
BuildRequires:	python3-sphinx_testing
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
Requires:	python-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Sphinx extension for embedding block diagram using blockdiag module.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do osadzania diagramów blokowych przy użyciu
modułu blockdiag.

%package -n python3-sphinxcontrib-blockdiag
Summary:	Sphinx "blockdiag" extension
Summary(pl.UTF-8):	Rozszerzenie "blockdiag" dla Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-sphinxcontrib

%description -n python3-sphinxcontrib-blockdiag
A Sphinx extension for embedding block diagram using blockdiag module.

%description -n python3-sphinxcontrib-blockdiag -l pl.UTF-8
Rozszerzenie Sphinksa do osadzania diagramów blokowych przy użyciu
modułu blockdiag.

%prep
%setup -q -n sphinxcontrib-blockdiag-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%{py_sitescriptdir}/sphinxcontrib/blockdiag.py[co]
%{py_sitescriptdir}/sphinxcontrib_blockdiag-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_blockdiag-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-blockdiag
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/blockdiag.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/blockdiag.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_blockdiag-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_blockdiag-%{version}-py*-nspkg.pth
%endif
