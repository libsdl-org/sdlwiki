====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetGamepadBindForAxis =

Get the SDL joystick layer binding for a gamepad axis mapping.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_GamepadBinding SDL_GetGamepadBindForAxis(SDL_Gamepad *gamepad, SDL_GamepadAxis axis);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamepad'''
|a gamepad
|-
|'''axis'''
|an axis enum value (one of the [[SDL_GamepadAxis]] values)
|}

== Return Value ==

Returns a [[SDL_GamepadBinding]] describing the bind. On failure (like the
given Controller axis doesn't exist on the device), its
<code>.bindType</code> will be <code>[[SDL_GAMEPAD_BINDTYPE_NONE]]</code>.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetGamepadBindForButton]]

----
[[CategoryAPI]]


