%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Request
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Provides an easy way to perform HTTP requests
Summary(pl):	%{_class}_%{_subclass} - Daje ³atwy sposób przygotowania wywo³añ HTTP
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Supports GET/POST/HEAD/TRACE/PUT/DELETE, Basic authentication, Proxy,
Proxy Authentication etc.

%description -l pl
Wspiera GET/POST/HEAD/TRACE/PUT/DELETE, podstawow± autentyfikacjê,
Proxy, autentyfikacja Proxy, itd.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
