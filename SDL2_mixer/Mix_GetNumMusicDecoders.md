###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetNumMusicDecoders

Get a list of music decoders that this build of SDL_mixer provides.

## Syntax

```c
int Mix_GetNumMusicDecoders(void);

```

## Return Value

Returns number of music decoders available.

## Remarks

This list can change between builds AND runs of the program, if external
libraries that add functionality become available. You must successfully
call [Mix_OpenAudio](Mix_OpenAudio.md)() or
[Mix_OpenAudioDevice](Mix_OpenAudioDevice.md)() before calling this function,
as decoders are activated at device open time.

Appearing in this list doesn't promise your specific audio file will
decode...but it's handy to know if you have, say, a functioning Ogg Vorbis
install.

These return values are static, read-only data; do not modify or free it.
The pointers remain valid until you call
[Mix_CloseAudio](Mix_CloseAudio.md)().

## Version

This function is available since SDL_mixer 2.0.0.

## Related Functions

* [Mix_GetMusicDecoder](Mix_GetMusicDecoder.md)
* [Mix_HasMusicDecoder](Mix_HasMusicDecoder.md)

----
[CategoryAPI](CategoryAPI.md)
