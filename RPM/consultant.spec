%global debug_package %{nil}
Name:           consultant
Version:        0
Release:        2
Summary:        ConsultantPlus

Group:          Applications/Productivity
License:        GPLv2

# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
URL:            http://192.168.0.186/
Source0:        cons.ico
Source1:	conslin
Source2:	cons
Source3:	run_cons.sh
Source4:	run_consr.sh
Source5:	ConsultantPlus.desktop
Source6:	ConsultantPlusRegion.desktop
Source7:	cons2.ico

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:     i686
Requires:      wine

%description
ConsultantPlus

%prep

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/etc/
mkdir -p $RPM_BUILD_ROOT/mnt/consultantplus/
mkdir -p $RPM_BUILD_ROOT/mnt/consplusregion/
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
mkdir -p $RPM_BUILD_ROOT/home/user/Рабочий\ стол/
mkdir -p $RPM_BUILD_ROOT/etc/skel/Рабочий\ стол/

install -pm 444 %{SOURCE0} $RPM_BUILD_ROOT/usr/share/icons/
install -pm 777 %{SOURCE1} $RPM_BUILD_ROOT/usr/bin/
install -pm 444 %{SOURCE2} $RPM_BUILD_ROOT/etc/
install -pm 777 %{SOURCE3} $RPM_BUILD_ROOT/usr/local/bin/
install -pm 777 %{SOURCE4} $RPM_BUILD_ROOT/usr/local/bin/
install -pm 444 %{SOURCE5} $RPM_BUILD_ROOT/usr/share/applications/
install -pm 444 %{SOURCE6} $RPM_BUILD_ROOT/usr/share/applications/
install -pm 444 %{SOURCE7} $RPM_BUILD_ROOT/usr/share/icons/
install -pm 777 %{SOURCE5} $RPM_BUILD_ROOT/home/user/Рабочий\ стол/
install -pm 777 %{SOURCE5} $RPM_BUILD_ROOT/etc/skel/Рабочий\ стол/
install -pm 777 %{SOURCE6} $RPM_BUILD_ROOT/home/user/Рабочий\ стол/
install -pm 777 %{SOURCE6} $RPM_BUILD_ROOT/etc/skel/Рабочий\ стол/


%clean
rm -rf $RPM_BUILD_ROOT

%post
echo -e "\n//10.4.11.231/Cons	/mnt/consultantplus	cifs	credentials=/etc/cons,iocharset=utf8,file_mode=0777,dir_mode=0777,noperm,nocase,forcemand,users,noauto,rw	0 0" >> /etc/fstab
echo -e "\n//10.4.11.231/ConsR	/mnt/consplusregion	cifs	credentials=/etc/cons,iocharset=utf8,file_mode=0777,dir_mode=0777,noperm,nocase,forcemand,users,noauto,rw	0 0" >> /etc/fstab
echo -e "\n/usr/bin/conslin" >> /etc/rc.d/rc.local
chmod a+x /etc/rc.d/rc.local
chmod 4755 /sbin/mount.cifs
/usr/bin/conslin &

%preun

%postun
sed -i /conslin/d /etc/rc.d/rc.local
sed -i /consultantplus/d /etc/fstab
sed -i /consplusregion/d /etc/fstab

%files
%defattr(-,root,root,-)
%dir /mnt/consultantplus
%dir /mnt/consplusregion
/usr/share/icons/cons.ico
/usr/bin/conslin
/etc/cons
/usr/local/bin/run_cons.sh
/usr/local/bin/run_consr.sh
/usr/share/applications/ConsultantPlus.desktop
/usr/share/applications/ConsultantPlusRegion.desktop
/usr/share/icons/cons2.ico
/home/user/*/ConsultantPlus.desktop
/etc/skel/*/ConsultantPlus.desktop
/home/user/*/ConsultantPlusRegion.desktop
/etc/skel/*/ConsultantPlusRegion.desktop


%changelog
* Thu Jul 13 2017 <pva@sev.gov.ru> - 0-2
- CentOS 7 support
* Wed Jul 03 2017 <pva@sev.gov.ru> - 0-1
- New
