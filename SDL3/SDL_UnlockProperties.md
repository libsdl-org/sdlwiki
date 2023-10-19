###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnlockProperties

Unlock a set of properties 

## Syntax

```c
void SDL_UnlockProperties(SDL_PropertiesID props);

```

## Function Parameters

|               |                          |
| ------------- | ------------------------ |
| **props**     | the properties to unlock |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LockProperties](SDL_LockProperties)

----
[CategoryAPI](CategoryAPI)

