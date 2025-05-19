# Gemfile — simplified and GitHub‑Pages‑compatible
# -------------------------------------------------
# This layout keeps your local environment in lock‑step with what GitHub Pages
# runs in production, avoiding the “works on my machine” problem.

source "https://rubygems.org"

# 1️⃣  Meta‑gem that pins Jekyll and every *allowed* plugin
#     to the exact versions GitHub Pages builds with.
gem "github-pages", group: :jekyll_plugins

# 2️⃣  WEBrick was removed from Ruby ≥ 3.0 stdlib; Jekyll still expects it.
#     Required only for `bundle exec jekyll serve` on your Mac.
gem "webrick", "~> 1.8"

# 3️⃣  If you decide to stay on Ruby 3.2/3.3, uncomment the line below so that
#     EventMachine (a C‑extension) picks a version that compiles. GitHub Pages
#     is fine with 1.2.9 too.
# gem "eventmachine", "~> 1.2", ">= 1.2.9"

# 4️⃣  Windows‑specific helpers — harmless but ignored on macOS.
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
gem "wdm", "~> 0.1.1", platforms: [:mingw, :x64_mingw, :mswin]
