====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetRectEnclosingPoints =

Calculate a minimal rectangle enclosing a set of points.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_GetRectEnclosingPoints(const SDL_Point * points,
                           int count,
                           const SDL_Rect * clip,
                           SDL_Rect * result);
</syntaxhighlight>

== Function Parameters ==

{|
|'''points'''
|an array of [[SDL_Point]] structures representing points to be enclosed
|-
|'''count'''
|the number of structures in the <code>points</code> array
|-
|'''clip'''
|an [[SDL_Rect]] used for clipping or NULL to enclose all points
|-
|'''result'''
|an [[SDL_Rect]] structure filled in with the minimal enclosing rectangle
|}

== Return Value ==

Returns [[SDL_TRUE]] if any points were enclosed or [[SDL_FALSE]] if all
the points were outside of the clipping rectangle.

== Remarks ==

If <code>clip</code> is not NULL then only points inside of the clipping
rectangle are considered.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


