====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_DestroyWindow =

Destroy a window.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_DestroyWindow(SDL_Window * window);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to destroy
|}

== Remarks ==

If <code>window</code> is NULL, this function will return immediately after
setting the SDL error message to "Invalid window". See [[SDL_GetError]]().

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateWindow]]
:[[SDL_CreateWindowFrom]]

----
[[CategoryAPI]]


