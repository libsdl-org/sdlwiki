###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetStringProperty

Set a string property on a set of properties 

## Syntax

```c
int SDL_SetStringProperty(SDL_PropertiesID props, const char *name, const char *value);

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

## Related Functions

* [SDL_GetStringProperty](SDL_GetStringProperty)

----
[CategoryAPI](CategoryAPI)

