====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_DelEventWatch =

Remove an event watch callback added with [[SDL_AddEventWatch]]().

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_DelEventWatch(SDL_EventFilter filter,
                       void *userdata);
</syntaxhighlight>

== Function Parameters ==

{|
|'''filter'''
|the function originally passed to [[SDL_AddEventWatch]]()
|-
|'''userdata'''
|the pointer originally passed to [[SDL_AddEventWatch]]()
|}

== Remarks ==

This function takes the same input as [[SDL_AddEventWatch]]() to identify
and delete the corresponding callback.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_AddEventWatch]]

----
[[CategoryAPI]]


