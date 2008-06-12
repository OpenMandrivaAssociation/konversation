%define _requires_exceptions devel\(linux-gate\)

%define __libtoolize    /bin/true
%define launchers /etc/dynamic/launchers/scanner

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 0
%{?_unstable: %{expand: %%global unstable 1}}

%if %unstable
%define use_enable_final 0
%define dont_strip 1
%endif

Name: konversation
Version: 1.0.1
Release: %mkrel 9
Summary: A user friendly IRC Client for KDE
License: GPL
Group: Networking/IRC
URL: http://konversation.kde.org
Source0: http://download2.berlios.de/konversation/%{name}-%{version}.tar.bz2
Patch0: %{name}-0.19-default_channel.patch
Patch1: %{name}-1.0.1-add-audacious-to-media.patch
Patch2: %{name}-1.0.1-fix-dcc-crash.patch
Patch3: %{name}-1.0.1-SVN_r604746.diff 
Patch4:	%{name}-fix-fr-translation.patch
Patch5:	%{name}-1.0.1-fix-desktop-file.patch
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
%{_bindir}/%{name}
%{_bindir}/%{name}ircprotocolhandler
%dir %{_datadir}/apps/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/applications/kde/%{name}.desktop
%{_iconsdir}/*/*/*/*
%_datadir/apps/kconf_update/*
%_docdir/HTML/*/konversation
%_datadir/config.kcfg/konversation.kcfg
%_datadir/services/*

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .default_channel
%patch1 -p0 -b .add_audacious_to_media
%patch2 -p0 -b .fix_dcc_crash
%patch3 -p0 -b .fix_serveur_under_compiz
%patch4 -p0 -b .fix_fr_translation
%patch5 -p0 -b .fix_desktop_file

%build
%configure2_5x \
%if %unstable
	--enable-debug=full \
%else
	--disable-debug \
%endif
%if %use_enable_final
	--enable-final \
%else
	--disable-final \
%endif
	--disable-static \
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif
	--disable-rpath \
	--with-xinerama 

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

