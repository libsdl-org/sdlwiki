====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetCursor =

Get the active cursor.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Cursor* SDL_GetCursor(void);
</syntaxhighlight>

== Return Value ==

Returns the active cursor or NULL if there is no mouse.

== Remarks ==

This function returns a pointer to the current cursor which is owned by the
library. It is not necessary to free the cursor with [[SDL_FreeCursor]]().

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_SetCursor]]

----
[[CategoryAPI]]


