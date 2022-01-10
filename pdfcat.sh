#!/usr/bin/env bash
gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=designpatterns.pdf -dBATCH chainofresponsibilty/Behavioral_thumb_rules.pdf chainofresponsibilty/Chain_of_Responsibilty.pdf command/Command_pattern.pdf interpreter/Interpreter.pdf singleton/tex/singleton.pdf prototype/tex/prototype.pdf factorymethod/tex/factorymethod.pdf objectpool/tex/objectpool.pdf
