# which plugins to actually build and install
%global gstdirs gst/dvbsuboverlay gst/dvdspu gst/siren
%global extdirs ext/dts ext/faad ext/libmms ext/mpeg2enc ext/mplex ext/rtmp ext/voamrwbenc ext/x265/ ext/openh264/ ext/dts/ ext/rtmp/

%global         majorminor 1.0

Summary:        GStreamer 1.0 streaming media framework "bad" plug-ins
Name:           gstreamer1-plugins-bad-freeworld
Version:        1.14.1
Release:        8%{?dist}
License:        LGPLv2+
Group:          Applications/Multimedia
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
BuildRequires:  gstreamer1-devel >= 1.4.0
BuildRequires:  gstreamer1-plugins-base-devel >= 1.4.0
BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gtk-doc
BuildRequires:  orc-devel
BuildRequires:  libdca-devel
BuildRequires:  faad2-devel
BuildRequires:  libmms-devel
BuildRequires:  mjpegtools-devel >= 2.0.0
BuildRequires:  twolame-devel
BuildRequires:  libmimic-devel
BuildRequires:  librtmp-devel
BuildRequires:  vo-amrwbenc-devel
BuildRequires:	x265-devel >= 2.8
#BuildRequires:  vo-aacenc-devel
BuildRequires: libusbx-devel
# New Make Depends
BuildRequires:	schroedinger-devel
BuildRequires:	libexif-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libvdpau-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	valgrind-devel
BuildRequires:	wildmidi-devel
BuildRequires:	librsvg2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	gtk3-devel
BuildRequires:	clutter-devel
BuildRequires:	libtiger-devel
BuildRequires:	ladspa-devel
BuildRequires:	openal-soft-devel
BuildRequires:	libusb-devel
# BuildRequires:	qt5-qtquick1-devel
BuildRequires:	qt5-qtx11extras-devel
BuildRequires:	qt5-qtwayland-devel
BuildRequires:	openh264-devel
#
# For autoreconf
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: nasm

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that have licensing issues, aren't tested
well enough, or the code is not of good enough quality.

%package -n 	gstreamer1-plugin-openh264
Summary:        GStreamer H.264 plugin


%description -n gstreamer1-plugin-openh264
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

%prep
%setup -q -n gst-plugins-bad-%{version}
autoreconf -ivf


%build
export OPENH264_CFLAGS="-I%{_includedir}"
export OPENH264_LIBS="-L%{_libdir} -lopenh264"
export CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations"

%configure --disable-static --enable-experimental --enable-gtk-doc \
    --with-package-name="gst-plugins-bad 1.0 rpmfusion rpm" \
    --with-package-origin="http://rpmfusion.org/" \
    --with-gtk=3.0 \
    --enable-debug \
    --enable-silent-rules \
    --enable-experimental

  # https://bugzilla.gnome.org/show_bug.cgi?id=655517
  # sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  # Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

for i in %{gstdirs} %{extdirs}; do
    pushd $i
    make %{?_smp_mflags} V=0
    popd
done


%install

for i in %{gstdirs} %{extdirs}; do
    pushd $i
    make install V=0 DESTDIR=$RPM_BUILD_ROOT
    popd
done

rm $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/*.la


%files
%doc AUTHORS COPYING.LIB NEWS README RELEASE
# Take the whole dir for proper dir ownership (shared with other plugin pkgs)
%{_datadir}/gstreamer-1.0

# Plugins without external dependencies
%{_libdir}/gstreamer-1.0/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-1.0/libgstdvdspu.so
%{_libdir}/gstreamer-1.0/libgstsiren.so

# Plugins with external dependencies
%{_libdir}/gstreamer-1.0/libgstdtsdec.so
%{_libdir}/gstreamer-1.0/libgstfaad.so
%{_libdir}/gstreamer-1.0/libgstmms.so
#%{_libdir}/gstreamer-1.0/libgstmimic.so
%{_libdir}/gstreamer-1.0/libgstmpeg2enc.so
#%{_libdir}/gstreamer-1.0/libgstmpg123.so
%{_libdir}/gstreamer-1.0/libgstmplex.so
%{_libdir}/gstreamer-1.0/libgstrtmp.so
%{_libdir}/gstreamer-1.0/libgstvoamrwbenc.so
%{_libdir}/gstreamer-1.0/libgstx265.so

%files -n gstreamer1-plugin-openh264
%{_libdir}/gstreamer-1.0/libgstopenh264.so

%changelog

* Sun May 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.1-8  
- Automatic Mass Rebuild

* Mon May 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.1-7 
- Updated to 1.14.1-7

* Wed Mar 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.0-7 
- Updated to 1.14.0-7

* Sun Mar 04 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.13.90-7  
- Updated to 1.13.90-7

* Sat Feb 24 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.12.4-8  
- Automatic Mass Rebuild

* Fri Dec 08 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.12.4-7
- Updated to 1.12.4-7   

* Thu Oct 05 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.12.3-9  
- Automatic Mass Rebuild

* Thu Sep 28 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.12.3-8  
- Automatic Mass Rebuild

* Mon Sep 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.3-7
- Updated to 1.12.3-7

* Tue Sep 05 2017 David Vásquez <davidva AT tutanota DOT com> - 1.12.2-5
- Rebuilt for new openh264

* Fri Aug 25 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.12.2-4  
- Automatic Mass Rebuild

* Mon Jul 31 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.12.2-3  
- Automatic Mass Rebuild

* Thu Jul 20 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.2-2
- Updated to 1.12.2-2

* Sat Jun 24 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.1-2
- Updated to 1.12.1-2

* Thu May 25 2017 David Vásquez <davidva AT tutanota DOT com> 1.12.0-2
- Updated to 1.12.0-2

* Sat Apr 29 2017 David Vásquez <davidva AT tutanota DOT com> 1.11.91-2
- Updated to 1.11.91-2

* Thu Apr 20 2017 David Vásquez <davidva AT tutanota DOT com> 1.11.90-2
- Updated to 1.11.90-2

* Fri Mar 31 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 1.11.2-3
- Rebuilt for openh264

* Tue Mar 14 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 1.11.2-2
- Updated for x265

* Fri Feb 24 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 1.11.2-1
- Updated to 1.11.2

* Fri Jan 27 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 1.11.1-1
- Updated to 1.11.1

* Tue Nov 15 2016 Pavlo Rudyi <paulcarroty At riseup.net> 1.10.2-1
- Updated to 1.10.2

* Thu Oct 06 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.9.2-1
- Updated to 1.9.2

* Fri Jul 08 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.9.1-1
- Updated to 1.9.1

* Thu Jun 23 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.8.2-1
- Updated

* Mon Jun 06 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.8.1-4
- Added, sub-package gstreamer1-plugin-openh264 and avoid conflicts

* Sat Jun 4 2016 Pavlo Rudyi <paulcarroty At riseup.net> 1.8.1-3
- Disabled openh264

* Sat Apr 23 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.8.1-2
- Added -Wno-deprecated-declarations

* Thu Apr 21 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.8.1-1
- Updated to 1.8.1
- Enabled openh264
- Enabled faac

* Sat May 16 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.5-2
- Add a patch from upstream fixing a faad2 crash which crashes firefox (rf3636)

* Sat May 16 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.5-1
- Rebase to new upstream release 1.4.5

* Wed Oct  1 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.3-1
- Rebase to new upstream release 1.4.3

* Sat Aug 30 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.1-1
- Rebase to new upstream release 1.4.1

* Sun Jun 15 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.4-1
- Rebase to new upstream release 1.2.4

* Sat Feb 15 2014 Michael Kuhn <suraia@ikkoku.de> - 1.2.3-1
- Update to 1.2.3.

* Thu Jan 09 2014 Michael Kuhn <suraia@ikkoku.de> - 1.2.2-1
- Update to 1.2.2.

* Tue Jan 07 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.2.1-2
- Rebuilt for librtmp

* Sat Nov 16 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.1-1
- Rebase to new upstream release 1.2.1

* Sun Nov 10 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-2
- Rebuilt for mjpegtools update to 2.1.0

* Sun Oct 13 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.0-1
- Rebase to new upstream release 1.2.0

* Thu Aug  8 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.1.3-1
- Rebase to new upstream release 1.1.3

* Tue Aug  6 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.9-1
- New upstream release 1.0.9

* Mon Mar 25 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.6-1
- New upstream release 1.0.6

* Sat Mar  2 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.5-1
- New upstream release 1.0.5
- Drop no longer needed PyXML BuildRequires (rf#2572)

* Sat Nov  3 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.2-2
- Include some more files in %%doc (rf#2473)

* Sun Oct 28 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.2-1
- New upstream release 1.0.2

* Sun Sep 23 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.99-1
- New upstream release 0.11.99
- Use global rather then define (rf#2473)
- Disable vo-aacenc plugin for now (rf#1742)
- Enable siren plugin now that it has been ported to the 1.0 API

* Sun Sep  9 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.93-1
- First version of gstreamer1-plugins-ugly for rpmfusion
