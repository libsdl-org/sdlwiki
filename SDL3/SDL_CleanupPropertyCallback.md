###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CleanupPropertyCallback

A callback used to free resources when a property is deleted.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
typedef void (SDLCALL *SDL_CleanupPropertyCallback)(void *userdata, void *value);
```

## Function Parameters

|                  |                                                   |
| ---------------- | ------------------------------------------------- |
| **userdata**     | an app-defined pointer passed to the callback.    |
| **value**        | the pointer assigned to the property to clean up. |

## Remarks

This should release any resources associated with `value` that are no
longer needed.

This callback is set per-property. Different properties in the same set can
have different cleanup callbacks.

This callback will be called _during_
[SDL_SetPropertyWithCleanup](SDL_SetPropertyWithCleanup) if the function
fails for any reason.

## Thread Safety

This callback may fire without any locks held; if this is a concern, the
app should provide its own locking.

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_SetPropertyWithCleanup](SDL_SetPropertyWithCleanup)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryProperties](CategoryProperties)

