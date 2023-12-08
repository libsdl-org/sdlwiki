###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_VideoInit

Initialize the video subsystem, optionally specifying a video driver.

## Syntax

```c
int SDL_VideoInit(const char *driver_name);

```

## Function Parameters

|                     |                                                                          |
| ------------------- | ------------------------------------------------------------------------ |
| **driver_name**     | the name of a video driver to initialize, or NULL for the default driver |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function initializes the video subsystem, setting up a connection to
the window manager, etc, and determines the available display modes and
pixel formats, but does not initialize a window or graphics mode.

If you use this function and you haven't used the
[SDL_INIT_VIDEO](SDL_INIT_VIDEO.md) flag with either [SDL_Init](SDL_Init.md)() or
[SDL_InitSubSystem](SDL_InitSubSystem.md)(), you should call
[SDL_VideoQuit](SDL_VideoQuit.md)() before calling [SDL_Quit](SDL_Quit.md)().

It is safe to call this function multiple times.
[SDL_VideoInit](SDL_VideoInit.md)() will call [SDL_VideoQuit](SDL_VideoQuit.md)()
itself if the video subsystem has already been initialized.

You can use [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers.md)() and
[SDL_GetVideoDriver](SDL_GetVideoDriver.md)() to find a specific
`driver_name`.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetNumVideoDrivers](SDL_GetNumVideoDrivers.md)
* [SDL_GetVideoDriver](SDL_GetVideoDriver.md)
* [SDL_InitSubSystem](SDL_InitSubSystem.md)
* [SDL_VideoQuit](SDL_VideoQuit.md)

----
[CategoryAPI](CategoryAPI.md)
