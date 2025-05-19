# MyResearchNotes

This repository contains the source for **MyResearchNotes**, a Hugo-based blog powered by the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme. The site is designed for publishing research articles and tutorials related to AI.

## Local Development

1. Install [Hugo](https://gohugo.io/).
2. Clone the PaperMod theme:
   ```bash
   git submodule update --init --recursive
   ```
3. Serve the site locally:
   ```bash
   hugo server -D
   ```
4. Visit `http://localhost:1313` in your browser.

## Deployment

The site can be deployed by running `hugo` and uploading the generated `public` directory to your hosting provider or GitHub Pages.

## GitHub Pages

This repository includes a GitHub Actions workflow that automatically builds the
site with Hugo and publishes it to GitHub Pages. To enable automated deployment:

1. Configure GitHub Pages in your repository settings to use the `gh-pages`
   branch.
2. Update the `baseURL` field in `config.toml` to match your GitHub Pages URL,
   for example `https://<USERNAME>.github.io/<REPOSITORY>/`.
3. Push changes to the `main` branch. The workflow will build and deploy the
   site.

The published blog will be available at your configured GitHub Pages URL.
