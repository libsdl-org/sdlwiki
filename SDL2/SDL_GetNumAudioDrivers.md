###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetNumAudioDrivers

Use this function to get the number of built-in audio drivers.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
int SDL_GetNumAudioDrivers(void);

```

## Return Value

Returns the number of built-in audio drivers.

## Remarks

This function returns a hardcoded number. This never returns a negative
value; if there are no drivers compiled into this build of SDL, this
function returns zero. The presence of a driver in this list does not mean
it will function, it just means SDL is capable of interacting with that
interface. For example, a build of SDL might have esound support, but if
there's no esound server available, SDL's esound driver would fail if used.

By default, SDL tries all drivers, in its preferred order, until one is
found to be usable.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_GetAudioDriver](SDL_GetAudioDriver)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

