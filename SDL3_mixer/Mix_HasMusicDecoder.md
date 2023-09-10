###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_HasMusicDecoder

Check if a music decoder is available by name.

## Syntax

```c
SDL_bool Mix_HasMusicDecoder(const char *name);

```

## Function Parameters

|              |                            |
| ------------ | -------------------------- |
| **name**     | the decoder name to query. |

## Return Value

Returns SDL_TRUE if a decoder by that name is available, SDL_FALSE
otherwise.

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

This function is available since SDL_mixer 3.0.0

## Related Functions

* [Mix_GetNumMusicDecoders](Mix_GetNumMusicDecoders)
* [Mix_GetMusicDecoder](Mix_GetMusicDecoder)

----
[CategoryAPI](CategoryAPI)

