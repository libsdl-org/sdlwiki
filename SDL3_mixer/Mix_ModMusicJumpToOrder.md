###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_ModMusicJumpToOrder

Jump to a given order in mod music.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool Mix_ModMusicJumpToOrder(int order);
```

## Function Parameters

|     |           |        |
| --- | --------- | ------ |
| int | **order** | order. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This only applies to MOD music formats.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

