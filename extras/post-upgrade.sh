#!/bin/bash

# Post-upgrade script for Mutalyzer. Run after the setuptools installation
# (python setup.py install).
#
# Notice: The definitions in this file are quite specific to the standard
# Mutalyzer environment. This consists of a Debian stable (Squeeze) system
# with Apache and Mutalyzer using its mod_wsgi module. Debian conventions are
# used throughout. See the README file for more information.
#
# Usage (from the source root directory):
#   sudo bash extras/post-upgrade.sh

set -e

# The 'cd /' is a hack to prevent the mutalyzer package under the current
# directory to be used.
PACKAGE_ROOT=$(cd / && python -c 'import mutalyzer; print mutalyzer.package_root()')

if [ ! -e /var/www/mutalyzer ]; then
    mkdir -p /var/www/mutalyzer
fi

if [ -e /var/www/mutalyzer/base ]; then
    echo "Removing /var/www/mutalyzer/base"
    rm /var/www/mutalyzer/base
fi

echo "Symlinking /var/www/mutalyzer/base to $PACKAGE_ROOT/templates/base"
ln -s $PACKAGE_ROOT/templates/base /var/www/mutalyzer/base

echo "Restarting Apache"
/etc/init.d/apache2 restart

echo "Restarting Mutalyzer batch daemon"
/etc/init.d/mutalyzer-batchd restart