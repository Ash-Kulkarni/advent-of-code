import fs from "fs";
const input = fs.readFileSync("input.txt", "utf8");

const lines = input.split("\n").filter((l) => l.trim() !== "");
const pairs = lines.map((line) => line.split("   ").map(Number));

const l1 = pairs.map(([x, _]) => x);
const l2 = pairs.map(([_, x]) => x);

// console.log({ l1, l2 });

const part1 = () => {
  const numSort = (a, b) => a - b;
  const sl1 = [...l1].sort(numSort);
  const sl2 = [...l2].sort(numSort);

  const zipped = sl1.map((v, i) => [v, sl2[i]]);
  const diffs = zipped.map(([a, b]) => Math.abs(a - b));

  let total = 0;

  diffs.forEach((d) => {
    total += d;
  });
  console.log({ total });
};

part1();

const part2 = () => {
  const countMap = {};

  l2.forEach((v) => {
    if (!countMap[v]) countMap[v] = 0;
    countMap[v]++;
  });

  const totalSimilarity = l1
    .map((x) => x * countMap[x] || 0)
    .reduce((a, b) => a + b, 0);
  console.log({ totalSimilarity });
};

part2();
