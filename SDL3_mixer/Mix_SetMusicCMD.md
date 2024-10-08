###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetMusicCMD

Run an external command as the music stream.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool Mix_SetMusicCMD(const char *command);
```

## Function Parameters

|              |             |          |
| ------------ | ----------- | -------- |
| const char * | **command** | command. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This halts any currently-playing music, and next time the music stream is
played, SDL_mixer will spawn a process using the command line specified in
`command`. This command is not subject to shell expansion, and beyond some
basic splitting up of arguments, is passed to execvp() on most platforms,
not system().

The command is responsible for generating sound; it is NOT mixed by
SDL_mixer! SDL_mixer will kill the child process if asked to halt the
music, but otherwise does not have any control over what the process does.

You are strongly encouraged not to use this function without an extremely
good reason.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

