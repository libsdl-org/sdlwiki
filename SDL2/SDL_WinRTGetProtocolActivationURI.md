# SDL_WinRTGetProtocolActivationURI

Get the protocol activation URI if the app was launched via protocol activation.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
char * SDL_WinRTGetProtocolActivationURI(void);
```

## Return Value

(char *) Returns the protocol activation URI as a UTF-8 string that must be
freed with [SDL_free](SDL_free)(), or NULL if the app was not activated via
protocol or the URI was already retrieved.

## Remarks

When a UWP/WinRT app is launched via a custom URI scheme (e.g.,
myapp://action?param=value), this function retrieves the full activation
URI string.

The URI is only available once per activation - after the first successful
call, subsequent calls will return NULL. This ensures the URI is processed
only once.

## Version

This function is available since SDL 2.33.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

