###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetHapticFromInstanceID

Get the [SDL_Haptic](SDL_Haptic) associated with an instance ID, if it has been opened.

## Syntax

```c
SDL_Haptic* SDL_GetHapticFromInstanceID(SDL_HapticID instance_id);

```

## Function Parameters

|                     |                                                         |
| ------------------- | ------------------------------------------------------- |
| **instance_id**     | the instance ID to get the [SDL_Haptic](SDL_Haptic) for |

## Return Value

Returns an [SDL_Haptic](SDL_Haptic) on success or NULL on failure or if it
hasn't been opened yet; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

