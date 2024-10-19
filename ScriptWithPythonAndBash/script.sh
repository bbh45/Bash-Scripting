#!/bin/bash

#Script to check if a website is up or down and if the website is down then send an email to a particular owner.

WEBSITE_URL=$1

check_website() {
    status_code=$(CURL --head -s $WEBSITE_URL | awk '/^HTTP/{print $2}')
    echo $status_code
    if [[ $status_code -eq "200" || $status_code -eq "301" ]]; then
        echo "website is running"
    else
        echo "website is down"
    fi
}
check_website