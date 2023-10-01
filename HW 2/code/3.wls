#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"];
hb= 1.0551972726992663`*^-34;
l=4.1 10^-10;
L=2l;
m=9.109000000000001`*^-31;
n^2 hb^2Pi^2/2/m/L^2(*n level*)/.n->3
5.86*10^28*(10^-4)^2*L/(10^-4)^2*2Pi*hb^2/2/m(*xy E_F*)
nn/(10^-4)^2*2Pi*hb^2/2/m(*xy E_F*)
4 hb^2Pi^2/2/m/l^2
Plot[m/hb^2/Pi,{e,0,10},AxesLabel->{"E(J)","g(E)(\!\(\*SuperscriptBox[\(s\), \(2\)]\)\!\(\*SuperscriptBox[\(kg\), \(-1\)]\)\!\(\*SuperscriptBox[\(m\), \(-4\)]\))"}]
