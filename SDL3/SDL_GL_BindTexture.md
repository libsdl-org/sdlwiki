###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GL_BindTexture

Bind an OpenGL/ES/ES2 texture to the current context.

## Syntax

```c
int SDL_GL_BindTexture(SDL_Texture *texture, float *texw, float *texh);

```

## Function Parameters

|                 |                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| **texture**     | the texture to bind to the current OpenGL/ES/ES2 context                                                     |
| **texw**        | a pointer to a float value which will be filled with the texture width or NULL if you don't need that value  |
| **texh**        | a pointer to a float value which will be filled with the texture height or NULL if you don't need that value |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This is for use with OpenGL instructions when rendering OpenGL primitives
directly.

If not NULL, `texw` and `texh` will be filled with the width and height
values suitable for the provided texture. In most cases, both will be 1.0,
however, on systems that support the GL_ARB_texture_rectangle extension,
these values will actually be the pixel width and height used to create the
texture, so this factor needs to be taken into account when providing
texture coordinates to OpenGL.

You need a renderer to create an [SDL_Texture](SDL_Texture.md), therefore you
can only use this function with an implicit OpenGL context from
[SDL_CreateRenderer](SDL_CreateRenderer.md)(), not with your own OpenGL
context. If you need control over your OpenGL context, you need to write
your own texture-loading methods.

Also note that SDL may upload RGB textures as BGR (or vice-versa), and
re-order the color channels in the shaders phase, so the uploaded texture
may have swapped color channels.

## Version

This function is available since SDL 3.0.0.

## Code Examples

The following are three examples extracted from the [Ignifuga Game Engine](http://ignifuga.org) that show how to integrate [libRocket](http://librocket.com) (which uses OpenGL for rendering) with SDL2.

```c++
void RocketSDLRenderInterfaceOpenGL::RenderGeometry(Rocket::Core::Vertex* vertices, int num_vertices, int* indices, int num_indices, const Rocket::Core::TextureHandle texture, const Rocket::Core::Vector2f& translation)
{
    // SDL uses shaders that we need to disable here
    render_data.glUseProgramObjectARB(0);
    render_data.glPushMatrix();
    render_data.glTranslatef(translation.x, translation.y, 0);

    std::vector<Rocket::Core::Vector2f> Positions(num_vertices);
    std::vector<Rocket::Core::Colourb> Colors(num_vertices);
    std::vector<Rocket::Core::Vector2f> TexCoords(num_vertices);
    float texw, texh;

    SDL_Texture* sdl_texture = NULL;
    if(texture) {
        render_data.glEnableClientState(GL_TEXTURE_COORD_ARRAY);
        sdl_texture = (SDL_Texture *) texture;
        SDL_GL_BindTexture(sdl_texture, &texw, &texh);
    }

    for (int  i = 0; i < num_vertices; i++) {
        Positions[i] = vertices[i].position;
        Colors[i] = vertices[i].colour;
        if (sdl_texture) {
            TexCoords[i].x = vertices[i].tex_coord.x * texw;
            TexCoords[i].y = vertices[i].tex_coord.y * texh;
        } else {
            TexCoords[i] = vertices[i].tex_coord;
        }
    }

    render_data.glEnableClientState(GL_VERTEX_ARRAY);
    render_data.glEnableClientState(GL_COLOR_ARRAY);
    render_data.glVertexPointer(2, GL_FLOAT, 0, &Positions[0]);
    render_data.glColorPointer(4, GL_UNSIGNED_BYTE, 0, &Colors[0]);
    render_data.glTexCoordPointer(2, GL_FLOAT, 0, &TexCoords[0]);


    render_data.glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
    render_data.glEnable(GL_BLEND);
    render_data.glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    render_data.glDrawElements(GL_TRIANGLES, num_indices, GL_UNSIGNED_INT, indices);
    render_data.glDisableClientState(GL_VERTEX_ARRAY);
    render_data.glDisableClientState(GL_COLOR_ARRAY);


    if (sdl_texture) {
        SDL_GL_UnbindTexture(sdl_texture);
        render_data.glDisableClientState(GL_TEXTURE_COORD_ARRAY);
    }

    render_data.glColor4f(1.0, 1.0, 1.0, 1.0);
    render_data.glPopMatrix();
}

```

```c++
void RocketSDLRenderInterfaceOpenGLES::RenderGeometry(Rocket::Core::Vertex* vertices, int num_vertices, int* indices, int num_indices, const Rocket::Core::TextureHandle texture, const Rocket::Core::Vector2f& translation)
{
    render_data.glPushMatrix();
    render_data.glTranslatef(translation.x, translation.y, 0);

    std::vector<Rocket::Core::Vector2f> Positions(num_vertices);
    std::vector<Rocket::Core::Colourb> Colors(num_vertices);
    std::vector<Rocket::Core::Vector2f> TexCoords(num_vertices);
    float texw, texh;

    SDL_Texture* sdl_texture = NULL;
    if(texture) {
        render_data.glEnableClientState(GL_TEXTURE_COORD_ARRAY);
        sdl_texture = (SDL_Texture *) texture;
        SDL_GL_BindTexture(sdl_texture, &texw, &texh);
    }

    for (int  i = 0; i < num_vertices; i++) {
        Positions[i] = vertices[i].position;
        Colors[i] = vertices[i].colour;
        if (sdl_texture) {
            TexCoords[i].x = vertices[i].tex_coord.x * texw;
            TexCoords[i].y = vertices[i].tex_coord.y * texh;
        } else {
            TexCoords[i] = vertices[i].tex_coord;
        }
    }

    unsigned short newIndicies[num_indices];
    for (int i = 0; i < num_indices; i++) {
        newIndicies[i] = (unsigned short) indices[i];
    }

    render_data.glEnableClientState(GL_VERTEX_ARRAY);
    render_data.glEnableClientState(GL_COLOR_ARRAY);
    render_data.glVertexPointer(2, GL_FLOAT, 0, &Positions[0]);
    render_data.glColorPointer(4, GL_UNSIGNED_BYTE, 0, &Colors[0]);
    render_data.glTexCoordPointer(2, GL_FLOAT, 0, &TexCoords[0]);

    render_data.glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
    render_data.glEnable(GL_BLEND);
    render_data.glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    render_data.glDrawElements(GL_TRIANGLES, num_indices, GL_UNSIGNED_SHORT, newIndicies);
    render_data.glDisableClientState(GL_VERTEX_ARRAY);
    render_data.glDisableClientState(GL_COLOR_ARRAY);
    render_data.glDisableClientState(GL_TEXTURE_COORD_ARRAY);

    if (sdl_texture) {
        SDL_GL_UnbindTexture(sdl_texture);
        render_data.glDisableClientState(GL_TEXTURE_COORD_ARRAY);
    }

    render_data.glColor4f(1.0, 1.0, 1.0, 1.0);
    render_data.glPopMatrix();
}
```

```c++
    SDL_Texture* sdl_texture = NULL;
    if(texture) render_data.glUseProgram(program_texture_id);
    else render_data.glUseProgram(program_color_id);
    int width, height;
    SDL_Rect rvp;
    SDL_GetRenderViewport(renderer, &rvp);

    GLfloat projection[4][4];

    // Prepare an orthographic projection
    projection[0][0] = 2.0f / rvp.w;
    projection[0][1] = 0.0f;
    projection[0][2] = 0.0f;
    projection[0][3] = 0.0f;
    projection[1][0] = 0.0f;
    //if (renderer->target) {
    //    projection[1][1] = 2.0f / height;
    //} else {
        projection[1][1] = -2.0f / rvp.h;
    //}
    projection[1][2] = 0.0f;
    projection[1][3] = 0.0f;
    projection[2][0] = 0.0f;
    projection[2][1] = 0.0f;
    projection[2][2] = 0.0f;
    projection[2][3] = 0.0f;
    projection[3][0] = -1.0f;
    //if (renderer->target) {
    //    projection[3][1] = -1.0f;
    //} else {
        projection[3][1] = 1.0f;
    //}
    projection[3][2] = 0.0f;
    projection[3][3] = 1.0f;

    // Set the projection matrix
    if (texture) {
        render_data.glUniformMatrix4fv(u_texture_projection, 1, GL_FALSE, (GLfloat *)projection);
        render_data.glUniform2f(u_texture_translation, translation.x, translation.y);
    } else {
        render_data.glUniformMatrix4fv(u_color_projection, 1, GL_FALSE, (GLfloat *)projection);
        render_data.glUniform2f(u_color_translation, translation.x, translation.y);
    }

    render_data.glEnable(GL_BLEND);
    render_data.glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    float texw, texh;

    unsigned short newIndicies[num_indices];
    for (int i = 0; i < num_indices; i++) {
      newIndicies[i] = (unsigned short) indices[i];
    }

    glVertexAttribPointer(ROCKETGLUE_ATTRIBUTE_POSITION, 2, GL_FLOAT, GL_FALSE, sizeof(Rocket::Core::Vertex), &vertices[0].position);
    glVertexAttribPointer(ROCKETGLUE_ATTRIBUTE_COLOR, 4, GL_UNSIGNED_BYTE, GL_TRUE, sizeof(Rocket::Core::Vertex), &vertices[0].colour);
    render_data.glEnableVertexAttribArray(ROCKETGLUE_ATTRIBUTE_POSITION);
    render_data.glEnableVertexAttribArray(ROCKETGLUE_ATTRIBUTE_TEXCOORD);
    render_data.glEnableVertexAttribArray(ROCKETGLUE_ATTRIBUTE_COLOR);

    if (texture) {
        sdl_texture = (SDL_Texture *) texture;
        SDL_GL_BindTexture(sdl_texture, &texw, &texh);
        render_data.glUniform1i(u_texture, 0);
        glVertexAttribPointer(ROCKETGLUE_ATTRIBUTE_TEXCOORD, 2, GL_FLOAT, GL_FALSE, sizeof(Rocket::Core::Vertex), &vertices[0].tex_coord);
    } else {
        render_data.glActiveTexture(GL_TEXTURE0);
        render_data.glDisable(GL_TEXTURE_2D);
        render_data.glDisableVertexAttribArray(ROCKETGLUE_ATTRIBUTE_TEXCOORD);
    }

    render_data.glDrawElements(GL_TRIANGLES, num_indices, GL_UNSIGNED_SHORT, newIndicies);

    /* We can disable ROCKETGLUE_ATTRIBUTE_COLOR (2) safely as SDL will reenable the vertex attrib 2 if it is required */
    render_data.glDisableVertexAttribArray(ROCKETGLUE_ATTRIBUTE_COLOR);

    /* Leave ROCKETGLUE_ATTRIBUTE_POSITION (0) and ROCKETGLUE_ATTRIBUTE_TEXCOORD (1) enabled for compatibility with SDL which
       doesn't re enable them when you call RenderCopy/Ex */
    if(sdl_texture) SDL_GL_UnbindTexture(sdl_texture);
    else render_data.glEnableVertexAttribArray(ROCKETGLUE_ATTRIBUTE_TEXCOORD);

    /* Reset blending and draw a fake point just outside the screen to let SDL know that it needs to reset its state in case it wants to render a texture */
    render_data.glDisable(GL_BLEND);
    SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_NONE);
    SDL_RenderPoint(renderer, -1, -1);
```

## Related Functions

* [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent.md)
* [SDL_GL_UnbindTexture](SDL_GL_UnbindTexture.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
