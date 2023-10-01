#!/usr/bin/env wolframscript
(* ::Package:: *)

Plot[{x^2,(x-1)^2,1+x^2,(x+1)^2,(x-1)^2+1},{x,0,.5},PlotLegends->"Expressions",AspectRatio->Full]


Plot[{1/4+y^2,1/4+(y-1)^2,1/4+(y+1)^2,9/4+y^2},{y,0,.5},PlotLegends->"Expressions",AspectRatio->Full]


Plot[{2x^2,(x-1)^2+x^2,(x+1)^2+x^2,2(x-1)^2},{x,0.5,0},PlotLegends->"Expressions",AspectRatio->Full]
