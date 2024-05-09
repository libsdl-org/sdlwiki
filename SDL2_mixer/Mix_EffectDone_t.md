###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_EffectDone_t

This is a callback that signifies that a channel has finished all its loops and has completed playback.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
typedef void (SDLCALL *Mix_EffectDone_t)(int chan, void *udata);
```

## Remarks

This gets called if the buffer plays out normally, or if you call
[Mix_HaltChannel](Mix_HaltChannel)(), implicitly stop a channel via
[Mix_AllocateChannels](Mix_AllocateChannels)(), or unregister a callback
while it's still playing.

DO NOT EVER call SDL_LockAudio() from your callback function!

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

