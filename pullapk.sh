#!/usr/bin/env bash

if [[ $# -eq 0 ]] ; then
    echo "Usage $0 com.package"
    exit 1
fi

PACKAGES=`adb shell pm list packages | grep "$@" | cut -d ':' -f2- `
NUMPACKAGES=`echo $PACKAGES | wc -l`
if [[ $NUMPACKAGES -le 0 ]]; then
    echo "No matching packages"
    exit 1
fi
if [[ $NUMPACKAGES -ge 2 ]]; then
    echo -e "Multiple packages:\n$PACKAGES"
    exit 1
fi

PACKAGE="${PACKAGES/$'\r'/}"
APKPATH=`adb shell pm path $PACKAGE | cut -d ':' -f2-`
APKPATH="${APKPATH/$'\r'/}"
COMMAND="adb pull $APKPATH $PACKAGE.apk"
echo $COMMAND
$COMMAND

