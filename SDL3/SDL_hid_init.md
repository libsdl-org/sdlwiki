###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_init

Initialize the HIDAPI library.

## Syntax

```c
int SDL_hid_init(void);

```

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function initializes the HIDAPI library. Calling it is not strictly
necessary, as it will be called automatically by
[SDL_hid_enumerate](SDL_hid_enumerate)() and any of the
[SDL_hid_open_](SDL_hid_open_)*() functions if it is needed. This function
should be called at the beginning of execution however, if there is a
chance of HIDAPI handles being opened by different threads simultaneously.

Each call to this function should have a matching call to
[SDL_hid_exit](SDL_hid_exit)()

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_hid_exit](SDL_hid_exit)

----
[CategoryAPI](CategoryAPI)

