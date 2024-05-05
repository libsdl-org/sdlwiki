###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetProperty

Set a property on a set of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
int SDL_SetProperty(SDL_PropertiesID props, const char *name, void *value);

```

## Function Parameters

|               |                                                               |
| ------------- | ------------------------------------------------------------- |
| **props**     | the properties to modify                                      |
| **name**      | the name of the property to modify                            |
| **value**     | the new value of the property, or NULL to delete the property |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetProperty](SDL_GetProperty)
- [SDL_HasProperty](SDL_HasProperty)
- [SDL_SetBooleanProperty](SDL_SetBooleanProperty)
- [SDL_SetFloatProperty](SDL_SetFloatProperty)
- [SDL_SetNumberProperty](SDL_SetNumberProperty)
- [SDL_SetPropertyWithCleanup](SDL_SetPropertyWithCleanup)
- [SDL_SetStringProperty](SDL_SetStringProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

