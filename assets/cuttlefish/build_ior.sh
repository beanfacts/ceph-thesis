#!/bin/bash
docker build -t cf-bench-ior -f Dockerfile.ior .
cat > build-ior.def << EOF
Bootstrap: docker-daemon
From: cf-bench-ior:latest

%runscript
    exec "\$@"

%startscript
    exec "\$@"
EOF
apptainer build --force --fix-perms cf-bench-ior.sif build-ior.def
