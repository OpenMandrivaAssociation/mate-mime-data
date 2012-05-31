Name:		mate-mime-data
Summary:	The MATE MIME database files
Version:	1.2.2
Release:	1
License:	GPLv2
Group:		System/Libraries
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	shared-mime-info

%description
The MATE MIME database contains a basic set of applications and MIME
types for a MATE system.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}

%description devel
The pkgconfig for %{name}.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--build=%_host

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README
%{_sysconfdir}/mate-vfs-mime-magic
%{_datadir}/application-registry
%{_datadir}/mime-info/*

%files devel
%{_datadir}/pkgconfig/*.pc

