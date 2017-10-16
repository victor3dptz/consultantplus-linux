#!/bin/bash 

cd ~
if [ $(pgrep -f /mnt/consplusregion/consreg.exe)>'0' ]
then
exit 1;
fi
stat=`mktemp`
mount /mnt/consplusregion
WINEARCH=win32 wine /mnt/consplusregion/consreg.exe /linux >$stat 2>&1 &
while ! grep -q "fixme:file:MoveFileWithProgressW MOVEFILE_WRITE_THROUGH unimplemented" $stat
do
sleep 10;
done
#kill
VR=$(pgrep -f consplusregion)
kill $VR;
VR2=$(pgrep -f CONSPLUSREGION)
kill $VR2;
umount -l /mnt/consplusregion
rm -f $stat