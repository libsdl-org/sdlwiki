###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_exit

Finalize the HIDAPI library.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
int SDL_hid_exit(void);

```

## Return Value

Returns 0 on success and -1 on error.

## Remarks

This function frees all of the static data associated with HIDAPI. It
should be called at the end of execution to avoid memory leaks.

## Version

This function is available since SDL 2.0.18.

## Related Functions

* [SDL_hid_init](SDL_hid_init)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


