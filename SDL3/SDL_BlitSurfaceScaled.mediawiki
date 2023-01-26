====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_BlitSurfaceScaled =

Perform a scaled surface copy to a destination surface.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_BlitSurfaceScaled
    (SDL_Surface *src, const SDL_Rect *srcrect,
    SDL_Surface *dst, SDL_Rect *dstrect);
</syntaxhighlight>

== Function Parameters ==

{|
|'''src'''
|the [[SDL_Surface]] structure to be copied from
|-
|'''srcrect'''
|the [[SDL_Rect]] structure representing the rectangle to be copied
|-
|'''dst'''
|the [[SDL_Surface]] structure that is the blit target
|-
|'''dstrect'''
|the [[SDL_Rect]] structure representing the rectangle that is copied into
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_BlitScaled]]

----
[[CategoryAPI]]


