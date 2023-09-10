###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicTitleTag

Get the title for a music object.

## Syntax

```c
const char* Mix_GetMusicTitleTag(const Mix_Music *music);

```

## Function Parameters

|               |                                                                     |
| ------------- | ------------------------------------------------------------------- |
| **music**     | the music object to query, or NULL for the currently-playing music. |

## Return Value

Returns the music's title if available, or "".

## Remarks

This returns format-specific metadata. Not all file formats supply this!

If `music` is NULL, this will query the currently-playing music.

Unlike this function, [Mix_GetMusicTitle](Mix_GetMusicTitle)() produce a
string with the music's filename if a title isn't available, which might be
preferable for some applications.

This function never returns NULL! If no data is available, it will return
an empty string ("").

## Version

This function is available since SDL_mixer 3.0.0.

## Related Functions

* [Mix_GetMusicTitle](Mix_GetMusicTitle)
* [Mix_GetMusicArtistTag](Mix_GetMusicArtistTag)
* [Mix_GetMusicAlbumTag](Mix_GetMusicAlbumTag)
* [Mix_GetMusicCopyrightTag](Mix_GetMusicCopyrightTag)

----
[CategoryAPI](CategoryAPI)

