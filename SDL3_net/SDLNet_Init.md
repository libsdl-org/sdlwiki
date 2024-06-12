###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_Init

Initialize the SDL_net library.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int SDLNet_Init(void);
```

## Return Value

(int) Returns 0 on success, -1 on error; call SDL_GetError() for details.

## Remarks

This must be successfully called once before (almost) any other SDL_net
function can be used.

It is safe to call this multiple times; the library will only initialize
once, and won't deinitialize until [SDLNet_Quit](SDLNet_Quit)() has been
called a matching number of times. Extra attempts to init report success.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_net 3.0.0.

## See Also

- [SDLNet_Quit](SDLNet_Quit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

