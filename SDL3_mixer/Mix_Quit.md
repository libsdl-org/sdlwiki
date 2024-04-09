###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_Quit

Deinitialize SDL_mixer.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
void Mix_Quit(void);

```

## Remarks

This should be the last function you call in SDL_mixer, after freeing all
other resources and closing all audio devices. This will unload any shared
libraries it is using for various codecs.

After this call, a call to [Mix_Init](Mix_Init)(0) will return 0 (no codecs
loaded).

You can safely call [Mix_Init](Mix_Init)() to reload various codec support
after this call.

Unlike other SDL satellite libraries, calls to [Mix_Init](Mix_Init) do not
stack; a single call to [Mix_Quit](Mix_Quit)() will deinitialize everything
and does not have to be paired with a matching [Mix_Init](Mix_Init) call.
For that reason, it's considered best practices to have a single
[Mix_Init](Mix_Init) and [Mix_Quit](Mix_Quit) call in your program. While
this isn't required, be aware of the risks of deviating from that behavior.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

* [Mix_Init](Mix_Init)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

