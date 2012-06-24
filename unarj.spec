Summary:	Decompressor for .arj format archives
Summary(de):	Dekomprimierer f�r .arj-Archive
Summary(es):	Descompresor para archivos en formato .arj
Summary(fr):	D�compresseur pour les archives .arj
Summary(pl):	Program rozpakowuj�cy archiwa ARJ
Summary(pt_BR):	Descompactador para arquivos no formato .arj
Summary(ru):	������������ ��� �������� ������ ������� .arj
Summary(tr):	ARJ bi�imindeki ar�ivleri a�an ara�
Summary(uk):	����������� ��� ��Ȧ���� ���̦� ������� .arj
Name:		unarj
Version:	2.63a
Release:	2
License:	distributable
Group:		Applications/Archiving
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
# Source0-md5:	a83d139c245f911f22cb1b611ec9768f
Patch0:		%{name}-opt.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unarj program is used to uncompress .arj format archives, which
were somewhat popular on DOS based machines.

%description -l de
Das Programm 'unarj' dient zum Dekomprimieren von Archiven im
.arj-Format, das auf DOS-Rechnern einigerma�en beliebt ware.

%description -l es
El programa unarj se usa para descomprimir almacenajes en formato
.arj, que era algo popular en m�quinas DOS.

%description -l fr
Le programme unarj est utilis� pour d�compresser des archives au
format .arj, qui ont �t� tr�s r�pandeus sur les syst�mes DOS.

%description -l pl
Program unarj umo�liwa rozpakowanie archiw�w w formacie ARJ,
popularnym w systemach opartych o DOS.

%description -l pt_BR
O programa unarj � usado para descomprimir armazenagens em formato
.arj, que era algo popular em m�quinas DOS.

%description -l ru
��������� unarj ������������ ��� ������������ ������� ������� .arj,
����������� ��������������� � ���� DOS.

%description -l tr
unarj, arj bi�imindeki ar�ivler i�in a�ma program�d�r. ARJ, DOS
tabanl� makinelerde s�k�a kullan�lan bir s�k��t�rma bi�imidir.

%description -l uk
�������� unarj ����������դ���� ��� ��������Ӧ� ��Ȧצ� ������� .arj,
����������� ��������� � �צԦ DOS.

%prep
%setup -q
%patch0 -p1

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
