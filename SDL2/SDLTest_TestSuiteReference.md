###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDLTest_TestSuiteReference

Holds information about a test suite (multiple test cases).

## Header File

Defined in [SDL_test_harness.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_test_harness.h)

## Syntax

```c
typedef struct SDLTest_TestSuiteReference {
    /* !< "PlatformSuite" */
    const char *name;
    /* !< The function that is run before each test. NULL skips. */
    SDLTest_TestCaseSetUpFp testSetUp;
    /* !< The test cases that are run as part of the suite. Last item should be NULL. */
    const SDLTest_TestCaseReference **testCases;
    /* !< The function that is run after each test. NULL skips. */
    SDLTest_TestCaseTearDownFp testTearDown;
} SDLTest_TestSuiteReference;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

