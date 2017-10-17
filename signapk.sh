#!/usr/bin/env bash

if [[ $# -eq 0 ]] ; then
    echo "Usage $0 app.apk"
    exit 1
fi

jarsigner -verbose -keystore ~/.android/debug.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA $1 androiddebugkey

