#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import vm from 'node:vm';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const viewerPath = path.join(repoRoot, '100-viewer.html');
const html = fs.readFileSync(viewerPath, 'utf8');
const errors = [];

const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map(match => match[1]);
if (!scripts.length) {
  errors.push('100-viewer.html does not contain an inline <script> block.');
}

scripts.forEach((script, index) => {
  try {
    new vm.Script(script, { filename: `100-viewer.inline-${index + 1}.js` });
  } catch (error) {
    errors.push(`Inline script ${index + 1} has a syntax error: ${error.message}`);
  }
});

const ids = new Set([...html.matchAll(/\sid=["']([^"']+)["']/g)].map(match => match[1]));
const idRefs = [...html.matchAll(/getElementById\(["']([^"']+)["']\)/g)].map(match => match[1]);
const missingIds = [...new Set(idRefs.filter(id => !ids.has(id)))];
if (missingIds.length) {
  errors.push(`Missing DOM ids referenced by getElementById: ${missingIds.join(', ')}`);
}

if (/fiłe|‹|›/.test(html)) {
  errors.push('Viewer contains previously observed corrupted overview markup characters.');
}

if (!/\.sandbox\s*=\s*['"]allow-scripts['"]/.test(html)) {
  errors.push('Slide iframes should be sandboxed with allow-scripts only.');
}

if (!/URL\.revokeObjectURL/.test(html)) {
  errors.push('Viewer should revoke object URLs when replacing decks.');
}

if (!/webkitdirectory/.test(html) || !/type="file"/.test(html)) {
  errors.push('Viewer must keep browser-native folder and file picker inputs.');
}

if (errors.length) {
  console.error(errors.map(error => `- ${error}`).join('\n'));
  process.exit(1);
}

console.log('viewer static checks passed');
