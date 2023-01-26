====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!
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

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetModState]]

----
[[CategoryAPI]], [[CategoryKeyboard]], [[CategoryDraft]]


