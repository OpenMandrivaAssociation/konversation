#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	A user friendly IRC Client for Plasma 6
Name:		plasma6-konversation
Version:	24.02.0
Release:	%{?git:0.%{git}.}2
License:	GPLv2+
Group:		Networking/IRC
Url:		https://konversation.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/konversation/-/archive/%{gitbranch}/konversation-%{gitbranchd}.tar.bz2#/konversation-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/konversation-%{version}.tar.xz
%endif
Patch0:		konversation-1.6-default-channel.patch
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Tools)
BuildRequires:	pkgconfig(phonon4qt6)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IdleTime)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:  qt6-qtmultimedia-gstreamer
BuildRequires:	qt6-qttools-dbus

%description
Konversation is a graphical Internet Relay Chat client (IRC)
with Plasma 6 support.

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

%files -f konversation.lang
%doc README
%{_bindir}/konversation
%{_datadir}/applications/org.kde.konversation.desktop
%{_iconsdir}/hicolor/*/*/konversation.png
%{_iconsdir}/hicolor/*/actions/konv_message.png
%{_datadir}/knotifications6/konversation.notifyrc
%{_datadir}/konversation
%{_datadir}/metainfo/org.kde.konversation.appdata.xml
%{_datadir}/knsrcfiles/konversation_nicklist_theme.knsrc
%{_datadir}/qlogging-categories6/konversation.categories
%{_datadir}/dbus-1/services/org.kde.konversation.service

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n konversation-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang konversation --with-html
