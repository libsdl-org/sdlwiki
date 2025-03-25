# SDL_ProgressState

Window progress state

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef enum SDL_ProgressState
{
    SDL_PROGRESS_STATE_INVALID = -1,    /**< An invalid progress state indicating an error; check SDL_GetError() */
    SDL_PROGRESS_STATE_NONE,            /**< No progress bar is shown */
    SDL_PROGRESS_STATE_INDETERMINATE,   /**< The progress bar is shown in a indeterminate state */
    SDL_PROGRESS_STATE_NORMAL,          /**< The progress bar is shown in a normal state */
    SDL_PROGRESS_STATE_PAUSED,          /**< The progress bar is shown in a paused state */
    SDL_PROGRESS_STATE_ERROR            /**< The progress bar is shown in a state indicating the application had an error */
} SDL_ProgressState;
```

## Version

This enum is available since SDL 3.2.8.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryVideo](CategoryVideo)

