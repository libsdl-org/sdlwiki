====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_SaveDollarTemplate =

Save a currently loaded Dollar Gesture template.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SaveDollarTemplate(SDL_GestureID gestureId,SDL_RWops *dst);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gestureId'''
|a gesture id
|-
|'''dst'''
|a [[SDL_RWops]] to save to
|}

== Return Value ==

Returns 1 on success or 0 on failure; call [[SDL_GetError]]() for more
information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_LoadDollarTemplates]]
:[[SDL_SaveAllDollarTemplates]]

----
[[CategoryAPI]]


