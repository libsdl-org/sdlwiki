###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetPostMix

Set a function that is called after all mixing is performed.

## Syntax

```c
void Mix_SetPostMix(void (SDLCALL *mix_func)(void *udata, Uint8 *stream, int len), void *arg);

```

## Function Parameters

|                  |                                                            |
| ---------------- | ---------------------------------------------------------- |
| **mix_func**     | the callback function to become the new post-mix callback. |
| **arg**          | a pointer that is passed, untouched, to the callback.      |

## Remarks

This can be used to provide real-time visual display of the audio stream or
add a custom mixer filter for the stream data.

The callback will fire every time SDL_mixer is ready to supply more data to
the audio device, after it has finished all its mixing work. This runs
inside an SDL audio callback, so it's important that the callback return
quickly, or there could be problems in the audio playback.

The data provided to the callback is in the format that the audio device
was opened in, and it represents the exact waveform SDL_mixer has mixed
from all playing chunks and music for playback. You are allowed to modify
the data, but it cannot be resized (so you can't add a reverb effect that
goes past the end of the buffer without saving some state between runs to
add it into the next callback, or resample the buffer to a smaller size to
speed it up, etc).

The `arg` pointer supplied here is passed to the callback as-is, for
whatever the callback might want to do with it (keep track of some ongoing
state, settings, etc).

Passing a NULL callback disables the post-mix callback until such a time as
a new one callback is set.

There is only one callback available. If you need to mix multiple inputs,
be prepared to handle them from a single function.

## Version

This function is available since SDL_mixer 3.0.0.

## Related Functions

* [Mix_HookMusic](Mix_HookMusic.md)

----
[CategoryAPI](CategoryAPI.md)
