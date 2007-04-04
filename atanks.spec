Summary:	Atomic Tanks - a game similiar to Scorched Earth and Worms
Summary(pl.UTF-8):	Atomic Tanks - gra podobna do Scorched Earth oraz Worms
Name:		atanks
Version:	2.2
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/atanks/%{name}-%{version}.tar.gz
# Source0-md5:	dcb1c5b244755714edf903b2d3e87ec6
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-datadir.patch
URL:		http://atanks.sourceforge.net/
BuildRequires:	allegro-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atomic Tanks is a Scorched Earth clone similar to the Worms series of
games. Annihilate the other tanks to earn money, then spend it on
bigger and better shields and weapons to wipe out the opposition.
Features a wide array of weapons, AI players, destructible landscape,
weather, parachutes, teleports and a wide range of other features.

%description -l pl.UTF-8
Atomic Tanks to klon Scorched Earth, podobny do serii gier ,,Worms''.
Trzeba zniszczyć inne czołgi żeby zarobić pieniądze, potem wydać je na
większe i lepsze osłony i broń żeby zmiażdżyć przeciwników. Zaletami
gry są: duży asortyment broni, gracze sterowani przez komputer,
niszczalny teren, różne warunki pogodowe, spadochrony, teleporty i
inne.

%prep
%setup -q -n %{name}
%patch0 -p0

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
%doc BUGS Changelog credits.txt Help.txt instr.txt README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
