Name:		konversation
Version:	1.4
Release:	5
Summary:	A user friendly IRC Client for KDE
License:	GPLv2
Group:		Networking/IRC
URL:		http://konversation.kde.org
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/konversation/%{version}/src/%{name}-%{version}.tar.xz
Source1:	konversation-ru.po
#Patch0:		%{name}-1.2-default_channel.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	qca2-devel
BuildRequires:	openldap-devel
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

%files -f %name.lang
%doc README
%{_kde_bindir}/*
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*
%_kde_datadir/apps/kconf_update/*
%_kde_datadir/kde4/services/konvirc.protocol
%_kde_datadir/kde4/services/konvirc6.protocol
%_kde_datadir/kde4/services/konvircs.protocol

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
#%patch0 -p1 -b .default_channel
cp %SOURCE1 po/ru/konversation.po

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang %name --with-html



%changelog
* Fri Apr 27 2012 Crispin Boylan <crisb@mandriva.org> 1.4-1
+ Revision: 794006
- New release

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-2
+ Revision: 666040
- mass rebuild

* Fri Jul 09 2010 Funda Wang <fwang@mandriva.org> 1.3.1-1mdv2011.0
+ Revision: 549886
- new version 1.3.1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix spec file to follow kde spec files rules

* Fri Feb 26 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.2.3-2mdv2010.1
+ Revision: 512016
- Fix mix tabs/spaces
- Fix license
- Put %%files at end of spec

* Fri Feb 12 2010 Frederik Himpe <fhimpe@mandriva.org> 1.2.3-1mdv2010.1
+ Revision: 505075
- update to new version 1.2.3

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 1.2.2-1mdv2010.1
+ Revision: 504415
- New version 1.2.2

* Thu Nov 12 2009 Funda Wang <fwang@mandriva.org> 1.2.1-1mdv2010.1
+ Revision: 465261
- new version 1.2.1

* Tue Oct 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.2-2mdv2010.0
+ Revision: 459595
- Backport dcc location from trunk
  Remove patch rejected upstream

  + Raphaël Gertz <rapsys@mandriva.org>
    - Don't hide the apps by default
    - Fix default bad configuration

* Fri Oct 09 2009 Funda Wang <fwang@mandriva.org> 1.2-1mdv2010.0
+ Revision: 456344
- 1.2 Final

* Mon Oct 05 2009 Funda Wang <fwang@mandriva.org> 1.2-0.rc1.1mdv2010.0
+ Revision: 454165
- 1.2 rc 1

* Tue Sep 29 2009 Helio Chissini de Castro <helio@mandriva.com> 1.2-0.beta1.2mdv2010.0
+ Revision: 451011
- Provides kde4-irc-client

* Mon Sep 21 2009 Funda Wang <fwang@mandriva.org> 1.2-0.beta1.1mdv2010.0
+ Revision: 446535
- New version 1.2 beta1

* Sun Aug 09 2009 Funda Wang <fwang@mandriva.org> 1.2-0.alpha6.1mdv2010.0
+ Revision: 411851
- new version 1.2 alpha6

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 1.2-0.alpha5.1mdv2010.0
+ Revision: 410444
- new version 1.2 alpha5

* Sat Jul 04 2009 Funda Wang <fwang@mandriva.org> 1.2-0.alpha4.1mdv2010.0
+ Revision: 392089
- rediff channel patch
- New version 1.2 alpha 4

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 1.2-0.alpha3.1mdv2010.0
+ Revision: 382341
- New version 1.2 alpha3

* Tue May 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.2-0.alpha2.1mdv2010.0
+ Revision: 379885
- Remove pt_BR translation as this is now included
- Remove unused patches
- Add default channel
- Update to Alpha2

* Sat May 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1.75-0.968862.1mdv2010.0
+ Revision: 376498
- Fix file list
- New snapshot ( konvi is back on extragear)

* Fri May 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1.75-0.965153.1mdv2010.0
+ Revision: 373452
- Add buildrequire
- Update to kde4 port of konversation

* Sun Sep 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1-2mdv2009.0
+ Revision: 289113
- Add upstream patch that Fix keyboard accelerator management
- Add brazilian translations tks to Andre

* Wed Aug 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1-1mdv2009.0
+ Revision: 264720
- Add support for amarok 2.0
- Update to 1.1 Final release

* Mon Jul 14 2008 Funda Wang <fwang@mandriva.org> 1.1-0.rc1.1mdv2009.0
+ Revision: 234886
- New version 1.1 rc1
- drop old pacthes, they are not needed any more

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.0.1-9mdv2009.0
+ Revision: 218434
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-9mdv2008.1
+ Revision: 141733
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 01 2007 Helio Chissini de Castro <helio@mandriva.com> 1.0.1-8mdv2008.0
+ Revision: 57787
- Cleaned spec a little bit
- Keep flag enable_final off. was disabled before, but is workaround. Current patches togheter with
  1.0.1 make gcc preprocessor generates unqualified symbol errors, when doing the "join" of cpps.
  Need to be reported to konversarion devs.

* Wed Aug 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-7mdv2008.0
+ Revision: 57732
- fix mixture of tabs and spaces
- provide better description
- some minor cleans in spec file
- drop old menu directory
- use only konversation's upstream icons
- pass optimize options into configure

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix menu entry
    - [BUGFiX] Fix French translation (bug #22250)

