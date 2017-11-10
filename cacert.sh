#!/bin/bash

usage() {
    echo "$0 inputcert.pem"
    exit
}

if [ -z "$1" ]
then
    usage
fi
 
SUBJECT_HASH=`openssl x509 -inform PEM -in $1 -subject_hash -noout`
OUTFILE=$SUBJECT_HASH.0

echo "Creating $OUTFILE..."

openssl x509 -inform PEM -in $1 > $OUTFILE
openssl x509 -inform PEM -in $1 -text -noout >> $OUTFILE
openssl x509 -inform PEM -in $1 -fingerprint -noout >> $OUTFILE

