Summary:	Bitstream Vera TrueType fonts fork with additional characters
Summary(pl.UTF-8):	Odłam fontów TrueType Bitstream Vera z dodanymi znakami
Name:		fonts-TTF-DejaVu
Version:	2.37
Release:	1
License:	distributable
Group:		Fonts
Source0:	http://downloads.sourceforge.net/dejavu/dejavu-fonts-ttf-%{version}.tar.bz2
# Source0-md5:	d0efec10b9f110a32e9b8f796e21782c
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
%setup -q -n dejavu-fonts-ttf-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ttffontsdir},%{_datadir}/fontconfig/conf.avail,/etc/fonts/conf.d}

install ttf/*.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

cd fontconfig
for fontconf in *conf ; do
	install -m 0644 -p $fontconf $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
	ln -s %{_datadir}/fontconfig/conf.avail/$fontconf \
		$RPM_BUILD_ROOT/etc/fonts/conf.d/$fontconf
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS LICENSE NEWS README.md
%{_ttffontsdir}/DejaVu*.ttf
%{_datadir}/fontconfig/conf.avail/20-unhint-small-dejavu-*.conf
%{_datadir}/fontconfig/conf.avail/57-dejavu-*.conf
/etc/fonts/conf.d/20-unhint-small-dejavu-*.conf
/etc/fonts/conf.d/57-dejavu-*.conf
