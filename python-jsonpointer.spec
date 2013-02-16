Name:           python-jsonpointer
Version:        0.7.0
Release:        1%{?dist}
Summary:        Resolve JSON Pointers in Python

License:        BSD
URL:            http://pypi.python.org/pypi/jsonpointer/0.7
Source0:        http://pypi.python.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel


%description
Build self-validating python objects using JSON schemas

%prep
%setup -q -n jsonpointer-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
* Sat Feb 16 2013 Dan Prince - 0.7.0-1
- Initial package.
