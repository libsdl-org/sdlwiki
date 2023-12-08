###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicAlbumTag

Get the album name for a music object.

## Syntax

```c
const char* Mix_GetMusicAlbumTag(const Mix_Music *music);

```

## Function Parameters

|               |                                                                     |
| ------------- | ------------------------------------------------------------------- |
| **music**     | the music object to query, or NULL for the currently-playing music. |

## Return Value

Returns the music's album name if available, or "".

## Remarks

This returns format-specific metadata. Not all file formats supply this!

If `music` is NULL, this will query the currently-playing music.

This function never returns NULL! If no data is available, it will return
an empty string ("").

## Version

This function is available since SDL_mixer 2.6.0.

## Related Functions

* [Mix_GetMusicTitleTag](Mix_GetMusicTitleTag.md)
* [Mix_GetMusicArtistTag](Mix_GetMusicArtistTag.md)
* [Mix_GetMusicCopyrightTag](Mix_GetMusicCopyrightTag.md)

----
[CategoryAPI](CategoryAPI.md)
