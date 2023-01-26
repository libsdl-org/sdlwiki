====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!
= SDL_SetTextInputRect =

Set the rectangle used to type Unicode text inputs.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_SetTextInputRect(const SDL_Rect *rect);
</syntaxhighlight>

== Function Parameters ==

{|
|'''rect'''
|the [[SDL_Rect]] structure representing the rectangle to receive text (ignored if NULL)
|}

== Remarks ==

To start text input in a given location, this function is intended to be
called before [[SDL_StartTextInput]], although some platforms support
moving the rectangle even while text input (and a composition) is active.

Note: If you want to use the system native IME window, try setting hint
'''[[SDL_HINT_IME_SHOW_UI]]''' to '''1''', otherwise this function won't
give you any feedback.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_StartTextInput]]

----
[[CategoryAPI]], [[CategoryKeyboard]], [[CategoryDraft]]


