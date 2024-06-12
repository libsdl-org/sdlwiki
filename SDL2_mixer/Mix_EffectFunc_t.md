###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_EffectFunc_t

This is the format of a special effect callback:

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
typedef void (SDLCALL *Mix_EffectFunc_t)(int chan, void *stream, int len, void *udata);
```

## Remarks

myeffect(int chan, void *stream, int len, void *udata);

(chan) is the channel number that your effect is affecting. (stream) is the
buffer of data to work upon. (len) is the size of (stream), and (udata) is
a user-defined bit of data, which you pass as the last arg of
[Mix_RegisterEffect](Mix_RegisterEffect)(), and is passed back unmolested
to your callback. Your effect changes the contents of (stream) based on
whatever parameters are significant, or just leaves it be, if you prefer.
You can do whatever you like to the buffer, though, and it will continue in
its changed state down the mixing pipeline, through any other effect
functions, then finally to be mixed with the rest of the channels and music
for the final output stream.

DO NOT EVER call SDL_LockAudio() from your callback function!

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

