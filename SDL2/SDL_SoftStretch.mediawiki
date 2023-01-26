====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_SoftStretch =

Perform a fast, low quality, stretch blit between two surfaces of the same format.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SoftStretch(SDL_Surface * src,
                    const SDL_Rect * srcrect,
                    SDL_Surface * dst,
                    const SDL_Rect * dstrect);
</syntaxhighlight>

== Remarks ==

Please use [[SDL_BlitScaled]]() instead.

== Version ==

This function is available since SDL 2.0.0.

----
[[CategoryAPI]]


