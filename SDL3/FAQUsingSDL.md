# FAQ: Using SDL3

# What environment variables are used by SDL?

A complete list is available on the [EnvironmentVariables](EnvironmentVariables) page.

You can also browse [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h).
These can be set programmatically with SDL_SetHint, or specified as environment
variables by the end-user.

# Why does SDL disable my screensaver by default?

Many applications using SDL are games or screensavers or media players where
the user is either watching something for an extended period of time or using
joystick input which generally does not prevent the screensaver from kicking
on.

You can disable this behavior by setting the environment variable:
`SDL_VIDEO_ALLOW_SCREENSAVER=1`

This can be set globally for the user or on a per-application basis in code.

Programmatically, the function [SDL_EnableScreenSaver](SDL_EnableScreenSaver)
can be used; this might make sense for some programs to universally enable
the screensaver, or toggle it to disabled only during media playback, etc.

