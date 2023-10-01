#!/usr/bin/env wolframscript
(* ::Package:: *)

ee[k]:=e0+1/2+1/2*Sqrt[1+8t^2(1+Cos[k a])]


m=D[ee[k],k]


-((2 a t^2 Sin[a k])/Sqrt[1+8 t^2 (1+Cos[a k])])/.{k->1/a*ArcCos[(4e^2-1)/8/t^2-1]}//Assuming[a>0&&e>0&&t>0,Simplify[#]]&
