====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SetJoystickVirtualHat =

Set values on an opened, virtual-joystick's hat.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SetJoystickVirtualHat(SDL_Joystick *joystick, int hat, Uint8 value);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|the virtual joystick on which to set state.
|-
|'''hat'''
|the specific hat on the virtual joystick to set.
|-
|'''value'''
|the new value for the specified hat.
|}

== Return Value ==

Returns 0 on success, -1 on error.

== Remarks ==

Please note that values set here will not be applied until the next call to
[[SDL_UpdateJoysticks]], which can either be called directly, or can be
called indirectly through various other SDL APIs, including, but not
limited to the following: [[SDL_PollEvent]], [[SDL_PumpEvents]],
[[SDL_WaitEventTimeout]], [[SDL_WaitEvent]].

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


