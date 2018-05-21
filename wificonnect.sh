#!/bin/bash

IF=$1
STATUS=$2

if [ "$IF" == "wlan0" ]
then
    case "$2" in
        up)
        # interface is up
        ;;
        down)
        # interface will be down
        ;;
        pre-up)
        # interface will be up
        ;;
        post-down)
        # interface is down
        ;;
        *)
        ;;
    esac
fi
