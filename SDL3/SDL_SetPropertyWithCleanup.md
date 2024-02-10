###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetPropertyWithCleanup

Set a property on a set of properties with a cleanup function that is called when the property is deleted 

## Syntax

```c
int SDL_SetPropertyWithCleanup(SDL_PropertiesID props, const char *name, void *value, void (SDLCALL *cleanup)(void *userdata, void *value), void *userdata);

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

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

