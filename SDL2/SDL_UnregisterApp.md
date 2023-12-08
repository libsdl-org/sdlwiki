###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnregisterApp

Deregister the win32 window class from an [SDL_RegisterApp](SDL_RegisterApp.md) call.

## Syntax

```c
void SDL_UnregisterApp(void);

```

## Remarks

This can be called to undo the effects of
[SDL_RegisterApp](SDL_RegisterApp.md).

Most applications do not need to, and should not, call this directly; SDL
will call it when deinitializing the video subsystem.

It is safe to call this multiple times, as long as every call is eventually
paired with a prior call to [SDL_RegisterApp](SDL_RegisterApp.md). The window
class will only be deregistered when the registration counter in
[SDL_RegisterApp](SDL_RegisterApp.md) decrements to zero through calls to this
function.

## Version

This function is available since SDL 2.0.2.

----
[CategoryAPI](CategoryAPI.md)
