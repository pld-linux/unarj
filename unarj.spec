Summary:	Decompressor for .arj format archives
Summary(de.UTF-8):   Dekomprimierer für .arj-Archive
Summary(es.UTF-8):   Descompresor para archivos en formato .arj
Summary(fr.UTF-8):   Décompresseur pour les archives .arj
Summary(pl.UTF-8):   Program rozpakowujący archiwa ARJ
Summary(pt_BR.UTF-8):   Descompactador para arquivos no formato .arj
Summary(ru.UTF-8):   Декомпрессор для архивных файлов формата .arj
Summary(tr.UTF-8):   ARJ biçimindeki arşivleri açan araç
Summary(uk.UTF-8):   Декомпресор для архівних файлів формату .arj
Name:		unarj
Version:	2.63a
Release:	3
License:	distributable
Group:		Applications/Archiving
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
# Source0-md5:	a83d139c245f911f22cb1b611ec9768f
Patch0:		%{name}-opt.patch
Patch1:		%{name}-overflow.patch
Patch2:		%{name}-path.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unarj program is used to uncompress .arj format archives, which
were somewhat popular on DOS based machines.

%description -l de.UTF-8
Das Programm 'unarj' dient zum Dekomprimieren von Archiven im
.arj-Format, das auf DOS-Rechnern einigermaßen beliebt ware.

%description -l es.UTF-8
El programa unarj se usa para descomprimir almacenajes en formato
.arj, que era algo popular en máquinas DOS.

%description -l fr.UTF-8
Le programme unarj est utilisé pour décompresser des archives au
format .arj, qui ont été très répandeus sur les systèmes DOS.

%description -l pl.UTF-8
Program unarj umożliwa rozpakowanie archiwów w formacie ARJ,
popularnym w systemach opartych o DOS.

%description -l pt_BR.UTF-8
O programa unarj é usado para descomprimir armazenagens em formato
.arj, que era algo popular em máquinas DOS.

%description -l ru.UTF-8
Программа unarj используется для декомпрессии архивов формата .arj,
популярного преимущественно в мире DOS.

%description -l tr.UTF-8
unarj, arj biçimindeki arşivler için açma programıdır. ARJ, DOS
tabanlı makinelerde sıkça kullanılan bir sıkıştırma biçimidir.

%description -l uk.UTF-8
Програма unarj використовується для декомпресії архівів формату .arj,
популярного переважно в світі DOS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
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
%doc technote.txt unarj.txt
%attr(755,root,root) %{_bindir}/unarj
