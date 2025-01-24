# SDL_RegisterApp

Register a win32 window class for SDL's use.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
bool SDL_RegisterApp(const char *name, Uint32 style, void *hInst);
```

## Function Parameters

|                  |           |                                                                                                                                                      |
| ---------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| const char *     | **name**  | the window class name, in UTF-8 encoding. If NULL, SDL currently uses "[SDL_app](SDL_app)" but this isn't guaranteed.                                |
| [Uint32](Uint32) | **style** | the value to use in WNDCLASSEX::style. If `name` is NULL, SDL currently uses `(CS_BYTEALIGNCLIENT | CS_OWNDC)` regardless of what is specified here. |
| void *           | **hInst** | the HINSTANCE to use in WNDCLASSEX::hInstance. If zero, SDL will use `GetModuleHandle(NULL)` instead.                                                |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This can be called to set the application window class at startup. It is
safe to call this multiple times, as long as every call is eventually
paired with a call to [SDL_UnregisterApp](SDL_UnregisterApp), but a second
registration attempt while a previous registration is still active will be
ignored, other than to increment a counter.

Most applications do not need to, and should not, call this directly; SDL
will call it when initializing the video subsystem.

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

