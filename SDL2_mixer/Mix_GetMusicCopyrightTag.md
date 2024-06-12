###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicCopyrightTag

Get the copyright text for a music object.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
const char* Mix_GetMusicCopyrightTag(const Mix_Music *music);
```

## Function Parameters

|                                |           |                                                                     |
| ------------------------------ | --------- | ------------------------------------------------------------------- |
| const [Mix_Music](Mix_Music) * | **music** | the music object to query, or NULL for the currently-playing music. |

## Return Value

(const char *) Returns the music's copyright text if available, or "".

## Remarks

This returns format-specific metadata. Not all file formats supply this!

If `music` is NULL, this will query the currently-playing music.

This function never returns NULL! If no data is available, it will return
an empty string ("").

## Version

This function is available since SDL_mixer 2.6.0.

## See Also

- [Mix_GetMusicTitleTag](Mix_GetMusicTitleTag)
- [Mix_GetMusicArtistTag](Mix_GetMusicArtistTag)
- [Mix_GetMusicAlbumTag](Mix_GetMusicAlbumTag)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

