====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HapticClose =

Close a haptic device previously opened with [[SDL_HapticOpen]]().

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_HapticClose(SDL_Haptic * haptic);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|the [[SDL_Haptic]] device to close
|}

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_HapticOpen]]

----
[[CategoryAPI]]


