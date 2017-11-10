#!/bin/bash

openssl genrsa -des3 -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -sha256 -days 1825 -out ca.pem

