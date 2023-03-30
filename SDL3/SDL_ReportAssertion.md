###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReportAssertion

Never call this directly.

## Syntax

```c
SDL_AssertState SDL_ReportAssertion(SDL_AssertData *data,
                                    const char *func,
                                    const char *file, int line)
#ifdef __clang__
#if __has_feature(attribute_analyzer_noreturn)
   __attribute__((analyzer_noreturn))
#endif
#endif
;
/* Previous 'analyzer_noreturn' attribute tells Clang's static analysis that we're a custom assert function,
   and that the analyzer should assume the condition was always true past this
   SDL_assert test. */


/* Define the trigger breakpoint call used in asserts */
#ifndef SDL_AssertBreakpoint
#if defined(ANDROID) && defined(assert)
/* Define this as empty in case assert() is defined as SDL_assert */
#define SDL_AssertBreakpoint() 
#else
#define SDL_AssertBreakpoint() SDL_TriggerBreakpoint()
#endif
#endif /* !SDL_AssertBreakpoint */

/* the do {} while(0) avoids dangling else problems:
    if (x) SDL_assert(y); else blah();

```

## Function Parameters

|              |                       |
| ------------ | --------------------- |
| **data**     | assert data structure |
| **func**     | function name         |
| **file**     | file name             |
| **line**     | line number           |

## Return Value

Returns assert state

## Remarks

Use the [SDL_assert](SDL_assert)* macros.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

