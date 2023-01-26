====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_UnregisterApp =

Deregister the win32 window class from an [[SDL_RegisterApp]] call.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_UnregisterApp(void);
</syntaxhighlight>

== Remarks ==

This can be called to undo the effects of [[SDL_RegisterApp]].

Most applications do not need to, and should not, call this directly; SDL
will call it when deinitializing the video subsystem.

It is safe to call this multiple times, as long as every call is eventually
paired with a prior call to [[SDL_RegisterApp]]. The window class will only
be deregistered when the registration counter in [[SDL_RegisterApp]]
decrements to zero through calls to this function.

== Version ==

This function is available since SDL 2.0.2.

----
[[CategoryAPI]]


