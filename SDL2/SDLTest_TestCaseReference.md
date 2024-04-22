###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDLTest_TestCaseReference

Holds information about a single test case.

## Header File

Defined in [SDL_test_harness.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_test_harness.h)

## Syntax

```c
typedef struct SDLTest_TestCaseReference {
    /* !< Func2Stress */
    SDLTest_TestCaseFp testCase;
    /* !< Short name (or function name) "Func2Stress" */
    const char *name;
    /* !< Long name or full description "This test pushes func2() to the limit." */
    const char *description;
    /* !< Set to TEST_ENABLED or TEST_DISABLED (test won't be run) */
    int enabled;
} SDLTest_TestCaseReference;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

