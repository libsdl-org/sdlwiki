====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
= SDL_ReadU8 =

Use this function to read a byte from an [[SDL_RWops]].

== Syntax ==

<syntaxhighlight lang='c'>
Uint8 SDL_ReadU8(SDL_RWops * src);
</syntaxhighlight>

== Function Parameters ==

{|
|'''src'''
|the [[SDL_RWops]] to read from
|}

== Return Value ==

Returns the read byte on success or 0 on failure; call [[SDL_GetError]]()
for more information.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_WriteU8]]

----
[[CategoryAPI]], [[CategoryIO]], [[CategoryDraft]]


