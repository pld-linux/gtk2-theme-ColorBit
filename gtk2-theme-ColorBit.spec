Summary:	A colorfull all-in-one theme that uses clearlooks and pixbuf engine
Name:		gtk2-theme-ColorBit
Version:	1.0
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://carme.pld-linux.org/~uzsolt/sources/ColorBit.tar.gz
# Source0-md5:	9892481c0de40d10fb5221f1796051e7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A colorfull all-in-one theme that uses clearlooks and pixbuf engine.

%prep
%setup -q -n ColorBit

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/ColorBit
cp -R gtk* $RPM_BUILD_ROOT%{_datadir}/themes/ColorBit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/ColorBit
