#!/bin/sh


echo rebase on develop

# Store current_branch_name
current_branch_name=$(git rev-parse --abbrev-ref HEAD)

# Checkout develop and pull latest
git checkout develop
git pull

# Checkout current_branch_name
git checkout $current_branch_name

# rebase it
git rebase --interactive

