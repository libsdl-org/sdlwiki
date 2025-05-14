###### (This function is part of SDL_net, a separate library from SDL.)
# NET_Quit

Deinitialize the SDL_net library.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
void NET_Quit(void);
```

## Remarks

This must be called when done with the library, probably at the end of your
program.

It is safe to call this multiple times; the library will only deinitialize
once, when this function is called the same number of times as
[NET_Init](NET_Init) was successfully called.

Once you have successfully deinitialized the library, it is safe to call
[NET_Init](NET_Init) to reinitialize it for further use.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_net 3.0.0.

## See Also

- [NET_Init](NET_Init)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

