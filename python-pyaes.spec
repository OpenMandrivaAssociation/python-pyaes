%global srcname pyaes


Name:		python-%{srcname}
Version:	1.6.1
Release:	2%{?dist}
Summary:	Pure-Python implementation of AES block-cipher and common modes of operation
License:	MIT
URL:		https://github.com/ricmoo/%{srcname}
Source0:	https://github.com/ricmoo/%{srcname}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		python-pyaes-0001-Use-relative-imports-during-tests.patch
BuildArch:      noarch


%description
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).


%package -n python3-%{srcname}
Summary:	%{summary}
Provides:	python-%{srcname} = %{EVRD}
BuildRequires:  python3-crypto
BuildRequires:  python3-devel


%description -n python3-%{srcname}
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/*
