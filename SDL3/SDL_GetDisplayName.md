====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
= SDL_GetDisplayName =

Get the name of a display in UTF-8 encoding.

== Syntax ==

<syntaxhighlight lang='c'>
const char* SDL_GetDisplayName(SDL_DisplayID displayID);
</syntaxhighlight>

== Function Parameters ==

{|
|'''displayID'''
|the instance ID of the display to query
|}

== Return Value ==

Returns the name of a display or NULL on failure; call [[SDL_GetError]]()
for more information.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetDisplays]]

----
[[CategoryAPI]], [[CategoryVideo]], [[CategoryDraft]]
<!-- #See the Style Guide for instructions on editing the footer. -->


