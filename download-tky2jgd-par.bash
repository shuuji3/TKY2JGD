#!/usr/bin/env bash

# ref. TKY2JGD for Windowsダウンロード | 国土地理院
# https://www.gsi.go.jp/sokuchikijun/tky2jgd_download.html

VERSION="v2.1.2"
FILE_NAME="000185226.zip"

wget "https://www.gsi.go.jp/common/${FILE_NAME}"
unzip "${FILE_NAME}"
mv TKY2JGD.par data/
rm "${FILE_NAME}"
