###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AddHintCallback

Add a function to watch a particular hint.

## Syntax

```c
void SDL_AddHintCallback(const char *name,
                         SDL_HintCallback callback,
                         void *userdata);

```

## Function Parameters

|                  |                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| **name**         | the hint to watch                                                                                |
| **callback**     | An [SDL_HintCallback](SDL_HintCallback.md) function that will be called when the hint value changes |
| **userdata**     | a pointer to pass to the callback function                                                       |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_DelHintCallback](SDL_DelHintCallback.md)


## Example

```c
// Callback function that prints message if new value of hint is 1

void callback(void* f_name, const char* name, const char* oldValue, const char* newValue) {
  if (newValue == (const char*)"1") {
    printf("Hi %s\n", static_cast<char*>(f_name));
  }
}

...

SDL_SetHint(SDL_HINT_XINPUT_ENABLED, "0");

...

SDL_Init(SDL_INIT_EVERYTHING);

...

while(SDL_PollEvent(&event) != 0)
{
   // You can change hint here
}

...

SDL_AddHintCallback(SDL_HINT_XINPUT_ENABLED, callback, const_cast<char*>("SDL"));
```

----
[CategoryAPI](CategoryAPI.md), [CategoryHints](CategoryHints.md)
