%define	_rc	rc2
Summary:	Atomic Tanks - a game similiar to Scorched Earth and Worms
Summary(pl):	Atomic Tanks - gra podobna do Scorched Earth oraz Worms
Name:		atanks
Version:	1.0.0
Release:	0.%{_rc}.1
Epoch:		1
License:	GPL
Group:		X11/Application/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	807a00c0beb41a310abab96005296b22
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-datadir.patch
URL:		http://atanks.sourceforge.net/
BuildRequires:	allegro-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_bindir	%{_prefix}/games

%description
Atomic Tanks is a Scorched Earth clone similar to the Worms series of games.
Annihilate the other tanks to earn money, then spend it on bigger and
better shields and weapons to wipe out the opposition. Features a wide
array of weapons, AI players, destructible landscape, weather, parachutes,
teleports and a wide range of other features.

%description -l pl
Atomic Tanks to klon Scorched Earth, podobny do serii gier ,,Worms''. Zniszcz
inne czo³gi ¿eby zarobiæ pieni±dze, potem wydaj je na wiêksze i lepsze
os³ony i broñ ¿eby zmia¿d¿yæ przeciwników. Zaletami gry s±: du¿y
asortyment broni, gracze sterowani przez komputer, niszczalny teren, ró¿ne
warunki pogodowe, spadochrony, teleporty i inne.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	DATA_DIR="%{_datadir}/games/%{name}" \
	CFLAGS="%{rpmcflags} -Iinclude"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install *.dat $RPM_BUILD_ROOT%{_datadir}/games/%{name}
install {credits,gloat,instr,revenge}.txt $RPM_BUILD_ROOT%{_datadir}/games/%{name}
install atanks $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog INSTRUCTIONS README readme.linux tanks.txt TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
