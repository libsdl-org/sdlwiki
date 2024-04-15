###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_exit

Finalize the HIDAPI library.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hidapi.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
int SDL_hid_exit(void);

```

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function frees all of the static data associated with HIDAPI. It
should be called at the end of execution to avoid memory leaks.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_hid_init](SDL_hid_init)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

