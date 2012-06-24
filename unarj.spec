Summary:     decompressor for .arj format archives
Summary(de): Dekomprimierer f�r .arj-Archive
Summary(fr): D�compresseur pour les archives .arj .
Summary(pl): Program rozpakowuj�cy archiwa ARJ
Summary(tr): ARJ bi�imindeki ar�ivleri a�an ara�
Name:        unarj
Version:     2.41a
Release:     10
Group:       Utilities/Archiving
Group(pl):   Narz�dzia/Archiwizacja
Copyright:   distributable
Source:      ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}241a.tar.gz
Patch:       %{name}-%{version}-opt.patch
Buildroot:   /tmp/%{name}-%{version}-root

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
make CFLAGS="-Wall -ansi -pedantic -DUNIX $RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT 
install -d $RPM_BUILD_ROOT/usr/bin

install -s unarj $RPM_BUILD_ROOT/usr/bin

gzip -9nf unarj.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc unarj.doc.gz
%attr(755, root, root) /usr/bin/unarj

%changelog
* Thu Feb 25 1999 Maciej Le�niewski <nimir@kis.p.lodz.pl>
  [2.41a-10]
- fixed gziped docs.

* Thu Feb 10 1999 Micha� Kuratczyk <kurkens@polbox.com>
  [2.41a-9]
- added Group(pl)
- sloted BuildRoot into PLD standard
- added gzipping man page

* Wed Nov 13 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.41a-8]
- fixed passing $RPM_OPT_FLAGS flags.

* Wed Jun 17 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- added pl translation,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
