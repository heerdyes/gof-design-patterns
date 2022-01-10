#!/usr/bin/env bash
gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=designpatterns.pdf -dBATCH $(cat pdflist.txt | awk '{printf("\"%s\" ",$0)} END { printf "\n" }')
