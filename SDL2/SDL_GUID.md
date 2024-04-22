###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GUID

An [SDL_GUID](SDL_GUID) is a 128-bit identifier for an input device that identifies that device across runs of SDL programs on the same platform.

## Header File

Defined in [SDL_guid.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_guid.h)

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

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

