import fs from 'fs';
const input = fs.readFileSync('input.txt', 'utf8');
const lines = input.split('\n').filter(l => l.trim() !== '')
const s = lines.map(line => line.split('   ').map(Number))

const l1 = s.map(([x, _]) => x)
const l2 = s.map(([_, x]) => x)

const numSort = (a, b) => a - b;
const sl1 = [...l1].sort(numSort)
const sl2 = [...l2].sort(numSort)

const zipped = sl1.map((v, i) => [v, sl2[i]])
const diffs = zipped.map(([a, b]) => Math.abs(a - b))
const total_diff = diffs.reduce((a, b) => a + b, 0)

console.log({ total_diff })
