Summary:	decompressor for .arj format archives
Summary(de):	Dekomprimierer für .arj-Archive
Summary(fr):	Décompresseur pour les archives .arj .
Summary(pl):	Program rozpakowuj±cy archiwa ARJ
Summary(tr):	ARJ biçimindeki arþivleri açan araç
Name:		unarj
Version:	2.41a
Release:	10
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Copyright:	distributable
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}241a.tar.gz
Patch:		unarj-opt.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
The unarj program is used to uncompress .arj format archives,
which were somewhat popular on DOS based machines.

%description -l de
Das Programm 'unarj' dient zum Dekomprimieren von Archiven im
.arj-Format, das auf DOS-Rechnern einigermaßen beliebt ware.

%description -l fr
Le programme unarj est utilisé pour décompresser des archives
au format .arj, qui ont été très répandeus sur les systèmes DOS.

%description -l pl
Program unarj umo¿liwa rozpakowanie archiwów w formacie ARJ, 
popularnym w systemach opartych o DOS.

%description -l tr
unarj, arj biçimindeki arþivler için açma programýdýr. ARJ, DOS tabanlý
makinelerde sýkça kullanýlan bir sýkýþtýrma biçimidir.

%prep
%setup -q -n %{name}241a
%patch -p1

%build
make CFLAGS="-Wall -ansi -pedantic -DUNIX $RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT 
install -d $RPM_BUILD_ROOT%{_bindir}

install -s unarj $RPM_BUILD_ROOT%{_bindir}

gzip -9nf unarj.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc unarj.doc.gz
%attr(755,root,root) %{_bindir}/unarj
