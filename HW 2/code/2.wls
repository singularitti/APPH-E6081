#!/usr/bin/env wolframscript
(* ::Package:: *)

rhohe=8.1 10^4;
Na=6.02 10^23;
M=(2mproton+mneutron)Na*10^3;
hb=6.63 10^-34/2/Pi;
n=rhohe*Na/M;
m=9.109 10^-31;
mproton=1.6726 10^-27;
mneutron=1.6750 10^-27;
b=1.3806 10^-23;
kfhe=(3Pi^2 n)^(1/3);
hb^2kfhe^2/2/(2mproton+mneutron)/b
rhont=10^20;
Na=6.02 10^23;
Mnt=mneutron Na 10^3;
hb=6.63 10^-34/2/Pi;
nt=rhont*Na/Mnt;
mproton=1.6726 10^-27;
mneutron=1.6750 10^-27;
b=1.3806 10^-23;
kfnt=(3Pi^2 nt)^(1/3);
hb^2kfnt^2/2/(mneutron)/b
