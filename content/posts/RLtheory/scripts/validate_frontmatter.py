#!/usr/bin/env python3
"""
Front Matter Validation Script for RLtheory Markdown Files

This script validates and can automatically fix front matter inconsistencies
in markdown files according to the standardized format.

Usage:
  python validate_frontmatter.py [--fix] [--path DIR]

Standard front matter format:
  date: "YYYY-MM-DD"
  title: "Descriptive Title"
  summary: "Brief description"
  lastmod: "YYYY-MM-DD"
  category: Notes|Plan|Reference
  series: ["Series Name", "Subseries"]
  author: "Bryan Chan"
  hero: /assets/images/hero3.png
  image: /assets/images/card3.png
"""

import os
import re
import yaml
import argparse
from datetime import date
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional


class FrontMatterValidator:
    """Validates and fixes front matter in markdown files."""

    # Standard field requirements
    REQUIRED_FIELDS = ['date', 'title', 'summary', 'category', 'series', 'author']
    RECOMMENDED_FIELDS = ['lastmod', 'hero', 'image']

    # Valid values for specific fields
    VALID_CATEGORIES = ['Notes', 'Plan', 'Reference']
    VALID_SERIES = ['RL Theory', 'RL Topics', 'MARL', 'SuttonBarto', 'DL Theory', 'MAS', 'Continual Learning']

    # Standard values
    STANDARD_AUTHOR = "Bryan Chan"
    STANDARD_HERO = "/assets/images/hero3.png"
    STANDARD_IMAGE = "/assets/images/card3.png"

    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path)
        self.issues = []
        self.files_processed = 0

    def find_markdown_files(self) -> List[Path]:
        """Find all markdown files with front matter."""
        md_files = []
        for file_path in self.root_path.rglob("*.md"):
            if self.has_front_matter(file_path):
                md_files.append(file_path)
        return md_files

    def has_front_matter(self, file_path: Path) -> bool:
        """Check if file has YAML front matter."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                return content.startswith('---\\n') and '\\n---\\n' in content[4:]
        except Exception:
            return False

    def extract_front_matter(self, file_path: Path) -> Tuple[Optional[Dict], str]:
        """Extract YAML front matter and content from markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if not content.startswith('---\\n'):
                return None, content

            # Find the closing ---
            end_marker = content.find('\\n---\\n', 4)
            if end_marker == -1:
                return None, content

            yaml_content = content[4:end_marker]
            remaining_content = content[end_marker + 5:]

            front_matter = yaml.safe_load(yaml_content)
            return front_matter, remaining_content

        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None, ""

    def validate_file(self, file_path: Path) -> List[Dict[str, Any]]:
        """Validate front matter for a single file."""
        issues = []
        front_matter, content = self.extract_front_matter(file_path)

        if front_matter is None:
            return [{'file': str(file_path), 'type': 'no_front_matter', 'message': 'No front matter found'}]

        # Check required fields
        for field in self.REQUIRED_FIELDS:
            if field not in front_matter:
                issues.append({
                    'file': str(file_path),
                    'type': 'missing_field',
                    'field': field,
                    'message': f'Missing required field: {field}'
                })

        # Check recommended fields
        for field in self.RECOMMENDED_FIELDS:
            if field not in front_matter:
                issues.append({
                    'file': str(file_path),
                    'type': 'missing_recommended_field',
                    'field': field,
                    'message': f'Missing recommended field: {field}'
                })

        # Validate specific fields
        if 'category' in front_matter:
            category = front_matter['category']
            # Handle quoted categories
            if isinstance(category, str) and category.startswith('"') and category.endswith('"'):
                issues.append({
                    'file': str(file_path),
                    'type': 'category_quoted',
                    'field': 'category',
                    'current': category,
                    'recommended': category.strip('"'),
                    'message': f'Category should not be quoted: {category}'
                })

            # Map Tutorial to Notes
            clean_category = str(category).strip('"')
            if clean_category == 'Tutorial':
                issues.append({
                    'file': str(file_path),
                    'type': 'category_standardization',
                    'field': 'category',
                    'current': category,
                    'recommended': 'Notes',
                    'message': 'Tutorial category should be Notes'
                })
            elif clean_category == 'Taxonomy':
                issues.append({
                    'file': str(file_path),
                    'type': 'category_standardization',
                    'field': 'category',
                    'current': category,
                    'recommended': 'Reference',
                    'message': 'Taxonomy category should be Reference'
                })

        # Validate author field
        if 'author' in front_matter:
            author = front_matter['author']
            if isinstance(author, str) and author.startswith('Author: '):
                issues.append({
                    'file': str(file_path),
                    'type': 'author_prefix',
                    'field': 'author',
                    'current': author,
                    'recommended': author.replace('Author: ', ''),
                    'message': 'Author field should not have "Author:" prefix'
                })
            elif author != self.STANDARD_AUTHOR:
                issues.append({
                    'file': str(file_path),
                    'type': 'author_nonstandard',
                    'field': 'author',
                    'current': author,
                    'recommended': self.STANDARD_AUTHOR,
                    'message': f'Non-standard author: {author}'
                })

        # Validate date format
        if 'date' in front_matter:
            date_str = str(front_matter['date']).strip('"')
            if not re.match(r'^\\d{4}-\\d{2}-\\d{2}$', date_str):
                issues.append({
                    'file': str(file_path),
                    'type': 'date_format',
                    'field': 'date',
                    'current': front_matter['date'],
                    'message': f'Date should be YYYY-MM-DD format: {front_matter["date"]}'
                })

        # Check for title typos
        if 'title' in front_matter:
            title = front_matter['title']
            if 'Traeat' in str(title):
                issues.append({
                    'file': str(file_path),
                    'type': 'title_typo',
                    'field': 'title',
                    'current': title,
                    'recommended': str(title).replace('Traeat', 'Treat'),
                    'message': 'Title contains typo: "Traeat" should be "Treat"'
                })

        return issues

    def fix_front_matter(self, file_path: Path, issues: List[Dict[str, Any]]) -> bool:
        """Apply automatic fixes to front matter issues."""
        front_matter, content = self.extract_front_matter(file_path)
        if front_matter is None:
            return False

        modified = False
        today = date.today().strftime("%Y-%m-%d")

        for issue in issues:
            if issue['type'] == 'category_quoted':
                front_matter['category'] = issue['recommended']
                modified = True
            elif issue['type'] == 'category_standardization':
                front_matter['category'] = issue['recommended']
                modified = True
            elif issue['type'] == 'author_prefix':
                front_matter['author'] = issue['recommended']
                modified = True
            elif issue['type'] == 'author_nonstandard':
                # Only fix if it's a known template or obvious error
                if 'template' in issue['current'].lower() or issue['current'] == 'ChatGPT':
                    front_matter['author'] = self.STANDARD_AUTHOR
                    modified = True
            elif issue['type'] == 'title_typo':
                front_matter['title'] = issue['recommended']
                modified = True
            elif issue['type'] == 'missing_recommended_field':
                if issue['field'] == 'lastmod':
                    front_matter['lastmod'] = f'"{today}"'
                    modified = True
                elif issue['field'] == 'hero':
                    front_matter['hero'] = self.STANDARD_HERO
                    modified = True
                elif issue['field'] == 'image':
                    front_matter['image'] = self.STANDARD_IMAGE
                    modified = True

        if modified:
            self.write_front_matter(file_path, front_matter, content)
            return True
        return False

    def write_front_matter(self, file_path: Path, front_matter: Dict, content: str):
        """Write updated front matter back to file."""
        try:
            yaml_str = yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)
            new_content = f"---\\n{yaml_str}---\\n{content}"

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

        except Exception as e:
            print(f"Error writing to {file_path}: {e}")

    def validate_all(self, fix: bool = False) -> Dict[str, Any]:
        """Validate all markdown files."""
        files = self.find_markdown_files()
        all_issues = []
        files_fixed = 0

        for file_path in files:
            self.files_processed += 1
            file_issues = self.validate_file(file_path)

            if file_issues:
                all_issues.extend(file_issues)

                if fix:
                    if self.fix_front_matter(file_path, file_issues):
                        files_fixed += 1
                        print(f"Fixed: {file_path}")

        # Summary by issue type
        issue_counts = {}
        for issue in all_issues:
            issue_type = issue['type']
            issue_counts[issue_type] = issue_counts.get(issue_type, 0) + 1

        return {
            'total_files': len(files),
            'files_with_issues': len(set(issue['file'] for issue in all_issues)),
            'files_fixed': files_fixed,
            'total_issues': len(all_issues),
            'issues': all_issues,
            'issue_counts': issue_counts
        }


def main():
    parser = argparse.ArgumentParser(description='Validate front matter in markdown files')
    parser.add_argument('--fix', action='store_true', help='Automatically fix issues where possible')
    parser.add_argument('--path', default='.', help='Root path to search for markdown files')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')

    args = parser.parse_args()

    validator = FrontMatterValidator(args.path)
    results = validator.validate_all(fix=args.fix)

    print(f"\\n=== Front Matter Validation Results ===")
    print(f"Total files processed: {results['total_files']}")
    print(f"Files with issues: {results['files_with_issues']}")
    if args.fix:
        print(f"Files fixed: {results['files_fixed']}")
    print(f"Total issues found: {results['total_issues']}")

    if results['issue_counts']:
        print(f"\\n=== Issue Breakdown ===")
        for issue_type, count in sorted(results['issue_counts'].items()):
            print(f"  {issue_type}: {count}")

    if args.verbose and results['issues']:
        print(f"\\n=== Detailed Issues ===")
        for issue in results['issues']:
            print(f"  {issue['file']}: {issue['message']}")

    return 0 if results['total_issues'] == 0 else 1


if __name__ == '__main__':
    exit(main())