#!/bin/bash

if [ -z "$1" ]
then
    DESTINATION_BRANCH="master"
else
    DESTINATION_BRANCH=$1
fi
 
BRANCH=$(git rev-parse --abbrev-ref HEAD)
REPO_URL=$(git remote get-url origin | sed -e 's/git@//' -e 's/.git//' -e 's/:/\//')
PR_URL="https://$REPO_URL/compare/$DESTINATION_BRANCH...$BRANCH"
open $PR_URL

