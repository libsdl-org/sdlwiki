====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SetTextureAlphaMod =

Set an additional alpha value multiplied into render copy operations.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SetTextureAlphaMod(SDL_Texture *texture, Uint8 alpha);
</syntaxhighlight>

== Function Parameters ==

{|
|'''texture'''
|the texture to update
|-
|'''alpha'''
|the source alpha value multiplied into copy operations
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

When this texture is rendered, during the copy operation the source alpha
value is modulated by this alpha value according to the following formula:

<code>srcA = srcA * (alpha / 255)</code>

Alpha modulation is not always supported by the renderer; it will return -1
if alpha modulation is not supported.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetTextureAlphaMod]]
:[[SDL_SetTextureColorMod]]

----
[[CategoryAPI]], [[CategoryRender]]


