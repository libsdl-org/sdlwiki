###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_ModMusicJumpToOrder

Jump to a given order in mod music.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
int Mix_ModMusicJumpToOrder(int order);
```

## Function Parameters

|     |           |        |
| --- | --------- | ------ |
| int | **order** | order. |

## Return Value

(int) Returns 0 if successful, or -1 if failed or isn't implemented.

## Remarks

This only applies to MOD music formats.

## Version

This function is available since SDL_mixer 2.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

