###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AssertData

Information about an assertion failure.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
typedef struct SDL_AssertData
{
    SDL_bool always_ignore;  /**< SDL_TRUE if app should always continue when assertion is triggered. */
    unsigned int trigger_count; /**< Number of times this assertion has been triggered. */
    const char *condition;  /**< A string of this assert's test code. */
    const char *filename;  /**< The source file where this assert lives. */
    int linenum;  /**< The line in `filename` where this assert lives. */
    const char *function;  /**< The name of the function where this assert lives. */
    const struct SDL_AssertData *next;  /**< next item in the linked list. */
} SDL_AssertData;
```

## Remarks

This structure is filled in with information about a triggered assertion,
used by the assertion handler, then added to the assertion report. This is
returned as a linked list from
[SDL_GetAssertionReport](SDL_GetAssertionReport)().

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

