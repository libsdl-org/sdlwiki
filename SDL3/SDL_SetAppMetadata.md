###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetAppMetadata

Specify basic metadata about your app.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
bool SDL_SetAppMetadata(const char *appname, const char *appversion, const char *appidentifier);
```

## Function Parameters

|              |                   |                                                                                            |
| ------------ | ----------------- | ------------------------------------------------------------------------------------------ |
| const char * | **appname**       | The name of the application ("My Game 2: Bad Guy's Revenge!").                             |
| const char * | **appversion**    | The version of the application ("1.0.0beta5" or a git hash, or whatever makes sense).      |
| const char * | **appidentifier** | A unique string in reverse-domain format that identifies this app ("com.example.mygame2"). |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can optionally provide metadata about your app to SDL. This is not
required, but strongly encouraged.

There are several locations where SDL can make use of metadata (an "About"
box in the macOS menu bar, the name of the app can be shown on some audio
mixers, etc). Any piece of metadata can be left as NULL, if a specific
detail doesn't make sense for the app.

This function should be called as early as possible, before
[SDL_Init](SDL_Init). Multiple calls to this function are allowed, but
various state might not change once it has been set up with a previous call
to this function.

Passing a NULL removes any previous metadata.

This is a simplified interface for the most important information. You can
supply significantly more detailed metadata with
[SDL_SetAppMetadataProperty](SDL_SetAppMetadataProperty)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetAppMetadataProperty](SDL_SetAppMetadataProperty)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)

