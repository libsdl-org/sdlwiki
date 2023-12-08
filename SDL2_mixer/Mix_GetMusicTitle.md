###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicTitle

Get the title for a music object, or its filename.

## Syntax

```c
const char* Mix_GetMusicTitle(const Mix_Music *music);

```

## Function Parameters

|               |                                                                     |
| ------------- | ------------------------------------------------------------------- |
| **music**     | the music object to query, or NULL for the currently-playing music. |

## Return Value

Returns the music's title if available, or the filename if not, or "".

## Remarks

This returns format-specific metadata. Not all file formats supply this!

If `music` is NULL, this will query the currently-playing music.

If music's title tag is missing or empty, the filename will be returned. If
you'd rather have the actual metadata or nothing, use
[Mix_GetMusicTitleTag](Mix_GetMusicTitleTag.md)() instead.

Please note that if the music was loaded from an SDL_RWops instead of a
filename, the filename returned will be an empty string ("").

This function never returns NULL! If no data is available, it will return
an empty string ("").

## Version

This function is available since SDL_mixer 2.6.0.

## Related Functions

* [Mix_GetMusicTitleTag](Mix_GetMusicTitleTag.md)
* [Mix_GetMusicArtistTag](Mix_GetMusicArtistTag.md)
* [Mix_GetMusicAlbumTag](Mix_GetMusicAlbumTag.md)
* [Mix_GetMusicCopyrightTag](Mix_GetMusicCopyrightTag.md)

----
[CategoryAPI](CategoryAPI.md)
