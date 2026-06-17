# STORIES.md  
**Project:** `type-refactor` – TypeScript‑specific refactoring tool  
**Goal:** Deliver an MVP that automates common TypeScript code optimizations, enforces configurable style rules, and integrates seamlessly into existing developer workflows (CLI, VS Code, CI/CD).  

---  

## Epics Overview  

| Epic ID | Title | Description | MVP Priority |
|---------|-------|-------------|--------------|
| **E1** | Core Refactoring Engine | Parse, analyze, and transform TypeScript ASTs to apply safe, automated refactorings. | ✅ |
| **E2** | CLI Interface | Provide a command‑line tool for batch processing and interactive usage. | ✅ |
| **E3** | VS Code Extension | Expose refactorings inside the editor with on‑demand suggestions and quick‑fixes. | ✅ |
| **E4** | Configurable Rule Set | Allow teams to enable/disable specific refactorings and customize thresholds. | ✅ |
| **E5** | CI/CD Integration | Offer a GitHub Action / npm script that fails builds on disallowed patterns. | ❌ |
| **E6** | Reporting & Metrics | Generate HTML/JSON reports summarizing changes, warnings, and potential savings. | ❌ |
| **E7** | Performance & Scalability | Optimize for large monorepos (≥ 1 M lines) with incremental analysis and caching. | ❌ |
| **E8** | Documentation & Onboarding | Comprehensive README, tutorials, and API docs for contributors and end‑users. | ✅ |

> **MVP** = all stories marked with ✅ must be completed before the first production release.  

---  

## User Stories  

### Epic E1 – Core Refactoring Engine  

| ID | Story | Acceptance Criteria |
|----|-------|----------------------|
| **E1‑S1** | As a **developer**, I want the tool to **detect and replace `any` types with inferred types**, so that my codebase becomes type‑safe. | - Parses all `.ts`/`.tsx` files in the supplied project root.<br>- For each `any` usage, runs type‑inference and proposes a concrete type.<br>- Generates a diff that compiles without errors.<br>- Provides a `--dry-run` mode showing proposed changes only. |
| **E1‑S2** | As a **developer**, I want the tool to **convert `for…in` loops over arrays to `for…of`**, so that runtime bugs are avoided. | - Detects `for (const key in arr)` where `arr` is typed as an array.<br>- Rewrites to `for (const item of arr)` preserving variable name semantics.<br>- Updated code passes `tsc --noEmit` with no new errors. |
| **E1‑S3** | As a **developer**, I want the engine to **merge duplicate type/interface declarations**, so that the code stays DRY. | - Finds identical `type`/`interface` definitions across files.<br>- Suggests a single shared declaration and updates all references.<br>- Handles export/import semantics correctly.<br>- No circular‑dependency introduced. |
| **E1‑S4** | As a **developer**, I want the tool to **remove unused imports**, so that the bundle size is reduced. | - Analyzes import statements and usage sites.<br>- Removes only imports that have zero references.<br>- Leaves side‑effect imports (`import "./polyfill"`) untouched.<br>- `npm run lint` passes after changes. |
| **E1‑S5** | As a **developer**, I want the engine to **upgrade `enum` usages to `as const` objects where appropriate**, so that I get better type inference. | - Detects numeric enums used only as a set of constants.<br>- Rewrites to `const MyEnum = { … } as const` and updates all references.<br>- Preserves runtime values and semantics. |

### Epic E2 – CLI Interface  

| ID | Story | Acceptance Criteria |
|----|-------|----------------------|
| **E2‑S1** | As a **build engineer**, I want a `type-refactor` CLI command with `--project <path>` flag, so that I can run it against any monorepo. | - `type-refactor --project ./my-app` scans recursively.<br>- Returns exit code `0` on success, `1` on fatal error, `2` when changes are required (non‑dry‑run). |
| **E2‑S2** | As a **developer**, I want a `--dry-run` option, so that I can preview changes before applying them. | - Outputs a concise summary (files changed, number of edits).<br>- Writes a `.type-refactor.diff` file with unified diff format. |
| **E2‑S3** | As a **developer**, I want the CLI to support `--fix <rule>` to run a single refactoring, so that I can target specific issues. | - `type-refactor --fix no-any` only applies the “no‑any” rule.<br>- Invalid rule names produce a helpful error message listing available rules. |
| **E2‑S4** | As a **CI engineer**, I want the CLI to emit JSON (`--output json`) for machine consumption, so that I can integrate it into pipelines. | - JSON includes file paths, original code snippets, transformed snippets, and rule identifiers.<br>- Schema is documented in `docs/json-schema.md`. |

### Epic E3 – VS Code Extension  

| ID | Story | Acceptance Criteria |
|----|-------|----------------------|
| **E3‑S1** | As a **frontend developer**, I want VS Code to underline code that can be refactored, so that I see suggestions inline. | - Extension registers a `CodeActionProvider` for `typescript` and `typescriptreact`.<br>- Hover tooltip explains the rule and shows before/after snippets.<br>- Clicking “Apply” runs the transformation on the open file. |
| **E3‑S2** | As a **developer**, I want a command palette entry “Type‑Refactor: Run on Workspace”, so that I can apply all fixes from the editor. | - Executes the same logic as the CLI `--project .` on the opened workspace.<br>- Shows a progress notification and a final summary dialog. |
| **E3‑S3** | As a **developer**, I want the extension to respect the project’s `.type-refactorrc` config, so that my team’s conventions are enforced. | - Reads config from workspace root.<br>- Disables any rule marked `false` in the UI. |

### Epic E4 – Configurable Rule Set  

| ID | Story | Acceptance Criteria |
|----|-------|----------------------|
| **E4‑S1** | As a **team lead**, I want a `.type-refactorrc` file (JSON) to enable/disable individual rules, so that we can adopt the tool gradually. | - File supports `{ "rules": { "no-any": true, "no-for-in": false } }`.<br>- Missing file defaults to all rules enabled.<br>- CLI and VS Code read the same config. |
| **E4‑S2** | As a **developer**, I want rule severity levels (`off`, `warn`, `error`), so that I can treat some suggestions as optional. | - Severity influences CLI exit codes (`warn` → exit 0, `error` → exit 2).<br>- VS Code shows warnings in yellow, errors in red. |
| **E4‑S3** | As a **devops engineer**, I want environment variable overrides (`TYPE_REFRACTOR_RULES=no-any:off`), so that CI can temporarily suppress noisy rules. | - Parses `TYPE_REFRACTOR_RULES` and merges with file config, precedence to env var.<br>- Documented in `README.md`. |

### Epic E5 – CI/CD Integration (Future)  

| ID | Story | Acceptance Criteria |
|----|-------|----------------------|
| **E5‑S1** | As a **CI engineer**, I want a GitHub Action `type-refactor/action` that runs on PRs, so that code quality gates are enforced automatically. | - Action checks out repo, runs `type-refactor --output json`.<br>- Fails the job if any `error`‑level violations are found.<br>- Posts a comment with a summary and a link to the full JSON artifact. |

### Epic E6 – Reporting & Metrics (Future)  

| ID | Story | Acceptance Criteria |
|----|-------|----------------------|
| **E6‑S1** | As a **product manager**, I want an HTML report summarizing refactorings per module, so that I can track maintainability improvements over time. | - Generates `report.html` with charts (files changed, rule distribution).<br>- Links each entry to the corresponding diff view. |

### Epic E7 – Performance & Scalability (Future)  

| ID | Story | Acceptance Criteria |
|----|-------|----------------------|
| **E7‑S1** | As a **build engineer**, I want incremental analysis using a cache file, so that subsequent runs on large repos are fast. | - Stores a `.type-refactor.cache` with file hashes and AST snapshots.<br>- On re‑run, only files with changed hashes are re‑analyzed.<br>- Cache invalidated when config changes. |

### Epic E8 – Documentation & Onboarding (MVP)  

| ID | Story | Acceptance Criteria |
|----|-------|----------------------|
| **E8‑S1** | As a **new contributor**, I want a **Getting Started** guide, so that I can install and run the tool locally within 10 minutes. | - README includes sections: Installation (`npm i -g type-refactor`), Quick‑start CLI example, VS Code extension install link, Config file example.<br>- All commands verified on macOS, Linux, Windows. |
| **E8‑S2** | As a **developer**, I want API documentation for the internal `RefactorEngine` class, so that I can extend the rule set. | - Generated via TypeDoc and published under `docs/api/`.<br>- Includes example of adding a custom rule plugin. |
| **E8‑S3** | As a **team lead**, I want a **FAQ** section covering common pitfalls (e.g., false‑positive `any` inference), so that support tickets are reduced. | - FAQ lives in `docs/FAQ.md` and is linked from the main README. |

---  

## Prioritization for MVP (✅)  

1. **E1‑S1**, **E1‑S2**, **E1‑S4** – high‑impact, low‑risk refactorings.  
2. **E2‑S1**, **E2‑S2**, **E2‑S4** – core CLI functionality.  
3. **E3‑S1**, **E3‑S2** – editor integration for immediate developer feedback.  
4. **E4‑S1**, **E4‑S2** – configurability and severity handling.  
5. **E8‑S1**, **E8‑S2** – documentation to enable adoption.  

All other stories (E5‑E7) are slated for post‑MVP releases.  

---  

*Prepared by the senior product/engineering lead, 2026‑06‑17.*
