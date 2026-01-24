%global srcname pyaes

Name:		python-%{srcname}
Version:	1.6.1
Release:	3
Summary:	Pure-Python implementation of AES block-cipher and common modes of operation
License:	MIT
URL:		https://github.com/ricmoo/%{srcname}
Source0:	https://github.com/ricmoo/%{srcname}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		python-pyaes-0001-Use-relative-imports-during-tests.patch
BuildArch:      noarch
BuildSystem:  python
BuildRequires:  python%{pyver}dist(pycryptodome)

%description
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).

%prep
%autosetup -p1 -n %{srcname}-%{version}

%files
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/*
