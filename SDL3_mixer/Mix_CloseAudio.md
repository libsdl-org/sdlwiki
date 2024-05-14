###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_CloseAudio

Close the mixer, halting all playing audio.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
void Mix_CloseAudio(void);

```

## Remarks

Any halted channels will have any currently-registered effects
deregistered, and will call any callback specified by
[Mix_ChannelFinished](Mix_ChannelFinished)() before this function returns.

Any halted music will call any callback specified by
[Mix_HookMusicFinished](Mix_HookMusicFinished)() before this function
returns.

Do not start any new audio playing during callbacks in this function.

This will close the audio device. Attempting to play new audio after this
function returns will fail, until another successful call to
[Mix_OpenAudio](Mix_OpenAudio)().

Note that (unlike [Mix_OpenAudio](Mix_OpenAudio) optionally calling
SDL_Init(SDL_INIT_AUDIO) on the app's behalf), this will _not_ deinitialize
the SDL audio subsystem in any case. At some point after calling this
function and [Mix_Quit](Mix_Quit)(), some part of the application should be
responsible for calling SDL_Quit() to deinitialize all of SDL, including
its audio subsystem.

This function should be the last thing you call in SDL_mixer before
[Mix_Quit](Mix_Quit)(). However, the following notes apply if you don't
follow this advice:

Note that this will not free any loaded chunks or music; you should dispose
of those resources separately. It is probably poor form to dispose of them
_after_ this function, but it is safe to call
[Mix_FreeChunk](Mix_FreeChunk)() and [Mix_FreeMusic](Mix_FreeMusic)() after
closing the device.

Note that any chunks or music you don't free may or may not work if you
call [Mix_OpenAudio](Mix_OpenAudio) again, as the audio device may be in a
new format and the existing chunks will not be converted to match.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [Mix_Quit](Mix_Quit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

