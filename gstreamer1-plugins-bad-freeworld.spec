# which plugins to actually build and install
%global gstdirs gst/dvbsuboverlay gst/dvdspu gst/siren
%global extdirs ext/dts ext/faad ext/libmms ext/mpeg2enc ext/mplex ext/rtmp ext/voamrwbenc ext/x265/ ext/openh264/ ext/dts/ ext/rtmp/
%define _legacy_common_support 1

%global         majorminor 1.0

Summary:        GStreamer %{majorminor} streaming media framework "bad" plug-ins
Name:           gstreamer1-plugins-bad-freeworld
Version:        1.17.2
Release:        7%{?dist}
License:        LGPLv2+
Group:          Applications/Multimedia
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gtk-doc
BuildRequires:  orc-devel
BuildRequires:  libdca-devel
BuildRequires:  faad2-devel >= 2.9.1
BuildRequires:  libmms-devel
BuildRequires:  mjpegtools-devel >= 2.0.0
BuildRequires:  twolame-devel
BuildRequires:  libmimic-devel
BuildRequires:  librtmp-devel
BuildRequires:  vo-amrwbenc-devel
BuildRequires:	x265-devel >= 3.4
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
BuildRequires:	openh264-devel >= 2.1.1
#
# For autoreconf
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: nasm

BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:  gcc-c++
BuildRequires:	mesa-libGLES-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libltc-devel
BuildRequires:  lcms2-devel
BuildRequires:  pkgconfig(gudev-%{majorminor})
BuildRequires:  pkgconfig(libusb-%{majorminor})
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(zvbi-0.2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  libnice-devel
BuildRequires:  liblrdf-devel
BuildRequires:  lilv-devel
BuildRequires:  libdvdnav-devel
BuildRequires:	openssl-devel

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
%autosetup -n gst-plugins-bad-%{version} -p1


%build
export OPENH264_CFLAGS="-I%{_includedir}"
export OPENH264_LIBS="-L%{_libdir} -lopenh264"
export CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations"

%meson \
    -D package-name="gst-plugins-bad 1.0 unitedrpms rpm" \
    -D package-origin="https://unitedrpms.github.io" \
    -D doc=disabled -D faac=disabled -D msdk=disabled \
    -D dts=enabled -D faad=enabled -D bluez=disabled \
    -D libmms=enabled -D mpeg2enc=enabled -D mplex=enabled \
    -D neon=disabled -D rtmp=enabled -D rtmp2=disabled \
    -D flite=disabled -D sbc=disabled  \
    -D voamrwbenc=enabled -D x265=enabled -D opencv=disabled \
    -D dvbsuboverlay=enabled -D dvdspu=enabled -D siren=enabled \
    -D real=disabled -D opensles=disabled -D tinyalsa=disabled \
    -D wasapi=disabled -D wasapi2=disabled -D avtp=disabled \
    -D dc1394=disabled -D directfb=disabled -D iqa=disabled \
    -D libde265=disabled -D musepack=disabled -D openni2=disabled \
    -D sctp=disabled -D svthevcenc=disabled -D voaacenc=disabled \
    -D zxing=disabled -D wpe=disabled -D x11=disabled \
    -D openh264=enabled -D srt=disabled -D openmpt=disabled \
    -D lv2=disabled -D va=disabled -D spandsp=disabled \
    -D openal=disabled -D vdpau=disabled -D uvch264=disabled \
    -D ltc=disabled -D vulkan=disabled -D wayland=disabled \
    -D libdrm=disabled -D usb=disabled -D va=disabled \
    -D assrender=disabled -D bz2=disabled -D kate=disabled \
    -D magicleap=disabled -D aom=disabled -D bs2b=disabled \
    -D chromaprint=disabled -D curl=disabled -D fdkaac=disabled \
    -D fluidsynth=disabled -D gme=disabled -D gsm=disabled \
    -D lrdf=disabled -D ladspa=disabled -D microdns=disabled \
    -D modplug=disabled -D openjpeg=disabled -D sndfile=disabled \
    -D ofa=disabled -D openal=disabled -D openexr=disabled \
    -D openmpt=disabled -D opus=disabled -D rsvg=disabled \
    -D soundtouch=disabled -D spandsp=disabled -D srt=disabled \
    -D srtp=disabled -D wildmidi=disabled -D zbar=disabled \
    -D webrtc=disabled -D webrtcdsp=disabled -D webp=disabled \
    -D openssl=disabled

%meson_build 

%install
%meson_install 

   
# Files exist in gstreamer1-plugins-bad-free, we don't need it here   

rm -f 	%{buildroot}/%{_bindir}/gst-transcoder-%{majorminor}
   
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/audio/audio-bad-prelude.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstnonstreamaudiodecoder.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstplanaraudioadapter.h
   

rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/basecamerabinsrc-prelude.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstbasecamerasrc.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstcamerabin-enum.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstcamerabinpreview.h
   
   
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/codecparsers-prelude.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstav1parser.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gsth264parser.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gsth265parser.h
   
   
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstjpeg2000sampling.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstjpegparser.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstmpeg4parser.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstmpegvideometa.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstmpegvideoparser.h

rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstvc1parser.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstvp8parser.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstvp8rangedecoder.h

rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers/gstvp9parser.h


rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/insertbin/gstinsertbin.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography-enumtypes.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography-prelude.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/isoff/gstisoff.h
   
   
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gst-atsc-section.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gst-dvb-descriptor.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gst-dvb-section.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gst-scte-section.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gstmpegts-enumtypes.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gstmpegtsdescriptor.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gstmpegtssection.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/mpegts-prelude.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/mpegts.h
   
   
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/gstplayer-g-main-context-signal-dispatcher.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/gstplayer-media-info.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/gstplayer-signal-dispatcher.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/gstplayer-types.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/gstplayer-video-overlay-video-renderer.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/gstplayer-video-renderer.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/gstplayer-visualization.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/gstplayer.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/player-prelude.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/player/player.h
   
   
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/sctp/sctp-prelude.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/sctp/sctpreceivemeta.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/sctp/sctpsendmeta.h
   
   
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/transcoder/gsttranscoder.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/transcoder/transcoder-prelude.h
   
   
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/gstfragment.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/gsturidownloader.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/gsturidownloader_debug.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/uridownloader-prelude.h
   
   
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/datachannel.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/dtlstransport.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/icetransport.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/rtcsessiondescription.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/rtpreceiver.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/rtpsender.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/rtptransceiver.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/webrtc-enumtypes.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/webrtc.h
rm -f   %{buildroot}/%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/webrtc_fwd.h


rm -f   %{buildroot}/%{_libdir}/girepository-%{majorminor}/GstBadAudio-%{majorminor}.typelib
rm -f   %{buildroot}/%{_libdir}/girepository-%{majorminor}/GstCodecs-%{majorminor}.typelib
rm -f   %{buildroot}/%{_libdir}/girepository-%{majorminor}/GstInsertBin-%{majorminor}.typelib
rm -f   %{buildroot}/%{_libdir}/girepository-%{majorminor}/GstMpegts-%{majorminor}.typelib
rm -f   %{buildroot}/%{_libdir}/girepository-%{majorminor}/GstPlayer-%{majorminor}.typelib   
rm -f   %{buildroot}/%{_libdir}/girepository-%{majorminor}/GstTranscoder-%{majorminor}.typelib
rm -f   %{buildroot}/%{_libdir}/girepository-%{majorminor}/GstWebRTC-%{majorminor}.typelib


rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaccurip.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaudiobuffersplit.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaudiofxbad.so
   
   
   
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaudiolatency.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixmatrix.so
rm -f	%{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstclosedcaption.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstcolormanagement.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdash.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdtls.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstdvbsubenc.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstfaceoverlay.so   
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so


rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstfreeverb.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstinter.so


rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstinterlace.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstipcpipeline.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstivfparse.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstivtc.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstjp2kdecimator.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstkms.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstlegacyrawparse.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmidi.so
   
   
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsdemux.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstnetsim.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstnvcodec.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so


rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstproxy.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstremovesilence.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstresindvd.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstrist.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstrtpmanagerbad.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstrtponvif.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so


rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstsmooth.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstswitchbin.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstteletext.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgsttimecode.so


rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgsttranscode.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstttmlsubs.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstv4l2codecs.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstvideoframe_audiolevel.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so
rm -f   %{buildroot}/%{_libdir}/gstreamer-%{majorminor}/libgsty4mdec.so
   
   
rm -f   %{buildroot}/%{_libdir}/libgstadaptivedemux-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstadaptivedemux-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstadaptivedemux-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgstbadaudio-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstbadaudio-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstbadaudio-%{majorminor}.so.0.1702.0


rm -f   %{buildroot}/%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.0.1702.0


rm -f   %{buildroot}/%{_libdir}/libgstcodecparsers-%{majorminor}.so
rm -f	%{buildroot}/%{_libdir}/libgstcodecparsers-%{majorminor}.so.0
rm -f	%{buildroot}/%{_libdir}/libgstcodecparsers-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgstcodecs-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstcodecs-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstcodecs-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgstinsertbin-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstinsertbin-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstinsertbin-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgstisoff-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstisoff-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstisoff-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgstmpegts-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstmpegts-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstmpegts-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgstphotography-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstphotography-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstphotography-%{majorminor}.so.0.1702.0
   
rm -f   %{buildroot}/%{_libdir}/libgstplayer-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstplayer-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstplayer-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgstsctp-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstsctp-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstsctp-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgsttranscoder-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgsttranscoder-%{majorminor}.so.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgsturidownloader-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgsturidownloader-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgsturidownloader-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/libgstwebrtc-%{majorminor}.so
rm -f   %{buildroot}/%{_libdir}/libgstwebrtc-%{majorminor}.so.0
rm -f   %{buildroot}/%{_libdir}/libgstwebrtc-%{majorminor}.so.0.1702.0
   
   
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-bad-audio-%{majorminor}.pc
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-bad-transcoder-%{majorminor}.pc

rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-codecparsers-%{majorminor}.pc
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-insertbin-%{majorminor}.pc
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-mpegts-%{majorminor}.pc
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-photography-%{majorminor}.pc
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-player-%{majorminor}.pc
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-sctp-%{majorminor}.pc
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-transcoder-%{majorminor}.pc
rm -f   %{buildroot}/%{_libdir}/pkgconfig/gstreamer-webrtc-%{majorminor}.pc

rm -f   %{buildroot}/%{_datadir}/gir-%{majorminor}/GstBadAudio-%{majorminor}.gir
rm -f   %{buildroot}/%{_datadir}/gir-%{majorminor}/GstCodecs-%{majorminor}.gir
rm -f   %{buildroot}/%{_datadir}/gir-%{majorminor}/GstInsertBin-%{majorminor}.gir
rm -f   %{buildroot}/%{_datadir}/gir-%{majorminor}/GstMpegts-%{majorminor}.gir
rm -f   %{buildroot}/%{_datadir}/gir-%{majorminor}/GstPlayer-%{majorminor}.gir
rm -f   %{buildroot}/%{_datadir}/gir-%{majorminor}/GstTranscoder-%{majorminor}.gir
rm -f   %{buildroot}/%{_datadir}/gir-%{majorminor}/GstWebRTC-%{majorminor}.gir


rm -rf   %{buildroot}/%{_datadir}/locale/
#

%files
%doc AUTHORS COPYING.LIB NEWS README RELEASE
# Take the whole dir for proper dir ownership (shared with other plugin pkgs)
%{_datadir}/gstreamer-%{majorminor}
%{_bindir}/playout

# Plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so
%{_libdir}/gstreamer-%{majorminor}/libgstsiren.so

# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
%{_libdir}/gstreamer-%{majorminor}/libgstmms.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{majorminor}/libgstmplex.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtmp.so
%{_libdir}/gstreamer-%{majorminor}/libgstvoamrwbenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstx265.so

%files -n gstreamer1-plugin-openh264
%{_libdir}/gstreamer-%{majorminor}/libgstopenh264.so

%changelog

* Fri Jul 10 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.17.2-7
- Updated to 1.17.2

* Sat May 30 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.2-11
- Rebuilt for x265

* Fri May 22 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.2-10
- Rebuilt for openh264

* Tue Mar 24 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.2-9
- Rebuilt for openh264

* Mon Feb 24 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.2-8
- Rebuilt for x265

* Wed Dec 04 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.2-7
- Updated to 1.16.2

* Sun Dec 01 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.1-9
- Rebuilt for x265

* Fri Nov 08 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.1-8
- Rebuilt for faad2

* Wed Oct 02 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.1-7
- Updated to 1.16.1

* Sat Aug 03 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.0-10
- Rebuilt for x265

* Tue Jun 25 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.0-9
- Rebuilt for openh264

* Sat Jun 22 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.0-8
- Rebuilt for x265

* Fri Apr 19 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.0-7
- Updated to 1.16.0-7

* Wed Feb 27 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.15.2-7
- Updated to 1.15.2-7

* Fri Feb 08 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.15.1-8  
- Rebuilt for x265

* Fri Jan 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.15.1-7  
- Updated to 1.15.1-7

* Fri Oct 12 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.4-8  
- Automatic Mass Rebuild

* Wed Oct 03 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.4-7  
- Updated to 1.14.4-7

* Mon Sep 17 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.3-7  
- Updated to 1.14.3-7

* Fri Jul 20 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.2-7  
- Updated to 1.14.2-7

* Sat Jul 07 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.1-9  
- Automatic Mass Rebuild

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
- Rebuilt for mjpegtools update to 2.%{majorminor}

* Sun Oct 13 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.0-1
- Rebase to new upstream release 1.2.0

* Thu Aug  8 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.1.3-1
- Rebase to new upstream release 1.1.3

* Tue Aug  6 2013 Hans de Goede <j.w.r.degoede@gmail.com> - %{majorminor}.9-1
- New upstream release %{majorminor}.9

* Mon Mar 25 2013 Hans de Goede <j.w.r.degoede@gmail.com> - %{majorminor}.6-1
- New upstream release %{majorminor}.6

* Sat Mar  2 2013 Hans de Goede <j.w.r.degoede@gmail.com> - %{majorminor}.5-1
- New upstream release %{majorminor}.5
- Drop no longer needed PyXML BuildRequires (rf#2572)

* Sat Nov  3 2012 Hans de Goede <j.w.r.degoede@gmail.com> - %{majorminor}.2-2
- Include some more files in %%doc (rf#2473)

* Sun Oct 28 2012 Hans de Goede <j.w.r.degoede@gmail.com> - %{majorminor}.2-1
- New upstream release %{majorminor}.2

* Sun Sep 23 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.99-1
- New upstream release 0.11.99
- Use global rather then define (rf#2473)
- Disable vo-aacenc plugin for now (rf#1742)
- Enable siren plugin now that it has been ported to the %{majorminor} API

* Sun Sep  9 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.93-1
- First version of gstreamer1-plugins-ugly for rpmfusion
