Summary:	Simple Elegant Image Viewer
Name:		viewnior
Version:	1.8
Release:	1
License:	GPLv3
Group:		Graphics
URL:		http://xsisqox.github.com/Viewnior/
Source0:	https://github.com/hellosiyan/Viewnior/archive/refs/tags/Viewnior-viewnior-%{version}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	gnome-icon-theme
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	shared-mime-info
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)

Requires:	gnome-icon-theme >= 2.19.1
Requires:	shared-mime-info >= 0.20

%description
Viewnior is a image viewer program. Created to be simple, fast and elegant.
It's minimalistic interface provides more screenspace for your images.
Among its features are:

* Fullscreen & Slideshow
* Rotate, flip, save, delete images
* Animation support
* Browse only selected images
* Navigation window
* Set image as wallpaper (only under GNOME, see INSTALL file)
* Simple interface

%prep
%autosetup -n Viewnior-%{name}-%{version}

%build
%configure \
	--enable-wallpaper \
	--enable-shave

%make_build LIBS='-lm'

%install
%make_install
desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-Multimedia-Graphics" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*
     
# Correct permissions
find %{buildroot}%{_datadir}/icons/ -type d -print0 | xargs -0 chmod 0755
find %{buildroot}%{_datadir}/icons/ -type f -print0 | xargs -0 chmod 0644

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog* COPYING README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*



%changelog
* Thu May 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.3-1
+ Revision: 800418
- new version 1.3

* Wed Jan 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1-2
+ Revision: 768164
- imported package viewnior


* Sat Dec 18 2010 KDulcimer <kdulcimer@unity-linux.org> 1.1-1
- 1.1

* Fri Apr 02 2010 KDulcimer <kdulcimer@unity-linux.org> 1.0-1
- 1.0

* Fri Nov 20 2009 KDulcimer <kdulcimer@unity-linux.org> 0.7-1
- Import spec to Unity Linux

* Sun Sep 06 2009 slick50 <lxgator@gmail.com> 0.7-1pclos2009
- 0.7

* Sun Aug 09 2009 slick50 <lxgator@gmail.com> 0.6-1pclos2009
- 0.6

* Fri Jun 26 2009 slick50 <lxgator@gmail.com> 0.5-1pclos2009
- initial build
