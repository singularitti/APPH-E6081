#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]
eg1=Series[1/2+1/2+1/2Sqrt[1+8t^2(Cos[k]+1)],{t,0,2}]//Normal
eg2=Series[1/2+1/2-1/2Sqrt[1+8t^2(Cos[k]+1)],{t,0,2}]//Normal
Plot[{eg1,eg2}/.t->0.25,{k,-Pi,Pi}]



