# SDL_LockProperties

Lock a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
bool SDL_LockProperties(SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                         |
| ------------------------------------ | --------- | ----------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to lock. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Obtain a multi-threaded lock for these properties. Other threads will wait
while trying to lock these properties until they are unlocked. Properties
must be unlocked before they are destroyed.

The lock is automatically taken when setting individual properties, this
function is only needed when you want to set several properties atomically
or want to guarantee that properties being queried aren't freed in another
thread.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_UnlockProperties](SDL_UnlockProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

