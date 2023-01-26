====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!
= SDL_HapticIndex =

Get the index of a haptic device.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_HapticIndex(SDL_Haptic * haptic);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|the [[SDL_Haptic]] device to query
|}

== Return Value ==

Returns the index of the specified haptic device or a negative error code
on failure; call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_HapticOpen]]
:[[SDL_HapticOpened]]

----
[[CategoryAPI]], [[CategoryForceFeedback]], [[CategoryDraft]]


