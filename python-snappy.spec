Name:           python2-snappy
Version:        %{major_version}
Release:        %{minor_version}%{?dist}
Url:            http://github.com/andrix/python-snappy
Summary:        Python 2 library for the snappy compression library from Google
License:        BSD
Source0:        pysnappy-rpm-src.tar.gz
BuildRequires:  gcc-c++, snappy-devel, pytest

%description
%{name}


%if %{?python3_sitelib:1}0
%package -n python3-snappy
Summary:        Python 3 library for the snappy compression library from Google
BuildRequires:  gcc-c++, snappy-devel, python3-pytest

%description -n python3-snappy
%{name}

%endif


%prep
%setup -q -n pysnappy
mkdir test
mv test_* test


%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%if %{?python3_sitelib:1}0
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif


%check
python2 -m pytest test/
%if %{?python3_sitelib:1}0
python3 -m pytest test/
%endif



%files
%defattr(-,root,root,-)
%doc AUTHORS README.rst
%{python_sitearch}/*

%if %{?python3_sitelib:1}0
%files -n python3-snappy
%defattr(-,root,root,-)
%doc AUTHORS README.rst
%{python3_sitearch}/*
%endif


%changelog
* Wed Jul 8 2015 Oskari Saarenmaa <os@ohmu.fi> - 0.5-0
- Initial
