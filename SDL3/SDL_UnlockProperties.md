# SDL_UnlockProperties

Unlock a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
void SDL_UnlockProperties(SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                           |
| ------------------------------------ | --------- | ------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to unlock. |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LockProperties](SDL_LockProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

