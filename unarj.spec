Summary:	decompressor for .arj format archives
Summary(de):	Dekomprimierer f�r .arj-Archive
Summary(fr):	D�compresseur pour les archives .arj .
Summary(pl):	Program rozpakowuj�cy archiwa ARJ
Summary(tr):	ARJ bi�imindeki ar�ivleri a�an ara�
Name:		unarj
Version:	2.41a
Release:	10
Group:		Utilities/Archiving
Group(pl):	Narz�dzia/Archiwizacja
Copyright:	distributable
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}241a.tar.gz
Patch:		unarj-opt.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
The unarj program is used to uncompress .arj format archives,
which were somewhat popular on DOS based machines.

%description -l de
Das Programm 'unarj' dient zum Dekomprimieren von Archiven im
.arj-Format, das auf DOS-Rechnern einigerma�en beliebt ware.

%description -l fr
Le programme unarj est utilis� pour d�compresser des archives
au format .arj, qui ont �t� tr�s r�pandeus sur les syst�mes DOS.

%description -l pl
Program unarj umo�liwa rozpakowanie archiw�w w formacie ARJ, 
popularnym w systemach opartych o DOS.

%description -l tr
unarj, arj bi�imindeki ar�ivler i�in a�ma program�d�r. ARJ, DOS tabanl�
makinelerde s�k�a kullan�lan bir s�k��t�rma bi�imidir.

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
