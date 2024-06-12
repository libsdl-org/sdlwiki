###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicDecoder

Get a music decoder's name.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
const char * Mix_GetMusicDecoder(int index);
```

## Function Parameters

|     |           |                             |
| --- | --------- | --------------------------- |
| int | **index** | index of the music decoder. |

## Return Value

(const char *) Returns the music decoder's name.

## Remarks

The requested decoder's index must be between zero and
[Mix_GetNumMusicDecoders](Mix_GetNumMusicDecoders)()-1. It's safe to call
this with an invalid index; this function will return NULL in that case.

This list can change between builds AND runs of the program, if external
libraries that add functionality become available. You must successfully
call [Mix_OpenAudio](Mix_OpenAudio)() before calling this function, as
decoders are activated at device open time.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [Mix_GetNumMusicDecoders](Mix_GetNumMusicDecoders)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

