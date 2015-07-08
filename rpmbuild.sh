#!/bin/bash -xue

set -o pipefail

major_version=$(sed -ne "s,^version = '\(.*\)',\1,p" setup.py)
minor_version=0.$(git log | grep -c '^commit').$(git log -n 1| awk '/^commit/ { print substr($2, 1, 10); }')

git archive --output=pysnappy-rpm-src.tar.gz --prefix=pysnappy/ HEAD
rpmbuild -bb python-snappy.spec \
        --define "_sourcedir $(pwd)" \
        --define "major_version $major_version" \
        --define "minor_version $minor_version"
rm -f pysnappy-rpm-src.tar.gz
