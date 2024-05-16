###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GUID

An [SDL_GUID](SDL_GUID) is a 128-bit identifier for an input device that identifies that device across runs of SDL programs on the same platform.

## Header File

Defined in [<SDL3/SDL_guid.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_guid.h)

## Syntax

```c
typedef struct SDL_GUID {
    Uint8 data[16];
} SDL_GUID;
```

## Remarks

If the device is detached and then re-attached to a different port, or if
the base system is rebooted, the device should still report the same GUID.

GUIDs are as precise as possible but are not guaranteed to distinguish
physically distinct but equivalent devices. For example, two game
controllers from the same vendor with the same product ID and revision may
have the same GUID.

GUIDs may be platform-dependent (i.e., the same device may report different
GUIDs on different operating systems).

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGUID](CategoryGUID)

