###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_free_enumeration

Free an enumeration Linked List 

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_hid_free_enumeration(SDL_hid_device_info *devs);

```

## Function Parameters

|              |                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------ |
| **devs**     | Pointer to a list of struct_device returned from [SDL_hid_enumerate](SDL_hid_enumerate)(). |

## Remarks

This function frees a linked list created by
[SDL_hid_enumerate](SDL_hid_enumerate)().

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI)

