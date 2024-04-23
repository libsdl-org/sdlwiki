###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_GAMECONTROLLER_USE_BUTTON_LABELS

If set, game controller face buttons report their values according to their labels instead of their positional layout.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GAMECONTROLLER_USE_BUTTON_LABELS "SDL_GAMECONTROLLER_USE_BUTTON_LABELS"
```

## Remarks

For example, on Nintendo Switch controllers, normally you'd get:

```
     (Y)
 (X)     (B)
     (A)
```

but if this hint is set, you'll get:

```
     (X)
 (Y)     (A)
     (B)
```

The variable can be set to the following values:

- "0": Report the face buttons by position, as though they were on an Xbox
  controller.
- "1": Report the face buttons by label instead of position

The default value is "1". This hint may be set at any time.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

