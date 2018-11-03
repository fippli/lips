#!/bin/sh

read -p "Are you sure you wish to remove ip? [y/n]" CONFIRM

if [ "${CONFIRM}" = "y" -o "${CONFIRM}" = "Y" ]; then

    read -p "Do you wish to remove all ip files? [y/n]" ANS

    if [ "${ANS}" = "y" -o "${ANS}" = "Y" ]; then
            sourcePath=$(dirname "${BASH_SOURCE[0]}")
            rm -rf sourcePath
    fi;

    sudo rm /usr/local/bin/lips

    echo Removed lips

else
    echo Removal of lips was cancelled.
fi;



read -p "Press any key to close."
