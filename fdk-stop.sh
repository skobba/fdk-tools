#!/bin/sh

pushd ~/github_brreg/fdk/

# stop - will stop your containers, but it won’t remove them.
# down - will stop your containers, removes the stopped containers and any networks that were created.

docker-compose stop

popd




