====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_acos =

Use this function to compute arc cosine of <code>x</code>.

== Syntax ==

<syntaxhighlight lang='c'>
double SDL_acos(double x);
</syntaxhighlight>

== Function Parameters ==

{|
|'''x'''
|floating point value, in radians.
|}

== Return Value ==

Returns arc cosine of <code>x</code>.

== Remarks ==

The definition of <code>y = acos(x)</code> is <code>x = cos(y)</code>.

Domain: <code>-1 <= x <= 1</code>

Range: <code>0 <= y <= Pi</code>

== Version ==

This function is available since SDL 2.0.2.

----
[[CategoryAPI]]


