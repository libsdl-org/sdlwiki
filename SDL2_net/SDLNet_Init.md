###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_Init

Initialize SDL_net.

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
int SDLNet_Init(void);
```

## Return Value

(int) Returns 0 on success, -1 on error.

## Remarks

You must successfully call this function before it is safe to call any
other function in this library, with one exception: a human-readable error
message can be retrieved from [SDLNet_GetError](SDLNet_GetError)() if this
function fails.

SDL must be initialized before calls to functions in this library, because
this library uses utility functions from the SDL library.

It is safe to call this more than once; the library keeps a counter of init
calls, and decrements it on each call to [SDLNet_Quit](SDLNet_Quit), so you
must pair your init and quit calls.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

