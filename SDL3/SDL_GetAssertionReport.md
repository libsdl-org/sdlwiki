###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAssertionReport

Get a list of all assertion failures.

## Header File

Defined in [SDL_assert.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
const SDL_AssertData * SDL_GetAssertionReport(void);

```

## Return Value

Returns a list of all failed assertions or NULL if the list is empty. This
memory should not be modified or freed by the application.

## Remarks

This function gets all assertions triggered since the last call to
[SDL_ResetAssertionReport](SDL_ResetAssertionReport)(), or the start of the
program.

The proper way to examine this data looks something like this:

```c
const SDL_AssertData *item = SDL_GetAssertionReport();
while (item) {
   printf("'%s', %s (%s:%d), triggered %u times, always ignore: %s.\\n",
          item->condition, item->function, item->filename,
          item->linenum, item->trigger_count,
          item->always_ignore ? "yes" : "no");
   item = item->next;
}
```

## Version

This function is available since SDL 3.0.0.

## Code Examples

The proper way to examine this data looks something like this:
```c++
const SDL_AssertData *item = SDL_GetAssertionReport();
while (item) {
     printf("'%s', %s (%s:%d), triggered %u times, always ignore: %s.\n",
          item->condition, item->function, item->filename,
          item->linenum, item->trigger_count,
          item->always_ignore ? "yes" : "no");
     item = item->next;
}
```

## See Also

* [SDL_ResetAssertionReport](SDL_ResetAssertionReport)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAssertions](CategoryAssertions)


