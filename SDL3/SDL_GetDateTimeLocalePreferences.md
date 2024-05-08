###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDateTimeLocalePreferences

Gets the current preferred date and time format for the system locale.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
int SDL_GetDateTimeLocalePreferences(SDL_DateFormat *dateFormat, SDL_TimeFormat *timeFormat);

```

## Function Parameters

|                    |                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------- |
| **dateFormat**     | a pointer to the [SDL_DateFormat](SDL_DateFormat) to hold the returned date format, may be NULL |
| **timeFormat**     | a pointer to the [SDL_TimeFormat](SDL_TimeFormat) to hold the returned time format, may be NULL |

## Remarks

This might be a "slow" call that has to query the operating system. It's
best to ask for this once and save the results. However, the preferred
formats can change, usually because the user has changed a system
preference outside of your program.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

