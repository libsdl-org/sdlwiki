====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_AttachVirtualJoystick =

Attach a new virtual joystick.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_JoystickID SDL_AttachVirtualJoystick(SDL_JoystickType type,
                              int naxes,
                              int nbuttons,
                              int nhats);
</syntaxhighlight>

== Return Value ==

Returns the joystick instance ID, or 0 if an error occurred; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


