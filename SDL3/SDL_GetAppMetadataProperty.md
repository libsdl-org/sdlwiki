###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAppMetadataProperty

Get metadata about your app.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
const char * SDL_GetAppMetadataProperty(const char *name);
```

## Function Parameters

|              |          |                                           |
| ------------ | -------- | ----------------------------------------- |
| const char * | **name** | the name of the metadata property to get. |

## Return Value

(const char *) Returns the current value of the metadata property, or the
default if it is not set, NULL for properties with no default.

## Remarks

This returns metadata previously set using
[SDL_SetAppMetadata](SDL_SetAppMetadata)() or
[SDL_SetAppMetadataProperty](SDL_SetAppMetadataProperty)(). See
[SDL_SetAppMetadataProperty](SDL_SetAppMetadataProperty)() for the list of
available properties and their meanings.

## Thread Safety

It is safe to call this function from any thread, although the string
returned is not protected and could potentially be freed if you call
[SDL_SetAppMetadataProperty](SDL_SetAppMetadataProperty)() to set that
property from another thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetAppMetadata](SDL_SetAppMetadata)
- [SDL_SetAppMetadataProperty](SDL_SetAppMetadataProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)

