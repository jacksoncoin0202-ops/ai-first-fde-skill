#!/usr/bin/env python3
from pathlib import Path
import re, sys, json

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
SKILLS = ROOT / 'skills'
SECRET_PATTERNS = [
    r'gho_[A-Za-z0-9_]+', r'sk-[A-Za-z0-9]+', r'AKIA[0-9A-Z]{16}',
    r'BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY', r'password\s*[:=]\s*[^\s]+'
]
required = ['README.md', 'README.zh-Hant.md', 'README.zh-CN.md', 'README.en.md', 'README.ja.md', 'LICENSE', 'SECURITY.md']
errors = []
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f'missing {rel}')
if not SKILLS.exists():
    errors.append('missing skills directory')
else:
    for skill in sorted(SKILLS.iterdir()):
        if not skill.is_dir():
            continue
        sm = skill / 'SKILL.md'
        if not sm.exists():
            errors.append(f'{skill.name}: missing SKILL.md')
            continue
        txt = sm.read_text(encoding='utf-8')
        if not txt.startswith('---'):
            errors.append(f'{skill.name}: missing YAML frontmatter')
        if f'name: {skill.name}' not in txt:
            errors.append(f'{skill.name}: frontmatter name mismatch')
        if 'description:' not in txt:
            errors.append(f'{skill.name}: missing description')
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.md', '.txt', '.yml', '.yaml', '.json', '.py'}:
        txt = path.read_text(encoding='utf-8', errors='ignore')
        for pat in SECRET_PATTERNS:
            if re.search(pat, txt, flags=re.I):
                errors.append(f'secret-like pattern in {path.relative_to(ROOT)}: {pat}')
print(json.dumps({'ok': not errors, 'errors': errors}, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
