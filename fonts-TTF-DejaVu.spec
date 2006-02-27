%define		_name	dejavu
%define		_rel	1
Summary:	Bitstream Vera True Type fonts fork with latin-ext-A characters
Summary(pl):	Od�am font�w True Type Bitstream Vera ze znakami latin-ext-A
Name:		fonts-TTF-DejaVu
Version:	2.3
Release:	1
License:	distributable
Group:		Fonts
Source0:	http://dl.sourceforge.net/dejavu/%{_name}-ttf-%{version}-%{_rel}.tar.gz
# Source0-md5:	83d1a20b38bba47b4d2428c744ac6a26
URL:		http://dejavu.sourceforge.net/wiki/index.php/Main_Page
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
DejaVu is a set of fonts based on Bitstream Vera fonts which have
additional characters from Latin Extended-A set.

%description -l pl
DejaVu to zestaw font�w oparty na Bitstream Vera z rozszerzonym
wsparciem dla znak�w Latin Extened-A.

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
