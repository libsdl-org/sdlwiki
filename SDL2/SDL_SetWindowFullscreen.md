====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_SetWindowFullscreen =

Set a window's fullscreen state.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SetWindowFullscreen(SDL_Window * window,
                            Uint32 flags);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to change
|-
|'''flags'''
|<code>[[SDL_WINDOW_FULLSCREEN]]</code>, <code>[[SDL_WINDOW_FULLSCREEN_DESKTOP]]</code> or 0
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

<code>flags</code> may be <code>[[SDL_WINDOW_FULLSCREEN]]</code>, for
"real" fullscreen with a videomode change;
<code>[[SDL_WINDOW_FULLSCREEN_DESKTOP]]</code> for "fake" fullscreen that
takes the size of the desktop; and 0 for windowed mode.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetWindowDisplayMode]]
:[[SDL_SetWindowDisplayMode]]

----
[[CategoryAPI]]


