#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]
Assuming[k1\[Element]Reals&&k2\[Element]Reals,FullSimplify[eig=Sqrt[2.5^2(Exp[I(-k1)]+Exp[I (1/2k1-Sqrt[3]/2k2)]+Exp[I (1/2k1+Sqrt[3]/2k2)])* (Exp[I (k1)]+Exp[I (-1/2 k1+Sqrt[3]/2 k2)]+Exp[I (-1/2 k1-Sqrt[3]/2 k2)])]]]


R=3;
f=Interpolation[Table[{a,R {Cos[a],Sin[a]}},{a,-\[Pi],\[Pi],\[Pi]/3}],InterpolationOrder->1];


Plot3D[{eig,-eig},{k1,-3,3},{k2,-3,3},RegionFunction->Function[{x,y},Norm@{x,y}<Norm@f[ArcTan[y,x]]],PlotPoints->50]
