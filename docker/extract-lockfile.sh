#!/bin/sh

dockerid=$(docker run -d --rm mcr314/shg_mud_builder:margarita sleep 600)
docker cp $dockerid:/app/fountain/Gemfile.lock docker/Gemfile.lock
docker kill $dockerid

