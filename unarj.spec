Summary:	decompressor for .arj format archives
Summary(de):	Dekomprimierer für .arj-Archive
Summary(es):	Descompresor para archivos en formato .arj
Summary(fr):	Décompresseur pour les archives .arj
Summary(pl):	Program rozpakowuj±cy archiwa ARJ
Summary(pt_BR):	Descompactador para arquivos no formato .arj
Summary(tr):	ARJ biçimindeki arþivleri açan araç
Name:		unarj
Version:	2.43
Release:	9
Group:		Applications/Archiving
License:	distributable
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unarj program is used to uncompress .arj format archives, which
were somewhat popular on DOS based machines.

%description -l de
Das Programm 'unarj' dient zum Dekomprimieren von Archiven im
.arj-Format, das auf DOS-Rechnern einigermaßen beliebt ware.

%description -l es
El programa unarj se usa para descomprimir almacenajes en formato
.arj, que era algo popular en máquinas DOS.

%description -l fr
Le programme unarj est utilisé pour décompresser des archives au
format .arj, qui ont été très répandeus sur les systèmes DOS.

%description -l pl
Program unarj umo¿liwa rozpakowanie archiwów w formacie ARJ,
popularnym w systemach opartych o DOS.

%description -l pt_BR
O programa unarj é usado para descomprimir armazenagens em formato
.arj, que era algo popular em máquinas DOS.

%description -l tr
unarj, arj biçimindeki arþivler için açma programýdýr. ARJ, DOS
tabanlý makinelerde sýkça kullanýlan bir sýkýþtýrma biçimidir.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="-Wall -ansi -pedantic -DUNIX %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install unarj $RPM_BUILD_ROOT%{_bindir}

gzip -9nf unarj.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc unarj.doc.gz
%attr(755,root,root) %{_bindir}/unarj
