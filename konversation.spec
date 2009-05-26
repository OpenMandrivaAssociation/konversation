%define prever alpha2

Name: konversation
Version: 1.2
Release: %mkrel 0.%prever.1  
Summary: A user friendly IRC Client for KDE
License: GPL
Group: Networking/IRC
URL: http://konversation.kde.org
Source0: http://download2.berlios.de/konversation/%{name}-%{version}-%prever.tar.bz2
Patch0: %{name}-0.19-default_channel.patch
Patch1: konversation-1.1-add-amarok2-support.patch
Patch2: konversation-1.1-add-pt_BR.patch
Patch3: konversation-post-1.1-rev861574.patch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
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
						    
%files -f build/%name.lang
%defattr(-,root,root,-)
%doc README
%{_kde_bindir}/*
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*
%_kde_datadir/apps/kconf_update/*
%_kde_datadir/kde4/services/konvirc.protocol
%_kde_datadir/kde4/services/konvirc6.protocol

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-%prever
#%patch0 -p1 -b .default_channel
#%patch1 -p0
#%patch2 -p1
#%patch3 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std

%find_lang --with-html %name 

%clean
rm -rf %{buildroot}

