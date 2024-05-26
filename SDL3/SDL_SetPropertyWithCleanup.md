###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetPropertyWithCleanup

Set a property on a set of properties with a cleanup function that is called when the property is deleted.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
int SDL_SetPropertyWithCleanup(SDL_PropertiesID props, const char *name, void *value, SDL_CleanupPropertyCallback cleanup, void *userdata);

```

## Function Parameters

|                  |                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------- |
| **props**        | the properties to modify                                                               |
| **name**         | the name of the property to modify                                                     |
| **value**        | the new value of the property, or NULL to delete the property                          |
| **cleanup**      | the function to call when this property is deleted, or NULL if no cleanup is necessary |
| **userdata**     | a pointer that is passed to the cleanup function                                       |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The cleanup function is also called if setting the property fails for any
reason.

For simply setting basic data types, like numbers, bools, or strings, use
[SDL_SetNumberProperty](SDL_SetNumberProperty),
[SDL_SetBooleanProperty](SDL_SetBooleanProperty), or
[SDL_SetStringProperty](SDL_SetStringProperty) instead, as those functions
will handle cleanup on your behalf. This function is only for more complex,
custom data.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetProperty](SDL_GetProperty)
- [SDL_SetProperty](SDL_SetProperty)
- [SDL_CleanupPropertyCallback](SDL_CleanupPropertyCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

