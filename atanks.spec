Summary:	Atomic Tanks - a game similiar to Scorched Earth and Worms
Summary(pl.UTF-8):	Atomic Tanks - gra podobna do Scorched Earth oraz Worms
Name:		atanks
Version:	6.6
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://downloads.sourceforge.net/atanks/%{name}-%{version}.tar.gz
# Source0-md5:	f53bbb0017d1ed79045085f6a36c85a8
Patch0:		%{name}-flags.patch
Patch1:		%{name}-desktop.patch
URL:		https://atanks.sourceforge.io/
BuildRequires:	allegro-devel >= 4.4.0
BuildRequires:	libstdc++-devel >= 6:4.3
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

%build
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TODO credits.txt
%lang(ru) %doc README_ru.txt
%attr(755,root,root) %{_bindir}/atanks
%{_datadir}/games/%{name}
%{_datadir}/metainfo/io.sourceforge.atanks.metainfo.xml
%{_desktopdir}/atanks.desktop
%{_iconsdir}/hicolor/48x48/apps/atanks.png
