#!/bin/bash 

cd ~
if [ $(pgrep -f /mnt/consultantplus/cons.exe)>'0' ]
then
exit 1;
fi

stat=`mktemp`
mount /mnt/consultantplus
WINEARCH=win32 wine /mnt/consultantplus/cons.exe /linux >$stat 2>&1 &
while ! grep -q "fixme:file:MoveFileWithProgressW MOVEFILE_WRITE_THROUGH unimplemented" $stat
do
sleep 10;
done
#kill
VR=$(pgrep -f consultantplus)
kill $VR;
VR2=$(pgrep -f CONSULTANTPLUS)
kill $VR2;
umount -l /mnt/consultantplus
rm -f $stat