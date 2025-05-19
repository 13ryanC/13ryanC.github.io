source "https://rubygems.org"

gem "jekyll", "~> 3.9.0"
gem "jekyll-feed", "~> 0.15.0"
gem "jekyll-seo-tag", "~> 2.7.1"
gem "jekyll-paginate", "~> 1.1.0"

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# For kramdown and GFM compatibility
gem "kramdown-parser-gfm", "~> 1.1.0"

# For GitHub Pages compatibility
gem "github-pages", group: :jekyll_plugins
