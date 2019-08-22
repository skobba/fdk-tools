#!/bin/sh

echo delete all local branches that are already merged into master

git branch --merged master | grep -v '^[ *]*master$'
echo any key to continue..
read

git branch --merged master | grep -v '^[ *]*master$' | xargs git branch -d


