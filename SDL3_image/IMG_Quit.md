###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_Quit

Deinitialize SDL_image.

## Header File

Defined in SDL_image.h

## Syntax

```c
void IMG_Quit(void);

```

## Remarks

This should be the last function you call in SDL_image, after freeing all
other resources. This will unload any shared libraries it is using for
various codecs.

After this call, a call to [IMG_Init](IMG_Init)(0) will return 0 (no codecs
loaded).

You can safely call [IMG_Init](IMG_Init)() to reload various codec support
after this call.

Unlike other SDL satellite libraries, calls to [IMG_Init](IMG_Init) do not
stack; a single call to [IMG_Quit](IMG_Quit)() will deinitialize everything
and does not have to be paired with a matching [IMG_Init](IMG_Init) call.
For that reason, it's considered best practices to have a single
[IMG_Init](IMG_Init) and [IMG_Quit](IMG_Quit) call in your program. While
this isn't required, be aware of the risks of deviating from that behavior.

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_Init](IMG_Init)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

