%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Request
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides an easy way to perform HTTP requests
Summary(pl):	%{_pearname} - daje ³atwy sposób przygotowania wywo³añ HTTP
Name:		php-pear-%{_pearname}
Version:	1.2.4
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0dfacef0ab8e9ab5c3948c959180973c
URL:		http://pear.php.net/package/HTTP_Request/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Requires:	php-pear-Net_URL >= 1.0.7
Requires:	php-pear-Net_Socket >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Supports GET/POST/HEAD/TRACE/PUT/DELETE, Basic authentication, Proxy,
Proxy Authentication etc.

In PEAR status of this package is: %{_status}.

%description -l pl
Obs³uguje metody GET/POST/HEAD/TRACE/PUT/DELETE, motodê
uwierzytelniania Basic, Proxy, uwierzytelnianie Proxy itp.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
