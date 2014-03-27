Name:       gupnp
Summary:    GUPnP is an framework for creating UPnP devices & control points
Version:    0.20.5
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.gupnp.org/
Source0:    http://download.gnome.org/sources/%{name}/0.20/%{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gssdp-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala


%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary:    Development package for gupnp
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Files for development with gupnp.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -rf  $RPM_BUILD_ROOT%{_datadir}/gtk-doc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/gupnp-1.0.pc
%{_libdir}/*.so
%{_includedir}/gupnp-1.0
%{_bindir}/gupnp-binding-tool
%{_libdir}/girepository-1.0/GUPnP-1.0.typelib
%{_datadir}/gir-1.0/GUPnP-1.0.gir
%{_datadir}/vala/vapi/gupnp-1.0.deps
%{_datadir}/vala/vapi/gupnp-1.0.vapi
