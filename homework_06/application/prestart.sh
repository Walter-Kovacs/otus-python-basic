#!/usr/bin/env sh

echo "run prestart script"
flask db upgrade
echo "end prestart script"
