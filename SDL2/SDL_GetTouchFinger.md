====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetTouchFinger =

Get the finger object for specified touch device ID and finger index.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Finger * SDL_GetTouchFinger(SDL_TouchID touchID, int index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''touchID'''
|the ID of the requested touch device
|-
|'''index'''
|the index of the requested finger
|}

== Return Value ==

Returns a pointer to the [[SDL_Finger]] object or NULL if no object at the
given ID and index could be found.

== Remarks ==

The returned resource is owned by SDL and should not be deallocated.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_RecordGesture]]

----
[[CategoryAPI]]


