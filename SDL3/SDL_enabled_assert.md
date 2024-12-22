###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_enabled_assert

The macro used when an assertion is enabled.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
#define SDL_enabled_assert(condition) \
    do { \
        while ( !(condition) ) { \
            static struct SDL_AssertData sdl_assert_data = { 0, 0, #condition, 0, 0, 0, 0 }; \
            const SDL_AssertState sdl_assert_state = SDL_ReportAssertion(&sdl_assert_data, SDL_FUNCTION, SDL_FILE, SDL_LINE); \
            if (sdl_assert_state == SDL_ASSERTION_RETRY) { \
                continue; /* go again. */ \
            } else if (sdl_assert_state == SDL_ASSERTION_BREAK) { \
                SDL_AssertBreakpoint(); \
            } \
            break; /* not retrying. */ \
        } \
    } while (SDL_NULL_WHILE_LOOP_CONDITION)
```

## Macro Parameters

|               |                          |
| ------------- | ------------------------ |
| **condition** | the condition to assert. |

## Remarks

This isn't for direct use by apps, but this is the code that is inserted
when an [SDL_assert](SDL_assert) is enabled.

The `do {} while(0)` avoids dangling else problems:

```c
if (x) SDL_assert(y); else blah();
```

... without the do/while, the "else" could attach to this macro's "if". We
try to handle just the minimum we need here in a macro...the loop, the
static vars, and break points. The heavy lifting is handled in
[SDL_ReportAssertion](SDL_ReportAssertion)().

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAssert](CategoryAssert)

