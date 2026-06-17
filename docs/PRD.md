# PRD – **type‑refactor**

**Product:** `type-refactor` – a TypeScript‑specific refactoring engine that automatically detects, suggests, and applies code‑optimizations to improve maintainability, performance, and type‑safety across JavaScript/TypeScript projects.  

**Owner:** Senior Product/Engineering Lead – Axentx  

**Date:** 2026‑06‑17  

---  

## 1. Problem Statement  

| Symptom | Impact |
|---------|--------|
| Large TypeScript codebases accumulate **technical debt** (unused imports, overly‑broad types, duplicated interfaces, dead code). | Slower CI builds, higher bug‑rate, increased onboarding time. |
| Manual refactoring is **time‑consuming** and error‑prone, especially for cross‑module type changes. | Engineers spend ~15 % of sprint capacity on “clean‑up” tasks. |
| Existing generic refactoring tools (e.g., ESLint, Prettier) lack **deep type‑aware transformations** and cannot safely rename or restructure complex type hierarchies. | Missed opportunities for performance gains and API stability. |

**Bottom‑line:** Teams need an automated, type‑aware refactoring assistant that can safely apply best‑practice transformations at scale, freeing developer capacity and reducing production defects.

---

## 2. Target Users  

| Persona | Primary Pain | Desired Outcome |
|---------|--------------|-----------------|
| **Frontend Engineer** (mid‑senior) | Maintaining large React/Next.js apps with evolving type definitions. | One‑click safe type‑renames, interface extraction, and dead‑code removal. |
| **Backend Engineer** (Node/Express) | Managing shared libraries and DTOs across services. | Automated propagation of type changes across repo boundaries. |
| **Tech Lead / Architecture Owner** | Enforcing coding standards and preventing regression after refactors. | CI‑integrated checks that auto‑apply approved refactors or block PRs. |
| **DevOps / CI Engineer** | Keeping CI pipelines fast and reliable. | Incremental refactoring that reduces build time and lint errors. |

---

## 3. Goals (SMART)

| # | Goal | Metric | Target | Timeframe |
|---|------|--------|--------|-----------|
| G1 | **Increase developer productivity** by reducing manual refactor effort. | Avg. hours per sprint spent on refactor tasks. | ↓ 30 % from baseline. | 12 weeks |
| G2 | **Improve code health** measured by TypeScript compile warnings and ESLint errors. | % reduction in warnings/errors per PR. | ↓ 40 % (baseline = 12 warnings/PR). | 12 weeks |
| G3 | **Achieve safe automated refactoring** with < 0.5 % regression rate. | Post‑refactor regression bugs (detected in CI). | ≤ 0.5 % of total PRs. | 12 weeks |
| G4 | **Drive adoption** across internal Axentx projects. | Number of active repositories using `type‑refactor`. | ≥ 5 repos (≥ 200 k LOC total). | 12 weeks |
| G5 | **Validate market demand** via external pilot. | Signed pilot agreements with ≥ 2 external teams. | 2 pilots. | 16 weeks |

---

## 4. Key Features (Prioritized)

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|---------------------|
| **P1** | **Core Refactoring Engine** | LLM‑powered analysis (vLLM) + rule‑based transforms for TypeScript AST. | - Detects ≥ 30 predefined anti‑patterns (unused imports, any‑type, duplicate interfaces).<br>- Generates correct diff that passes `tsc --noEmit` and ESLint. |
| **P1** | **CLI Interface** | `type-refactor` command for batch processing, CI integration. | - `type-refactor run <path>` applies safe transforms.<br>- `--dry-run` outputs preview without file changes.<br>- Exit codes: 0 (no changes), 1 (changes applied), 2 (errors). |
| **P2** | **VS Code Extension** | Inline suggestions, one‑click apply, diagnostics panel. | - Shows suggestions in Problems view.<br>- “Apply All” button respects user config.<br>- No performance degradation > 200 ms per file load. |
| **P2** | **Configurable Rule Set** | JSON/YAML schema to enable/disable specific refactors, set severity. | - Users can toggle any of the 30+ rules.<br>- Config hot‑reloaded in VS Code and CLI. |
| **P3** | **CI/CD Guardrail** | GitHub Action that blocks PRs with high‑risk refactors unless approved. | - Action runs on PR, posts comment with suggested changes.<br>- Fails only when `dangerous` flag is true and no reviewer approval. |
| **P3** | **Telemetry & Reporting Dashboard** | Aggregates refactor counts, regression stats, adoption metrics (leverages Axentx BRAIN). | - Dashboard shows per‑repo stats, trend lines.<br>- Data stored in pgvector for future ML improvements. |
| **P4** | **Enterprise License & CLI Auth** | Token‑based usage tracking for external pilots. | - CLI refuses to run without valid token.<br>- Admin portal to generate/manage tokens. |

---

##
