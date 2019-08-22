#!/bin/sh

echo prunes tracking branches not on the remote.
git remote prune origin

echo delete the local branches for which the remote tracking branches have been pruned

# Make sure you are on master branch!
git checkout master
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -d

git branch -vv

