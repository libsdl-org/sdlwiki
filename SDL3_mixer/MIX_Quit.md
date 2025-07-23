###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_Quit

Deinitialize the SDL_mixer library.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void MIX_Quit(void);
```

## Remarks

This must be called when done with the library, probably at the end of your
program.

It is safe to call this multiple times; the library will only deinitialize
once, when this function is called the same number of times as
[MIX_Init](MIX_Init) was successfully called.

Once you have successfully deinitialized the library, it is safe to call
[MIX_Init](MIX_Init) to reinitialize it for further use.

On successful deinitialization, SDL_mixer will destroy almost all created
objects, including objects of type:

- [MIX_Mixer](MIX_Mixer)
- [MIX_Track](MIX_Track)
- [MIX_Audio](MIX_Audio)
- [MIX_Group](MIX_Group)
- [MIX_AudioDecoder](MIX_AudioDecoder)

...which is to say: it's possible a single call to this function will clean
up anything it allocated, stop all audio output, close audio devices, etc.
Don't attempt to destroy objects after this call. The app is still
encouraged to manage their resources carefully and clean up first, treating
this function as a safety net against memory leaks.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_Init](MIX_Init)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

