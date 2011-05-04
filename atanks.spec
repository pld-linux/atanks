Summary:	Atomic Tanks - a game similiar to Scorched Earth and Worms
Summary(pl.UTF-8):	Atomic Tanks - gra podobna do Scorched Earth oraz Worms
Name:		atanks
Version:	4.9
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/atanks/%{name}-%{version}.tar.gz
# Source0-md5:	0785ea915d944d3d2614739e2bdd6d07
Patch0:		%{name}-flags.patch
Patch1:		%{name}-install.patch
Patch2:		%{name}-desktop.patch
URL:		http://atanks.sourceforge.net/
BuildRequires:	allegro-devel >= 4.4.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atomic Tanks is a Scorched Earth clone similar to the Worms series of
games. Annihilate the other tanks to earn money, then spend it on
bigger and better shields and weapons to wipe out the opposition.
Features a wide array of weapons, AI players, destructible landscape,
weather, parachutes, teleports and a wide range of other features.

%description -l pl.UTF-8
Atomic Tanks to klon Scorched Earth, podobny do serii gier "Worms". W
grze należy niszczyć inne czołgi, aby zarobić pieniądze, które można
przeznaczyć na nowe, lepsze tarcze oraz broń, która pomoże zwyciężyć
przeciwników. Zaletami gry są: duży asortyment broni, komputerowi
gracze, niszczalny teren, różne warunki pogodowe, spadochrony,
teleporty i inne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	LIBS="`allegro-config --libs` -lpthread"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a atanks.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a atanks.png  $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog credits.txt text/* README* TODO
%attr(755,root,root) %{_bindir}/atanks
%{_datadir}/games/%{name}
%{_desktopdir}/atanks.desktop
%{_pixmapsdir}/atanks.png
