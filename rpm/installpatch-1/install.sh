#!/bin/sh
for rpm in `find /usr/share/installpatch/ -iname "*.rpm"`
do
	rpm -ivh ${rpm} --force
done
sed -i '/\/usr\/share\/installpatch\/install.sh/d' /etc/rc.local
