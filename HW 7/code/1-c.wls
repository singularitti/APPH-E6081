#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]
ep=0;a=1;t=0.25;e=ep+1/2-1/2Sqrt[Cos[k a/2]^2+1];
h={{ep+1,t(1+Exp[-I k a])},{t(1+Exp[I k a]),ep}};
eigVector=Eigenvectors[h]


eigVec1=eigVector[[1]];eigVec2=eigVector[[2]];
eigVec1=eigVec1/Sqrt[eigVec1[[1]]^2+eigVec1[[2]]^2](*Normalized eigenvector*);
eigVec2=eigVec2/Sqrt[eigVec2[[1]]^2+eigVec2[[2]]^2];


Plot[Conjugate[eigVec1[[1]]]eigVec1[[1]]/(Conjugate[eigVec1[[2]]]eigVec1[[2]])//Simplify,{k,-2,2}]


g=-2/Pi 16e/Sqrt[1-(8e^2-3)^2];
Plot[g*Assuming[k\[Element]Reals,FullSimplify[Dot[Conjugate[eigVec2],eigVec2]]],{k,-2,2}]


Plot[Assuming[k\[Element]Reals,FullSimplify[Dot[Conjugate[eigVec2],eigVec2]]],{k,-2,2}]


Plot[Re[Conjugate[eigVec1[[1]]]eigVec1[[1]]*g],{k,-2,2}]
