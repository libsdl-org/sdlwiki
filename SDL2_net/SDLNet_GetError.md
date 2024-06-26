###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_GetError

Get the latest error message from SDL_net.

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
const char * SDLNet_GetError(void);
```

## Return Value

(const char *) Returns the last set error message in UTF-8 encoding.

## Remarks

The error message, depending on how SDL_net was built, may or may not be
thread-local data. Sometimes things will set an error message when no
failure was reported; the error string is only meaningful right after a
public API reports a failure, and should be ignored otherwise.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

