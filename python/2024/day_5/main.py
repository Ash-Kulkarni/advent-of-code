def get_rules_and_updates():
    with open("input.txt") as f:
        rules, updates = f.read().split("\n\n")
        return rules.splitlines(), [u.split(",") for u in updates.splitlines()]


def build_deps(rules):
    deps = {}
    for r in rules:
        depends_on, x = r.split("|")
        if x not in deps:
            deps[x] = []
        deps[x].append(depends_on)
    return deps


def is_valid(deps, u):
    for i, n in enumerate(u):
        if n in deps:
            for d in deps[n]:
                if d in u[i:]:
                    return False
    return True


def part_1():
    rules, updates = get_rules_and_updates()
    deps = build_deps(rules)
    valid = [u for u in updates if is_valid(deps, u)]
    print(sum(int(u[len(u) // 2]) for u in valid))


def fix_invalid(update, deps):
    subdeps = {n: [d for d in deps.get(n, []) if d in update] for n in update}
    visited = set()
    result = []

    def visit(n):
        if n not in visited:
            for d in subdeps.get(n, []):
                visit(d)
            visited.add(n)
            result.append(n)

    for n in update:
        visit(n)

    return result[::-1]


def part_2():
    rules, updates = get_rules_and_updates()
    deps = build_deps(rules)
    invalid = [u for u in updates if not is_valid(deps, u)]
    fixed = [fix_invalid(i, deps) for i in invalid]
    print(sum(int(u[len(u) // 2]) for u in fixed))


part_1()
part_2()
