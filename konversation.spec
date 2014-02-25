Summary:	A user friendly IRC Client for KDE
Name:		konversation
Version:	1.5
Release:	2
License:	GPLv2+
Group:		Networking/IRC
Url:		http://konversation.kde.org
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/konversation/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		konversation-1.5-default-channel.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(openssl)
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
%{_kde_appsdir}/%{name}
%{_kde_appsdir}/kconf_update/*
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/konvirc.protocol
%{_kde_services}/konvirc6.protocol
%{_kde_services}/konvircs.protocol

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %name --with-html
