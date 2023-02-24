====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!
= SDL_StartTextInput =

Start accepting Unicode text input events.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_StartTextInput(void);
</syntaxhighlight>

== Remarks ==

This function will start accepting Unicode text input events in the focused
SDL window, and start emitting [[SDL_TextInputEvent]]
([[SDL_EVENT_TEXT_INPUT]]) and [[SDL_TextEditingEvent]]
([[SDL_EVENT_TEXT_EDITING]]) events. Please use this function in pair with
[[SDL_StopTextInput]]().

On some platforms using this function activates the screen keyboard.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_SetTextInputRect]]
:[[SDL_StopTextInput]]

----
[[CategoryAPI]], [[CategoryKeyboard]], [[CategoryDraft]]


