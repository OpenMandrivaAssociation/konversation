# THIS PACKAGE IS HOSTED AT MANDRIVA SVN
# PLEASE DO NOT UPLOAD DIRECTLY BEFORE COMMIT


%define name	konversation
%define version	1.0.1
%define release	%mkrel 7

Name:		%name
Summary:	A user friendly IRC Client for KDE
Version:	%version
Release:	%release
License:	GPL
Group:		Networking/IRC
Source0:	http://download2.berlios.de/konversation/%{name}-%{version}.tar.bz2
Patch2:		%{name}-0.19-default_channel.patch
# (nl) : Feature 138836
Patch4:		%{name}-1.0.1-add-audacious-to-media.patch
# (nl) : mdv bug: 28019 kde bug: 133312
Patch5:		%{name}-1.0.1-fix-dcc-crash.patch
#(nl) :  fix defective server list window with compiz
Patch6:		%{name}-1.0.1-SVN_r604746.diff 
Patch7:		%{name}-fix-fr-translation.patch
Patch8:		%{name}-1.0.1-fix-desktop-file.patch
BuildRoot:	%{_tmppath}/%{name}-root
URL:		http://konversation.kde.org
Requires:	kdebase-progs >= 3.4
BuildRequires:	kdebase-devel

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
						    
%post
%{update_menus}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README
%{_bindir}/%{name}
%{_bindir}/%{name}ircprotocolhandler

%dir %{_datadir}/apps/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/applications/kde/%{name}.desktop
%{_iconsdir}/crystalsvg/16x16/actions/kimproxyaway.png
%{_iconsdir}/crystalsvg/16x16/actions/kimproxyoffline.png
%{_iconsdir}/crystalsvg/16x16/actions/kimproxyonline.png
%{_iconsdir}/crystalsvg/22x22/actions/char.png
%{_iconsdir}/crystalsvg/22x22/actions/kimproxyaway.png
%{_iconsdir}/crystalsvg/22x22/actions/kimproxyoffline.png
%{_iconsdir}/crystalsvg/22x22/actions/kimproxyonline.png
%{_iconsdir}/crystalsvg/22x22/actions/konv_message.png
%{_iconsdir}/crystalsvg/32x32/actions/kimproxyaway.png
%{_iconsdir}/crystalsvg/32x32/actions/kimproxyoffline.png
%{_iconsdir}/crystalsvg/32x32/actions/kimproxyonline.png
%{_iconsdir}/crystalsvg/scalable/actions/kimproxyaway.svgz
%{_iconsdir}/crystalsvg/scalable/actions/kimproxyoffline.svgz
%{_iconsdir}/crystalsvg/scalable/actions/kimproxyonline.svgz
%{_iconsdir}/crystalsvg/scalable/actions/konv_message.svgz
%{_iconsdir}/hicolor/*/apps/konversation.png
%{_iconsdir}/hicolor/scalable/apps/konversation.svgz

%_datadir/apps/kconf_update/*.pl
%_datadir/apps/kconf_update/konversation.upd
   
%dir %_docdir/HTML/da/konversation/
%doc %_docdir/HTML/da/konversation/common
%doc %_docdir/HTML/da/konversation/*.bz2
%doc %_docdir/HTML/da/konversation/*.docbook
   
%dir %_docdir/HTML/en/konversation/
%doc %_docdir/HTML/en/konversation/common
%doc %_docdir/HTML/en/konversation/*.bz2
%doc %_docdir/HTML/en/konversation/*.docbook
%doc %_docdir/HTML/en/konversation/*.png

%dir %_docdir/HTML/et/konversation/
%doc %_docdir/HTML/et/konversation/common
%doc %_docdir/HTML/et/konversation/*.bz2
%doc %_docdir/HTML/et/konversation/*.docbook

%dir %_docdir/HTML/it/konversation/
%doc %_docdir/HTML/it/konversation/common
%doc %_docdir/HTML/it/konversation/*.bz2
%doc %_docdir/HTML/it/konversation/*.docbook
%doc %_docdir/HTML/it/konversation/*.png

%dir %_docdir/HTML/pt/konversation/
%doc %_docdir/HTML/pt/konversation/common
%doc %_docdir/HTML/pt/konversation/*.bz2
%doc %_docdir/HTML/pt/konversation/*.docbook

%dir %_docdir/HTML/ru/konversation/
%doc %_docdir/HTML/ru/konversation/common
%doc %_docdir/HTML/ru/konversation/*.bz2
%doc %_docdir/HTML/ru/konversation/*.docbook

%dir %_docdir/HTML/sv/konversation/
%doc %_docdir/HTML/sv/konversation/common
%doc %_docdir/HTML/sv/konversation/*.bz2
%doc %_docdir/HTML/sv/konversation/*.docbook
%doc %_docdir/HTML/sv/konversation/*.png

%dir %_docdir/HTML/nl/konversation/
%doc %_docdir/HTML/nl/konversation/common
%doc %_docdir/HTML/nl/konversation/*.bz2
%doc %_docdir/HTML/nl/konversation/*.docbook
%doc %_docdir/HTML/nl/konversation/*.png
   
%_datadir/config.kcfg/konversation.kcfg
%_datadir/services/konvirc.protocol
%_datadir/services/konvirc6.protocol

%doc %_docdir/HTML/es/konversation/*.png

#--------------------------------------------------------------------

%prep
%setup -q

%patch2 -p1 -b .default_channel
%patch4 -p0 -b .add_audacious_to_media
%patch5 -p0 -b .fix_dcc_crash
%patch6 -p0 -b .fix_serveur_under_compiz
%patch7 -p0 -b .fix_fr_translation
%patch8 -p0 -b .fix_desktop_file

%build

%configure2_5x \
	--disable-rpath \
	--enable-nmcheck \
	--enable-pch \
	--enable-new-ldflags
%make

%install
rm -rf %{buildroot}
%makeinstall_std PACKAGE=%{name}

%find_lang %{name}

%clean
rm -rf %{buildroot}
