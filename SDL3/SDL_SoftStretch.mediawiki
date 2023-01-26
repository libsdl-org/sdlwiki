====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SoftStretch =

Perform a fast, low quality, stretch blit between two surfaces of the same format.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SoftStretch(SDL_Surface *src,
                    const SDL_Rect *srcrect,
                    SDL_Surface *dst,
                    const SDL_Rect *dstrect);
</syntaxhighlight>

== Remarks ==

Please use [[SDL_BlitScaled]]() instead.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


