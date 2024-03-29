###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_toupper

Convert low-ASCII English letters to uppercase.

## Syntax

```c
int SDL_toupper(int x);

```

## Function Parameters

|           |                           |
| --------- | ------------------------- |
| **x**     | character value to check. |

## Return Value

Returns Capitalized version of x, or x if no conversion available.

## Remarks

**WARNING**: Regardless of system locale, this will only convert ASCII
values 'a' through 'z' to uppercase.

This function returns the uppercase equivalent of `x`. If a character
cannot be converted, or is already uppercase, this function returns `x`.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

