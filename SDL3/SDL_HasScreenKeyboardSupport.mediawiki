====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
= SDL_HasScreenKeyboardSupport =

Check whether the platform has screen keyboard support.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_HasScreenKeyboardSupport(void);
</syntaxhighlight>

== Return Value ==

Returns [[SDL_TRUE]] if the platform has some screen keyboard support or
[[SDL_FALSE]] if not.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_StartTextInput]]
:[[SDL_ScreenKeyboardShown]]

----
[[CategoryAPI]], [[CategoryKeyboard]], [[CategoryDraft]]
<!-- #See the Style Guide for instructions on editing the footer. -->


