#!/usr/bin/env wolframscript
(* ::Package:: *)

ClearAll["Global`*"]
e0=0;
e=0.05 t;
t=1;
h0:={{e0+e,t},{t,e0-e}};
h1:={{0,0},{t,0}};
hm1:={{0,t},{0,0}};
hk=Assuming[k\[Element]Reals,Simplify[Exp[I 2 k](h0+Exp[I 2 k]h1+Exp[-I 2 k]hm1)]]
eval=Assuming[k\[Element]Reals,Simplify[Re[Eigenvalues[hk]]]]
Plot[eval,{k,0,2Pi},ImageSize->Large]
