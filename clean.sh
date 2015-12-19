#!/bin/bash

pyc_count=`ls -l | grep .pyc | wc -l`

if [ "$pyc_count" = 0 ];
then
    echo "Clean"
fi

if [ "$pyc_count" -gt 0 ];
then
    echo "Cleaning..."
    rm *.pyc
fi
