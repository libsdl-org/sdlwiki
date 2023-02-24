###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_exit

Finalize the HIDAPI library.

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

## Related Functions

* [SDL_hid_init](SDL_hid_init)

----
[CategoryAPI](CategoryAPI)

