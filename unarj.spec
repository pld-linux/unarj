Summary:	Decompressor for .arj format archives
Summary(de):	Dekomprimierer fЭr .arj-Archive
Summary(es):	Descompresor para archivos en formato .arj
Summary(fr):	DИcompresseur pour les archives .arj
Summary(pl):	Program rozpakowuj╠cy archiwa ARJ
Summary(pt_BR):	Descompactador para arquivos no formato .arj
Summary(ru):	Декомпрессор для архивных файлов формата .arj
Summary(tr):	ARJ biГimindeki arЧivleri aГan araГ
Summary(uk):	Декомпресор для арх╕вних файл╕в формату .arj
Name:		unarj
Version:	2.43
Release:	11
Group:		Applications/Archiving
License:	distributable
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
Patch1:		%{name}-subdir.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unarj program is used to uncompress .arj format archives, which
were somewhat popular on DOS based machines.

%description -l de
Das Programm 'unarj' dient zum Dekomprimieren von Archiven im
.arj-Format, das auf DOS-Rechnern einigermaъen beliebt ware.

%description -l es
El programa unarj se usa para descomprimir almacenajes en formato
.arj, que era algo popular en mАquinas DOS.

%description -l fr
Le programme unarj est utilisИ pour dИcompresser des archives au
format .arj, qui ont ИtИ trХs rИpandeus sur les systХmes DOS.

%description -l pl
Program unarj umo©liwa rozpakowanie archiwСw w formacie ARJ,
popularnym w systemach opartych o DOS.

%description -l pt_BR
O programa unarj И usado para descomprimir armazenagens em formato
.arj, que era algo popular em mАquinas DOS.

%description -l ru
Программа unarj используется для декомпрессии архивов формата .arj,
популярного преимущественно в мире DOS.

%description -l tr
unarj, arj biГimindeki arЧivler iГin aГma programЩdЩr. ARJ, DOS
tabanlЩ makinelerde sЩkГa kullanЩlan bir sЩkЩЧtЩrma biГimidir.

%description -l uk
Програма unarj використову╓ться для декомпрес╕╖ арх╕в╕в формату .arj,
популярного переважно в св╕т╕ DOS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} clean
%{__make} \
	CC=%{__cc} \
	CFLAGS="-Wall -ansi -pedantic -DUNIX %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install unarj $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc unarj.doc
%attr(755,root,root) %{_bindir}/unarj
