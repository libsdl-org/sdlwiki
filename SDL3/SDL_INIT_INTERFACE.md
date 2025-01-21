###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_INIT_INTERFACE

A macro to initialize an SDL interface.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_INIT_INTERFACE(iface)               \
    do {                                        \
        SDL_zerop(iface);                       \
        (iface)->version = sizeof(*(iface));    \
    } while (0)
```

## Remarks

This macro will initialize an SDL interface structure and should be called
before you fill out the fields with your implementation.

You can use it like this:

```c
SDL_IOStreamInterface iface;

SDL_INIT_INTERFACE(&iface);

// Fill in the interface function pointers with your implementation
iface.seek = ...

stream = SDL_OpenIO(&iface, NULL);
```

If you are using designated initializers, you can use the size of the
interface as the version, e.g.

```c
SDL_IOStreamInterface iface = {
    .version = sizeof(iface),
    .seek = ...
};
stream = SDL_OpenIO(&iface, NULL);
```

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_IOStreamInterface](SDL_IOStreamInterface)
- [SDL_StorageInterface](SDL_StorageInterface)
- [SDL_VirtualJoystickDesc](SDL_VirtualJoystickDesc)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

