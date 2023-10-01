#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]
t(1+Exp[I 2Pi k1]+Exp[I 2Pi (k1+k2)])*t(Exp[I 2Pi (1/3k1+2/3k2)]+Exp[I 2Pi(1/3k1-1/3k2)]+Exp[I 2Pi(2/3k1-1/3k2)])//Sqrt//Simplify[#//ExpToTrig]&


H={{0,t(1+Exp[I 2Pi k1]+Exp[I 2Pi (k1+k2)])},{t(Exp[I 2Pi (1/3k1+2/3k2)]+Exp[I 2Pi(1/3k1-1/3k2)]+Exp[I 2Pi(-2/3k1-1/3k2)]),0}}
Eigenvalues[H]



