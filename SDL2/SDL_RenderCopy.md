====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderCopy =

Copy a portion of the texture to the current rendering target.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_RenderCopy(SDL_Renderer * renderer,
                   SDL_Texture * texture,
                   const SDL_Rect * srcrect,
                   const SDL_Rect * dstrect);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the rendering context
|-
|'''texture'''
|the source texture
|-
|'''srcrect'''
|the source [[SDL_Rect]] structure or NULL for the entire texture
|-
|'''dstrect'''
|the destination [[SDL_Rect]] structure or NULL for the entire rendering target; the texture will be stretched to fill the given rectangle
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

The texture is blended with the destination based on its blend mode set
with [[SDL_SetTextureBlendMode]]().

The texture color is affected based on its color modulation set by
[[SDL_SetTextureColorMod]]().

The texture alpha is affected based on its alpha modulation set by
[[SDL_SetTextureAlphaMod]]().

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_RenderCopyEx]]
:[[SDL_SetTextureAlphaMod]]
:[[SDL_SetTextureBlendMode]]
:[[SDL_SetTextureColorMod]]

----
[[CategoryAPI]]


