###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_Linked_Version

Query the version of SDL_net that the program is linked against.

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
const SDLNet_version * SDLNet_Linked_Version(void);
```

## Return Value

(const [SDLNet_version](SDLNet_version) *) Returns a pointer to the version
information.

## Remarks

This function gets the version of the dynamically linked SDL_net library.
This is separate from the SDL_NET_VERSION() macro, which tells you what
version of the SDL_net headers you compiled against.

This returns static internal data; do not free or modify it!

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

