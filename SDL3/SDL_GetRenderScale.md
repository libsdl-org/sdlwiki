====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetRenderScale =

Get the drawing scale for the current target.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_GetRenderScale(SDL_Renderer *renderer, float *scaleX, float *scaleY);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the renderer from which drawing scale should be queried
|-
|'''scaleX'''
|a pointer filled in with the horizontal scaling factor
|-
|'''scaleY'''
|a pointer filled in with the vertical scaling factor
|}

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_SetRenderScale]]

----
[[CategoryAPI]]


