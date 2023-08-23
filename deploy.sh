#!/bin/sh

pwd
sudo docker compose up -d
cd web
sudo docker compose up -d
