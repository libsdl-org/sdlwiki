====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_SetModState =

Set the current key modifier state for the keyboard.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_SetModState(SDL_Keymod modstate);
</syntaxhighlight>

== Function Parameters ==

{|
|'''modstate'''
|the desired [[SDL_Keymod]] for the keyboard
|}

== Remarks ==

The inverse of [[SDL_GetModState]](), [[SDL_SetModState]]() allows you to
impose modifier key states on your application. Simply pass your desired
modifier states into <code>modstate</code>. This value may be a bitwise,
OR'd combination of [[SDL_Keymod]] values.

This does not change the keyboard state, only the key modifier flags that
SDL reports.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetModState]]

----
[[CategoryAPI]]


