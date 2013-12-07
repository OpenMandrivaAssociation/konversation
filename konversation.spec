Summary:	A user friendly IRC Client for KDE
Name:		konversation
Version:	1.4
Release:	7
License:	GPLv2
Group:		Networking/IRC
Url:		http://konversation.kde.org
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/konversation/%{version}/src/%{name}-%{version}.tar.xz
Source1:	konversation-ru.po
#Patch0:		%{name}-1.2-default_channel.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(qca2)
Provides:	kde4-irc-client

%description
Konversation is a graphical Internet Relay Chat client (IRC)
with KDE support.

Features:
* Standard IRC features
* SSL server support
* Bookmarking support
* Easy to use graphical user interface
* Multiple servers and channels in one single window
* DCC file transfer
* Multiple identities for different servers
* Text decorations and colors
* OnScreen Display for notifications
* Automatic UTF-8 detection
* Per channel encoding support
* Theme support for nick icons
* Highly configurable

%files -f %{name}.lang
%doc README
%{_kde_bindir}/*
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_datadir}/apps/kconf_update/*
%{_kde_datadir}/kde4/services/konvirc.protocol
%{_kde_datadir}/kde4/services/konvirc6.protocol
%{_kde_datadir}/kde4/services/konvircs.protocol

#--------------------------------------------------------------------

%prep
%setup -q
#%patch0 -p1 -b .default_channel
cp %SOURCE1 po/ru/konversation.po

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang %{name} --with-html

