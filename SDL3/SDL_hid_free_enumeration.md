###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_hid_free_enumeration

Free an enumeration linked list.

## Header File

Defined in [<SDL3/SDL_hidapi.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hidapi.h)

## Syntax

```c
void SDL_hid_free_enumeration(SDL_hid_device_info *devs);
```

## Function Parameters

|                                              |          |                                                                                            |
| -------------------------------------------- | -------- | ------------------------------------------------------------------------------------------ |
| [SDL_hid_device_info](SDL_hid_device_info) * | **devs** | pointer to a list of struct_device returned from [SDL_hid_enumerate](SDL_hid_enumerate)(). |

## Remarks

This function frees a linked list created by
[SDL_hid_enumerate](SDL_hid_enumerate)().

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHIDAPI](CategoryHIDAPI)

