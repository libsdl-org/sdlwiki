# SDL_GetAudioStreamInputChannelMap

Get the current input channel map of an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int * SDL_GetAudioStreamInputChannelMap(SDL_AudioStream *stream, int *count);
```

## Function Parameters

|                                      |            |                                                               |
| ------------------------------------ | ---------- | ------------------------------------------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the [SDL_AudioStream](SDL_AudioStream) to query.              |
| int *                                | **count**  | On output, set to number of channels in the map. Can be NULL. |

## Return Value

(int *) Returns an array of the current channel mapping, with as many
elements as the current output spec's channels, or NULL if default. This
should be freed with [SDL_free](SDL_free)() when it is no longer needed.

## Remarks

Channel maps are optional; most things do not need them, instead passing
data in the [order that SDL expects](CategoryAudio#channel-layouts).

Audio streams default to no remapping applied. This is represented by
returning NULL, and does not signify an error.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetAudioStreamInputChannelMap](SDL_SetAudioStreamInputChannelMap)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

