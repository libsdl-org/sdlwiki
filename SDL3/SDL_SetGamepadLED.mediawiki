====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SetGamepadLED =

Update a gamepad's LED color.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SetGamepadLED(SDL_Gamepad *gamepad, Uint8 red, Uint8 green, Uint8 blue);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamepad'''
|The gamepad to update
|-
|'''red'''
|The intensity of the red LED
|-
|'''green'''
|The intensity of the green LED
|-
|'''blue'''
|The intensity of the blue LED
|}

== Return Value ==

Returns 0, or -1 if this gamepad does not have a modifiable LED

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


