====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_Quit =

Deinitialize SDL_ttf.

== Syntax ==

<syntaxhighlight lang='c'>
void TTF_Quit(void);
</syntaxhighlight>

== Remarks ==

You must call this when done with the library, to free internal resources.
It is safe to call this when the library isn't initialized, as it will just
return immediately.

Once you have as many quit calls as you have had successful calls to
[[TTF_Init]], the library will actually deinitialize.

Please note that this does not automatically close any fonts that are still
open at the time of deinitialization, and it is possibly not safe to close
them afterwards, as parts of the library will no longer be initialized to
deal with it. A well-written program should call [[TTF_CloseFont]]() on any
open fonts before calling this function!

== Version ==

This function is available since SDL_ttf 2.0.12.

----
[[CategoryAPI]]


