#!/bin/sh
env LC_CTYPE=C tr -dc "a-zA-Z0-9-_\!@#%^\&*\(\)\$\?+=\{\}[]\|:;\"<>,./?~\`" < /dev/urandom | head -c 128

