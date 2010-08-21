%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Request
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - provides an easy way to perform HTTP requests
Summary(pl.UTF-8):	%{_pearname} - daje łatwy sposób przygotowania wywołań HTTP
Name:		php-pear-%{_pearname}
Version:	1.4.4
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e7590ac0b912362b7ce85e247aefa8a6
URL:		http://pear.php.net/package/HTTP_Request/
BuildRequires:	php-pear-PEAR >= 1:1.4.3
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0.2
Requires:	php-pear-Net_Socket >= 1.0.7
Requires:	php-pear-Net_URL >= 1.0.12
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Supports GET/POST/HEAD/TRACE/PUT/DELETE, Basic authentication, Proxy,
Proxy Authentication etc.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Obsługuje metody GET/POST/HEAD/TRACE/PUT/DELETE, metodę
uwierzytelniania Basic, Proxy, uwierzytelnianie Proxy itp.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
