###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_HookMusic

Add your own music player or additional mixer function.

## Syntax

```c
void Mix_HookMusic(void (SDLCALL *mix_func)(void *udata, Uint8 *stream, int len), void *arg);

```

## Function Parameters

|                  |                                                            |
| ---------------- | ---------------------------------------------------------- |
| **mix_func**     | the callback function to become the new post-mix callback. |
| **arg**          | a pointer that is passed, untouched, to the callback.      |

## Remarks

This works something like [Mix_SetPostMix](Mix_SetPostMix)(), but it has
some crucial differences. Note that an app can use this _and_
[Mix_SetPostMix](Mix_SetPostMix)() at the same time. This allows an app to
replace the built-in music playback, either with it's own music decoder or
with some sort of procedurally-generated audio output.

The supplied callback will fire every time SDL_mixer is preparing to supply
more data to the audio device. This runs inside an SDL audio callback, so
it's important that the callback return quickly, or there could be problems
in the audio playback.

Running this callback is the first thing SDL_mixer will do when starting to
mix more audio. The buffer will contain silence upon entry, so the callback
does not need to mix into existing data or initialize the buffer.

Note that while a callback is set through this function, SDL_mixer will not
mix any playing music; this callback is used instead. To disable this
callback (and thus reenable built-in music playback) call this function
with a NULL callback.

The data written to by the callback is in the format that the audio device
was opened in, and upon return from the callback, SDL_mixer will mix any
playing chunks (but not music!) into the buffer. The callback cannot resize
the buffer (so you must be prepared to provide exactly the amount of data
demanded or leave it as silence).

The `arg` pointer supplied here is passed to the callback as-is, for
whatever the callback might want to do with it (keep track of some ongoing
state, settings, etc).

As there is only one music "channel" mixed, there is only one callback
available. If you need to mix multiple inputs, be prepared to handle them
from a single function.

## Version

This function is available since SDL_mixer 3.0.0.

## Related Functions

* [Mix_SetPostMix](Mix_SetPostMix)

----
[CategoryAPI](CategoryAPI)

