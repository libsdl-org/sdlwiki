====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_EventEnabled =

Query the state of processing events by type.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_EventEnabled(Uint32 type);
</syntaxhighlight>

== Function Parameters ==

{|
|'''type'''
|the type of event; see [[SDL_EventType]] for details
|}

== Return Value ==

Returns [[SDL_TRUE]] if the event is being processed, [[SDL_FALSE]]
otherwise.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_SetEventEnabled]]

----
[[CategoryAPI]]


