###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_Quit

Deinitialize SDL_net.

## Syntax

```c
void SDLNet_Quit(void);

```

## Remarks

You must call this when done with the library, to free internal resources.
It is safe to call this when the library isn't initialized, as it will just
return immediately.

Once you have as many quit calls as you have had successful calls to
[SDLNet_Init](SDLNet_Init.md), the library will actually deinitialize.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
