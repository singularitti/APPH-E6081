#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]
a=1;
Assuming[k1\[Element]Reals&&k2\[Element]Reals,FullSimplify[eig=Sqrt[2.5^2(Exp[I(-k1)a]+Exp[I (1/2k1-Sqrt[3]/2k2)a]+Exp[I (1/2k1+Sqrt[3]/2k2)a])* (Exp[I (k1)a]+Exp[I (-1/2 k1+Sqrt[3]/2 k2)a]+Exp[I (-1/2 k1-Sqrt[3]/2 k2)a])]]]


3+4 Cos[(3 k1)/2] Cos[(Sqrt[3] k2)/2]+2 Cos[Sqrt[3] k2]/.{k1->(k1+dk1),k2->(k2+dk2)}//TrigReduce//FullSimplify


((4(1-1/2 9/4a^2(k1+dk1)^2)(1-1/2 3/4a^2(k2+dk2)^2)//Expand)+2(1-1/2*3(k2+dk2)^2)+3//Simplify)/.{k1->2Pi/Sqrt[3],k2->2Pi/3/Sqrt[3]}//N
