%define		_name	dejavu
Summary:	Bitstream Vera True Type fonts fork with latin-ext-A characters
Summary(pl):	Odłam czionek True Type Bitstream Vera ze znakami latin-ext-A
Name:		fonts-TTF-DejaVu
Version:	1.0
Release:	1
License:	distributable
Group:		Fonts
Source0:	http://www.srnet.cz/~stepan/sw/data/%{_name}-ttf-%{version}.tar.gz
# Source0-md5:	1289834767d32c4ae3b4d27c2558eb54
#Source1:	%{name}.Fontmap
URL:		http://www.gnome.org/fonts/
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
DejaVu is a set of fonts based on Bitstream Vera fonts which have additional characters from Latin Extended-A set.

%description -l pl
DejaVu to zestaw czcionek oparty na Bitstream Vera z rozszerzonym wsparciem dla znaków Latin Extened-A.

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
%doc README
%{_ttffontsdir}/*
