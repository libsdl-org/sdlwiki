###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetNumChunkDecoders

Get a list of chunk decoders that this build of SDL_mixer provides.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int Mix_GetNumChunkDecoders(void);
```

## Return Value

(int) Returns number of chunk decoders available.

## Remarks

This list can change between builds AND runs of the program, if external
libraries that add functionality become available. You must successfully
call [Mix_OpenAudio](Mix_OpenAudio)() before calling this function, as
decoders are activated at device open time.

Appearing in this list doesn't promise your specific audio file will
decode...but it's handy to know if you have, say, a functioning Ogg Vorbis
install.

These return values are static, read-only data; do not modify or free it.
The pointers remain valid until you call
[Mix_CloseAudio](Mix_CloseAudio)().

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [Mix_GetChunkDecoder](Mix_GetChunkDecoder)
- [Mix_HasChunkDecoder](Mix_HasChunkDecoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

