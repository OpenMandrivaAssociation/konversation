Summary:	A user friendly IRC Client for Flasma 5
Name:		konversation
Version:	1.6
Release:	1
License:	GPLv2+
Group:		Networking/IRC
Url:		http://konversation.kde.org
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/konversation/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		konversation-1.6-default-channel.patch
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Emoticons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemViews)
Provides:	kde4-irc-client

%description
Konversation is a graphical Internet Relay Chat client (IRC)
with Plasma 5 support.

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
%cmake_qt5
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html
