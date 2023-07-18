#!/bin/bash
mkdir data
docker build -t forensics .
docker run -v ${PWD}/data:/data forensics