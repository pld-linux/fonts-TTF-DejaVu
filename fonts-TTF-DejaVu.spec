%define		_name	dejavu
%define		_rel	1
Summary:	Bitstream Vera True Type fonts fork with additional characters
Summary(pl.UTF-8):	Odłam fontów True Type Bitstream Vera z dodanymi znakami
Name:		fonts-TTF-DejaVu
Version:	2.15
Release:	1
License:	distributable
Group:		Fonts
Source0:	http://dl.sourceforge.net/dejavu/%{_name}-ttf-%{version}.tar.bz2
# Source0-md5:	2f8c073084c27d0df40e747eda7f79ba
URL:		http://dejavu.sourceforge.net/wiki/index.php/Main_Page
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
DejaVu is a set of fonts based on Bitstream Vera fonts which have
additional characters from a variety of scripts.

%description -l pl.UTF-8
DejaVu to zestaw fontów oparty na Bitstream Vera z dodanymi znakami
wielu alfabetów.

%prep
%setup -q -n %{_name}-ttf-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README NEWS
%{_ttffontsdir}/*
