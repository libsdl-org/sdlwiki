###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RegisterApp

Register a win32 window class for SDL's use.

## Header File

Defined in [SDL_main.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_main.h)

## Syntax

```c
int SDL_RegisterApp(const char *name, Uint32 style, void *hInst);
```

## Function Parameters

|              |           |                                                                                                                                                      |
| ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| const char * | **name**  | the window class name, in UTF-8 encoding. If NULL, SDL currently uses "[SDL_app](SDL_app)" but this isn't guaranteed.                                |
| Uint32       | **style** | the value to use in WNDCLASSEX::style. If `name` is NULL, SDL currently uses `(CS_BYTEALIGNCLIENT | CS_OWNDC)` regardless of what is specified here. |
| void *       | **hInst** | the HINSTANCE to use in WNDCLASSEX::hInstance. If zero, SDL will use `GetModuleHandle(NULL)` instead.                                                |

## Return Value

(int) Returns 0 on success, -1 on error. [SDL_GetError](SDL_GetError)() may
have details.

## Remarks

This can be called to set the application window class at startup. It is
safe to call this multiple times, as long as every call is eventually
paired with a call to [SDL_UnregisterApp](SDL_UnregisterApp), but a second
registration attempt while a previous registration is still active will be
ignored, other than to increment a counter.

Most applications do not need to, and should not, call this directly; SDL
will call it when initializing the video subsystem.

## Version

This function is available since SDL 2.0.2.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

