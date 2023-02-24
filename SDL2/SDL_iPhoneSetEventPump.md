====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_iPhoneSetEventPump =

Use this function to enable or disable the SDL event pump on Apple iOS.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_iPhoneSetEventPump(SDL_bool enabled);
</syntaxhighlight>

== Function Parameters ==

{|
|'''enabled'''
|[[SDL_TRUE]] to enable the event pump, [[SDL_FALSE]] to disable it
|}

== Remarks ==

This function is only available on Apple iOS.

This functions is also accessible using the macro [[SDL_iOSSetEventPump]]()
since SDL 2.0.4.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_iPhoneSetAnimationCallback]]

----
[[CategoryAPI]]


