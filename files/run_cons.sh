#!/bin/bash 

if [ $(pgrep -f /mnt/consultantplus/cons.exe)>'0' ]
then
exit 1;
fi
rm /tmp/cons1.stat
mount /mnt/consultantplus
WINEARCH=win32 WINEPREFIX="/home/user/.wine" wine /mnt/consultantplus/cons.exe /linux >/tmp/cons1.stat 2>&1 &
while ! grep -q "fixme:file:MoveFileWithProgressW MOVEFILE_WRITE_THROUGH unimplemented" /tmp/cons1.stat
do
sleep 10;
done
#kill
VR=$(pgrep -f consultantplus)
kill $VR;
VR2=$(pgrep -f CONSULTANTPLUS)
kill $VR2;
umount -l /mnt/consultantplus