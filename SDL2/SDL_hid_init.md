###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_init

Initialize the HIDAPI library.

## Syntax

```c
int SDL_hid_init(void);

```

## Return Value

Returns 0 on success and -1 on error.

## Remarks

This function initializes the HIDAPI library. Calling it is not strictly
necessary, as it will be called automatically by
[SDL_hid_enumerate](SDL_hid_enumerate.md)() and any of the
[SDL_hid_open_](SDL_hid_open_.md)*() functions if it is needed. This function
should be called at the beginning of execution however, if there is a
chance of HIDAPI handles being opened by different threads simultaneously.

Each call to this function should have a matching call to
[SDL_hid_exit](SDL_hid_exit.md)()

## Version

This function is available since SDL 2.0.18.

## Related Functions

* [SDL_hid_exit](SDL_hid_exit.md)

----
[CategoryAPI](CategoryAPI.md)
