Name: konversation
Version: 1.1
Release: %mkrel 1
Summary: A user friendly IRC Client for KDE
License: GPL
Group: Networking/IRC
URL: http://konversation.kde.org
Source0: http://download2.berlios.de/konversation/%{name}-%{version}.tar.bz2
Patch0: %{name}-0.19-default_channel.patch
Patch1: konversation-1.1-add-amarok2-support.patch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: kdelibs-devel
BuildRequires: openldap-devel

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
						    
%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache crystalsvg
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README
%{_kde3_bindir}/*
%{_kde3_datadir}/apps/%{name}
%{_kde3_datadir}/applications/kde/%{name}.desktop
%{_kde3_iconsdir}/*/*/*/*
%_kde3_datadir/apps/kconf_update/*
%_kde3_datadir/config.kcfg/konversation.kcfg
%_kde3_datadir/services/*

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p1 -b .default_channel
%patch1 -p0

%build
%configure_kde3
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name} --with-html

%clean
rm -rf %{buildroot}

