###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetNumChunkDecoders

Get a list of chunk decoders that this build of SDL_mixer provides.

## Syntax

```c
int Mix_GetNumChunkDecoders(void);

```

## Return Value

Returns number of chunk decoders available.

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

## Code Examples

```c
int i;
const int total = Mix_GetNumChunkDecoders();
for (i = 0; i < total; i++) {
    printf("Supported chunk decoder: [%s]\n", Mix_GetChunkDecoder(i));
}
```

## Related Functions

* [Mix_GetChunkDecoder](Mix_GetChunkDecoder.md)
* [Mix_HasChunkDecoder](Mix_HasChunkDecoder.md)

----
[CategoryAPI](CategoryAPI.md)
