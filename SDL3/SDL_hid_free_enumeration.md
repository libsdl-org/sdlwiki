###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_free_enumeration

Free an enumeration Linked List 

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

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

