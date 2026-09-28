# Ricard Grebol – academic website

Source code for <https://ricardgrebol.com>, an academic website built with
Jekyll and published with GitHub Pages.

## Publishing

GitHub Pages builds the site, so no local Ruby, Bundler or Jekyll installation
is needed. Commit and push to `main` (from GitHub Desktop or the command line):

```sh
git add -A
git commit -m "Describe the change"
git push origin main
```

Every push to `main` triggers a new build. Its progress is shown in the
repository's **Actions** tab. Once it finishes, reload the site without the
cache to check the new version.

Never commit the generated `_site/` folder, credentials or private tokens.

## Reusing this repository

Clone the repository:

```sh
git clone https://github.com/ricardbcn/ricardgrebol.github.io.git
```

To adapt a copy:

1. Replace the title, description, URL and author details in `_config.yml`.
2. Update the portrait, name, email, profile links and navigation in
   `_includes/sidebar.html`.
3. Replace the academic content in `index.md` and the files in `papers/`,
   `photos/` and `resume/`.
4. Delete `CNAME` if no custom domain is used, or replace its content with
   your own domain.
5. Enable GitHub Pages under **Settings → Pages**, publishing the `main`
   branch from the repository root.

## Main structure

- `index.md`: home page with the introduction, working papers, work in
  progress, teaching, publications, abstracts and CV link.
- `_config.yml`: general Jekyll settings, URL, plugins, comments and analytics.
- `_includes/sidebar.html`: portrait, name, contact, profile icons (email,
  Google Scholar, CV), light/dark toggle and navigation.
- `_includes/head.html`: metadata, initial colour mode, favicon, stylesheets,
  icon fonts, MathJax, feed and SEO.
- `_layouts/`: HTML templates shared by pages, posts and tag pages.
- `public/css/hyde.css`: layout, typography, sidebar and colour themes.
- `public/css/poole.css`: base styles and theme components.
- `public/css/custom.css`: home page styles.
- `papers/`, `photos/` and `resume/`: public documents and images.
- `CNAME`, `robots.txt` and `atom.xml`: domain, search engine rules and feed.

## Common updates

- **Change the portrait:** replace `photos/N22-1508.jpg` keeping the same
  name, or change the `src` attribute in `_includes/sidebar.html`.
- **Update the CV:** replace `resume/CV_RicardGrebol.pdf`. If the file name
  changes, update its links in `index.md` and `_includes/sidebar.html`.
- **Add or update a paper:** save the PDF in `papers/` and edit its title,
  co-authors, link and abstract in `index.md`.
- **Edit the introduction, projects or teaching:** edit the matching section
  of `index.md`.
- **Change contact details, navigation or profile links:** edit
  `_includes/sidebar.html`.
- **Change colours or styles:** the active theme is `theme-base-forest` (the
  `body` class in `_layouts/default.html`). Its light colours are variables at
  the start of that theme in `public/css/hyde.css`, and its dark colours are in
  the `html[data-theme="dark"]` block of the same file. Use
  `public/css/custom.css` for page-specific tweaks.
- **Light/dark mode:** the initial mode (the visitor's saved choice, otherwise
  their system setting, light by default) is set in `_includes/head.html`. The
  moon/sun button and its script are in `_includes/sidebar.html`.
- **Change the favicon:** replace `public/favicon.ico`.
- **Change the domain:** update `url` in `_config.yml` and edit or delete
  `CNAME`.

## Updating content

Keep public PDF file names stable so existing links keep working. If a name
changes, update its reference in `index.md` in the same commit.

Each abstract toggle in `index.md` has:

- a link with the `abs-toggle` class;
- a panel with a unique `id`;
- a reference to that same `id` in the link's `onclick` attribute.

## Optional blog infrastructure

The repository keeps support for blog posts, although it currently has none:

- `_layouts/post.html`, `_layouts/page.html` and `_layouts/tagpage.html`;
- archive, tag, comment and social link includes in `_includes/`;
- category and feed pages in `category.html` and `atom.xml`;
- code highlighting in `public/css/syntax.css`;
- tag page generation with `tag_generator.py`.

Posts go in `_posts/YYYY-MM-DD-slug.md` with Jekyll YAML front matter. After
changing their tags, regenerate the tag pages with:

```sh
python tag_generator.py
```

MathJax is available for mathematical content. Visitor statistics use
GoatCounter (no cookies); the dashboard is at
`https://<goatcounter>.goatcounter.com`, where `<goatcounter>` is the site code
in `_config.yml`. Visit the site with `#toggle-goatcounter` appended to the URL
to stop counting your own visits in that browser. Google Analytics stays
disabled while `google_analytics` is empty in `_config.yml`. Disqus is
configured through `disqus.shortname` in the same file.

## Checks after publishing

- the home page and the 404 page;
- links to the CV, papers and images;
- opening and closing the abstracts;
- sidebar navigation and scrolling;
- desktop and phone layouts, in light and dark mode;
- categories, tags and feed, if the blog is used.

## Credits and licences

The site is based on [Hyde](https://github.com/poole/hyde), released under the
MIT licence, which is kept in `LICENSE.md`. The Cooper Hewitt typeface is
released under the SIL Open Font License 1.1, kept in
`fonts/cooper_hewitt/OFL.txt`.

## File reference

This section lists the technical files that make up the site. It does not
cover the replaceable content of `papers/`, `photos/`, `resume/`, `icons/` or
`fonts/`.

### Root files

- `.gitignore`: keeps temporary files, caches and build output out of Git.
- `_config.yml`: central Jekyll configuration, metadata, URL, plugins,
  defaults, Disqus and Google Analytics.
- `404.html`: page shown when an address does not exist.
- `atom.xml`: Atom feed template for blog posts.
- `category.html`: page grouping posts by category.
- `CNAME`: connects GitHub Pages to the custom domain. Optional for copies that
  only use a `github.io` address.
- `index.md`: content and structure of the home page.
- `LICENSE.md`: the theme's original MIT licence.
- `README.md`: usage and maintenance documentation.
- `robots.txt`: basic search engine rules and sitemap reference.
- `tag_generator.py`: generates tag pages from the posts in `_posts/`.

### Reusable components: `_includes/`

- `_includes/archive.html`: builds the tag list used as the blog archive.
- `_includes/collecttags.html`: collects and sorts the tags used in posts.
- `_includes/disqus_comments.html`: adds Disqus comments when configured.
- `_includes/google_analytics.html`: loads Google Analytics 4 only if an ID is
  set in `_config.yml`.
- `_includes/goatcounter.html`: loads GoatCounter analytics when
  `goatcounter` is set in `_config.yml`, and counts clicks on PDF links
  (papers, CV) as events.
- `_includes/head.html`: builds the `<head>` with metadata, initial colour
  mode, stylesheets, favicon, feed, MathJax, Font Awesome, Academicons and SEO.
- `_includes/icon_link.html`: helper for links made of an icon and text.
- `_includes/mathjax.html`: configures and loads MathJax.
- `_includes/sidebar.html`: portrait, name, contact, profile icons with hover
  labels, light/dark toggle and navigation.
- `_includes/social_links.html`: social links when the optional
  `site.data.social` setting exists.

### Page templates: `_layouts/`

- `_layouts/default.html`: shared HTML structure, active theme, head and
  sidebar.
- `_layouts/page.html`: template for regular pages.
- `_layouts/post.html`: template for posts, with date, tags, related posts and
  comments.
- `_layouts/tagpage.html`: template for pages listing posts with the same tag.

### Stylesheets: `public/css/`

- `public/css/custom.css`: home page rules, paper links, abstract toggles,
  section spacing and teaching list.
- `public/css/hyde.css`: general layout, Cooper Hewitt typeface, sidebar,
  colour themes (including dark mode) and responsive variants.
- `public/css/poole.css`: base styles for text, lists, tables, code, pages,
  posts and pagination.
- `public/css/syntax.css`: code highlighting colours.

### Technical asset

- `public/favicon.ico`: the browser tab icon.
