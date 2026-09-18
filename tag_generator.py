#!/usr/bin/env python

"""
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
"""

import glob
import os


POST_DIR = '_posts/'
TAG_DIR = 'tag/'

filenames = glob.glob(POST_DIR + '*.md')
total_tags = []

for filename in filenames:
    print(filename)
    with open(filename, 'r', encoding='utf-8', errors='ignore') as post:
        reading_front_matter = False
        for line in post:
            if reading_front_matter:
                current_tags = line.strip().split()
                if current_tags and current_tags[0] == 'tags:':
                    total_tags.extend(current_tags[1:])
                    break
            if line.strip() == '---':
                reading_front_matter = not reading_front_matter
                if not reading_front_matter:
                    break

total_tags = set(total_tags)

# Remove generated pages first so deleted tags do not leave stale files behind.
for old_tag in glob.glob(TAG_DIR + '*.md'):
    os.remove(old_tag)

if not os.path.exists(TAG_DIR):
    os.makedirs(TAG_DIR)

for tag in total_tags:
    tag_filename = TAG_DIR + tag + '.md'
    with open(tag_filename, 'w', encoding='utf-8') as tag_page:
        # Jekyll uses this front matter to render the matching tag archive.
        front_matter = (
            '---\n'
            'layout: tagpage\n'
            f'title: "Tag: {tag}"\n'
            f'tag: {tag}\n'
            'robots: noindex\n'
            '---\n'
        )
        tag_page.write(front_matter)

print('Tags generated, count', len(total_tags))
