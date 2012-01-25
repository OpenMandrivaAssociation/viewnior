Summary:	Simple Elegant Image Viewer
Name:		viewnior
Version:	1.1
Release:	2
License:	GPLv3
Group:		Graphics
URL:		http://xsisqox.github.com/Viewnior/
Source0:	http://cloud.github.com/downloads/xsisqox/Viewnior/%{name}-%{version}.tar.xz

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
%setup -q

%build
%configure2_5x \
	--enable-wallpaper

%make LIBS='-lm'

%install
%makeinstall_std
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

