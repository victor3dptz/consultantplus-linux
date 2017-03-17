#!/bin/bash 

if [ $(pgrep -f /mnt/consplusregion/consreg.exe)>'0' ]
then
exit 1;
fi
rm /tmp/cons2.stat
mount /mnt/consplusregion
WINEARCH=win32 WINEPREFIX="/home/user/.wine" wine /mnt/consplusregion/consreg.exe /linux >/tmp/cons2.stat 2>&1 &
while ! grep -q "fixme:file:MoveFileWithProgressW MOVEFILE_WRITE_THROUGH unimplemented" /tmp/cons2.stat
do
sleep 10;
done
#kill
VR=$(pgrep -f consplusregion)
kill $VR;
VR2=$(pgrep -f CONSPLUSREGION)
kill $VR2;
umount -l /mnt/consplusregion