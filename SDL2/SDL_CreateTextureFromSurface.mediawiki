====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_CreateTextureFromSurface =

Create a texture from an existing surface.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Texture * SDL_CreateTextureFromSurface(SDL_Renderer * renderer, SDL_Surface * surface);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the rendering context
|-
|'''surface'''
|the [[SDL_Surface]] structure containing pixel data used to fill the texture
|}

== Return Value ==

Returns the created texture or NULL on failure; call [[SDL_GetError]]() for
more information.

== Remarks ==

The surface is not modified or freed by this function.

The [[SDL_TextureAccess]] hint for the created texture is
<code>[[SDL_TEXTUREACCESS_STATIC]]</code>.

The pixel format of the created texture may be different from the pixel
format of the surface. Use [[SDL_QueryTexture]]() to query the pixel format
of the texture.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateTexture]]
:[[SDL_DestroyTexture]]
:[[SDL_QueryTexture]]

----
[[CategoryAPI]]


