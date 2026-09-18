# Web académica de Ricard Grebol

Código fuente de <https://ricardgrebol.com>, una web académica construida
con Jekyll y publicada mediante GitHub Pages.

## Publicación

El flujo de trabajo utiliza GitHub Pages como entorno de construcción, por lo
que no requiere una instalación local de Ruby, Bundler o Jekyll:

```sh
git add -A
git commit -m "Descripción del cambio"
git push origin main
```

Cada actualización de `main` inicia una nueva publicación. El estado del
proceso puede consultarse en la pestaña **Actions** del repositorio. Una vez
terminado, conviene recargar la web sin caché para comprobar la versión nueva.

La carpeta generada `_site/`, las credenciales y los tokens privados no deben
incluirse en el repositorio.

## Crear una web a partir de este repositorio

El repositorio puede bifurcarse en GitHub o clonarse directamente:

```sh
git clone https://github.com/ricardbcn/ricardgrebol.github.io.git
```

Para adaptar una copia:

1. Sustituir el título, la descripción, la URL y los datos del autor en
   `_config.yml`.
2. Actualizar la fotografía, el nombre, el correo y la navegación en
   `_includes/sidebar.html`.
3. Reemplazar el contenido académico en `index.md` y los archivos de
   `papers/`, `photos/` y `resume/`.
4. Eliminar `CNAME` si no se utiliza un dominio propio, o sustituir su
   contenido por el dominio correspondiente.
5. Activar GitHub Pages desde **Settings → Pages**, publicando la rama `main`
   desde la raíz del repositorio.

Para una web de usuario en GitHub Pages, el repositorio suele llamarse
`usuario.github.io`.

## Estructura principal

- `index.md`: página principal, publicaciones, proyectos, resúmenes, docencia
  y enlaces al CV.
- `_config.yml`: configuración general de Jekyll, URL, extensiones,
  comentarios y analítica.
- `_includes/sidebar.html`: retrato, identidad, contacto y navegación.
- `_includes/head.html`: metadatos, favicon, hojas de estilo, MathJax, feed y
  SEO.
- `_layouts/`: estructuras HTML reutilizadas por páginas, entradas y
  etiquetas.
- `public/css/hyde.css`: layout, tipografía, barra lateral y temas de color.
- `public/css/poole.css`: estilos base y componentes del tema.
- `public/css/custom.css`: estilos específicos de la página principal.
- `papers/`, `photos/` y `resume/`: documentos e imágenes públicas.
- `CNAME`, `robots.txt` y `atom.xml`: dominio, indexación y feed.

## Actualizaciones habituales

- **Cambiar el retrato:** sustituir `photos/N22-1508.jpg` conservando el
  nombre, o modificar el atributo `src` correspondiente en
  `_includes/sidebar.html`.
- **Actualizar el CV:** sustituir `resume/CV_RicardGrebol.pdf`; si cambia el
  nombre del archivo, actualizar también sus enlaces en `index.md` y
  `_includes/sidebar.html`.
- **Añadir o actualizar un artículo:** guardar el PDF en `papers/` y editar
  en `index.md` el título, los autores, el enlace y el resumen.
- **Editar la presentación, los proyectos o la docencia:** modificar la sección
  correspondiente de `index.md`.
- **Cambiar los datos de contacto, la navegación o los enlaces de perfil
  (Google Scholar, CV):** editar `_includes/sidebar.html`.
- **Cambiar colores o estilos:** el tema activo es `theme-base-forest`
  (clase del `body` en `_layouts/default.html`); sus colores se definen como
  variables al principio de ese tema en `public/css/hyde.css`. Utilizar
  `public/css/custom.css` para ajustes específicos. Los colores del modo oscuro
  están en el bloque `html[data-theme="dark"]` del mismo archivo; el modo inicial
  (preferencia guardada o la del sistema) se fija en `_includes/head.html` y el
  botón luna/sol está en `_includes/sidebar.html`.
- **Cambiar el favicon:** sustituir `public/favicon.ico`.
- **Cambiar el dominio:** actualizar `url` en `_config.yml` y editar o
  eliminar `CNAME`, según se utilice o no un dominio propio.

## Actualizar contenido

Conviene mantener estables los nombres públicos de los PDF para no romper
enlaces existentes. Si cambia un nombre, su referencia en `index.md` debe
actualizarse en el mismo commit.

La carpeta `papers/` también funciona como histórico de versiones. Un PDF que
no tenga un enlace activo puede formar parte de ese seguimiento y no debe
eliminarse únicamente por estar sin referencias.

Cada control de resumen en `index.md` contiene:

- un enlace con la clase `abs-toggle`;
- un panel con un atributo `id` único;
- una referencia a ese mismo identificador en el atributo `onclick`.

El catálogo de `photos/` incluye alternativas conservadas para cambios de
diseño futuros. La ausencia de una referencia activa no implica necesariamente
que una imagen deba eliminarse.

## Infraestructura opcional de blog

El repositorio conserva soporte para publicaciones aunque actualmente no
contenga entradas:

- `_layouts/post.html`, `_layouts/page.html` y `_layouts/tagpage.html`;
- archivos de archivo, etiquetas, comentarios y enlaces sociales en
  `_includes/`;
- rutas de categorías y feed mediante `category.html` y `atom.xml`;
- resaltado de código en `public/css/syntax.css`;
- generación de páginas de etiquetas mediante `tag_generator.py`.

Las entradas se guardan como `_posts/AAAA-MM-DD-identificador.md` con cabecera
YAML de Jekyll. Después de modificar sus etiquetas, las páginas correspondientes
pueden regenerarse con:

```sh
python tag_generator.py
```

MathJax está disponible para contenido matemático. Google Analytics permanece
desactivado mientras `google_analytics` esté vacío en `_config.yml`. Disqus se
configura mediante `disqus.shortname` en el mismo archivo.

## Comprobaciones recomendadas

Después de publicar, revisar:

- la página principal y la página 404;
- los enlaces al CV, los artículos y las imágenes;
- la apertura y el cierre de los resúmenes;
- la navegación y el desplazamiento de la barra lateral;
- el resultado en pantallas de escritorio y móviles;
- las categorías, etiquetas y el feed si se utiliza el blog.

## Créditos y licencia

La web está basada en [Hyde](https://github.com/poole/hyde), distribuido con
licencia MIT. La licencia original se conserva en `LICENSE.md`. La tipografía
Cooper Hewitt se distribuye con licencia SIL Open Font License 1.1, que se
conserva en `fonts/cooper_hewitt/OFL.txt`.

## Referencia de archivos permanentes

Esta referencia enumera los archivos técnicos que forman la web. No detalla el
contenido reemplazable de `papers/`, `photos/`, `resume/`, `icons/` o
`fonts/`.

### Archivos de la raíz

- `.gitignore`: evita que Git registre archivos temporales, cachés y resultados
  de compilación.
- `_config.yml`: configuración central de Jekyll, metadatos, URL, extensiones,
  valores predeterminados, Disqus y Google Analytics.
- `404.html`: página mostrada cuando una dirección no existe.
- `atom.xml`: plantilla del feed Atom para las publicaciones del blog.
- `category.html`: página que agrupa las publicaciones por categorías.
- `CNAME`: asocia GitHub Pages con el dominio personalizado. Es opcional en
  copias que utilicen únicamente un dominio `github.io`.
- `index.md`: contenido y estructura de la página principal.
- `LICENSE.md`: licencia MIT original del tema.
- `README.md`: documentación de uso y mantenimiento del repositorio.
- `robots.txt`: instrucciones básicas para buscadores y referencia al sitemap.
- `tag_generator.py`: genera las páginas de etiquetas a partir de las entradas
  almacenadas en `_posts/`.

### Componentes reutilizables: `_includes/`

- `_includes/archive.html`: crea el listado de etiquetas utilizado como
  archivo del blog.
- `_includes/collecttags.html`: recopila y ordena las etiquetas presentes en
  las publicaciones.
- `_includes/disqus_comments.html`: inserta el sistema de comentarios Disqus
  cuando está configurado.
- `_includes/google_analytics.html`: carga Google Analytics 4 únicamente si
  existe un identificador en `_config.yml`.
- `_includes/head.html`: construye la sección `<head>` con metadatos, estilos,
  favicon, feed, MathJax, Font Awesome y SEO.
- `_includes/icon_link.html`: componente auxiliar para crear enlaces formados
  por un icono y texto.
- `_includes/mathjax.html`: configura y carga MathJax para mostrar fórmulas.
- `_includes/sidebar.html`: define el retrato, la identidad, el contacto y la
  navegación lateral.
- `_includes/social_links.html`: genera enlaces sociales cuando existe la
  configuración opcional `site.data.social`.

### Plantillas de página: `_layouts/`

- `_layouts/default.html`: estructura HTML común, tema activo, cabecera y barra
  lateral.
- `_layouts/page.html`: plantilla para páginas convencionales.
- `_layouts/post.html`: plantilla para entradas, con fecha, etiquetas,
  publicaciones relacionadas y comentarios.
- `_layouts/tagpage.html`: plantilla de las páginas que reúnen publicaciones
  con una misma etiqueta.

### Hojas de estilo: `public/css/`

- `public/css/custom.css`: reglas específicas de la página principal, enlaces
  de artículos y controles de resúmenes.
- `public/css/hyde.css`: layout general, tipografía Cooper Hewitt, barra
  lateral, temas de color y variantes responsive.
- `public/css/poole.css`: estilos base para texto, listas, tablas, código,
  páginas, entradas y paginación.
- `public/css/syntax.css`: colores utilizados para el resaltado de código.

### Recurso técnico

- `public/favicon.ico`: icono principal mostrado por el navegador.
