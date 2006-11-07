Summary:	Atomic Tanks - a game similiar to Scorched Earth and Worms
Summary(pl):	Atomic Tanks - gra podobna do Scorched Earth oraz Worms
Name:		atanks
Version:	1.1.0
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/atanks/%{name}-%{version}.tar.gz
# Source0-md5:	27e47c942dd95f1b4ac72216c8f30d30
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-gcc34.patch
URL:		http://atanks.sourceforge.net/
BuildRequires:	allegro-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atomic Tanks is a Scorched Earth clone similar to the Worms series of
games. Annihilate the other tanks to earn money, then spend it on
bigger and better shields and weapons to wipe out the opposition.
Features a wide array of weapons, AI players, destructible landscape,
weather, parachutes, teleports and a wide range of other features.

%description -l pl
Atomic Tanks to klon Scorched Earth, podobny do serii gier ,,Worms''.
Trzeba zniszczyæ inne czo³gi ¿eby zarobiæ pieni±dze, potem wydaæ je na
wiêksze i lepsze os³ony i broñ ¿eby zmia¿d¿yæ przeciwników. Zaletami
gry s±: du¿y asortyment broni, gracze sterowani przez komputer,
niszczalny teren, ró¿ne warunki pogodowe, spadochrony, teleporty i
inne.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	DATA_DIR="%{_datadir}/%{name}" \
	CFLAGS="%{rpmcflags} -Iinclude"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install *.dat $RPM_BUILD_ROOT%{_datadir}/%{name}
install {credits,gloat,instr,revenge}.txt $RPM_BUILD_ROOT%{_datadir}/%{name}
install atanks $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS Changelog credits.txt Help.txt instr.txt README readme.linux tanks.txt TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
