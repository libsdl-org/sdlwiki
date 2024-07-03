###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AudioStream

The opaque handle that represents an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
typedef struct SDL_AudioStream SDL_AudioStream;
```

## Remarks

[SDL_AudioStream](SDL_AudioStream) is an audio conversion interface.

- It can handle resampling data in chunks without generating artifacts,
  when it doesn't have the complete buffer available.
- It can handle incoming data in any variable size.
- It can handle input/output format changes on the fly.
- It can remap audio channels between inputs and outputs.
- You push data as you have it, and pull it when you need it
- It can also function as a basic audio data queue even if you just have
  sound that needs to pass from one place to another.
- You can hook callbacks up to them when more data is added or requested,
  to manage data on-the-fly.

Audio streams are the core of the SDL3 audio interface. You create one or
more of them, bind them to an opened audio device, and feed data to them
(or for recording, consume data from them).

## Version

This struct is available since SDL 3.0.0.

## See Also

- [SDL_CreateAudioStream](SDL_CreateAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAudio](CategoryAudio)

