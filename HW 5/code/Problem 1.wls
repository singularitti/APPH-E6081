#!/usr/bin/env wolframscript
(* ::Package:: *)

v004=-0.04Exp[2Pi I {{1,0},{-1,0},{0,1},{0,-1}} . {x,0}]//Total
v002=-0.02Exp[2Pi I {{1,1},{-1,-1},{-1,1},{1,-1}} . {x,0}]//Total
ListPlot[Table[{x,v004+v002//Re},{x,0,3,0.01}],PlotRange->All]


0 + v004+v002//FullSimplify
