###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_Quit

Deinitialize the SDL_net library.

## Syntax

```c
void SDLNet_Quit(void);

```

## Remarks

This must be called when done with the library, probably at the end of your
program.

It is safe to call this multiple times; the library will only deinitialize
once, when this function is called the same number of times as
[SDLNet_Init](SDLNet_Init) was successfully called.

Once you have successfully deinitialized the library, it is safe to call
[SDLNet_Init](SDLNet_Init) to reinitialize it for further use.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

## Related Functions

* [SDLNet_Quit](SDLNet_Quit)

----
[CategoryAPI](CategoryAPI)

