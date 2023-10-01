#!/usr/bin/env wolframscript
(* ::Package:: *)

ClearAll["Global`*"]
h={{ep+1,t(1+Exp[-I k a])},{t(1+Exp[I k a]),ep}};


Eigenvalues[h]//FullSimplify
