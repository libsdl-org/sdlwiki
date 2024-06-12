###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_HasMusicDecoder

Check if a music decoder is available by name.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
SDL_bool Mix_HasMusicDecoder(const char *name);
```

## Function Parameters

|              |          |                            |
| ------------ | -------- | -------------------------- |
| const char * | **name** | the decoder name to query. |

## Return Value

(SDL_bool) Returns SDL_TRUE if a decoder by that name is available,
SDL_FALSE otherwise.

## Remarks

This result can change between builds AND runs of the program, if external
libraries that add functionality become available. You must successfully
call [Mix_OpenAudio](Mix_OpenAudio)() or
[Mix_OpenAudioDevice](Mix_OpenAudioDevice)() before calling this function,
as decoders are activated at device open time.

Decoder names are arbitrary but also obvious, so you have to know what
you're looking for ahead of time, but usually it's the file extension in
capital letters (some example names are "MOD", "MP3", "FLAC").

## Version

This function is available since SDL_mixer 2.6.0

## See Also

- [Mix_GetNumMusicDecoders](Mix_GetNumMusicDecoders)
- [Mix_GetMusicDecoder](Mix_GetMusicDecoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

