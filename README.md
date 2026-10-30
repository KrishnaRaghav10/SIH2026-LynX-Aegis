# AEGIS: AICTE Approval & Compliance Management System

> **Tagline:** *"Bringing every approval under control."*  
> **Statutory Safeguard Principle:** *"Automated alerts support, but do not replace, statutory scrutiny and decisions of the competent authority."*

---

## 🏛️ Executive Summary

**AEGIS** is a digital statutory governance and compliance orchestration platform engineered for the **All India Council for Technical Education (AICTE)**. It streamlines the annual Approval Process Handbook (APH) lifecycle—covering Extension of Approval (EoA), new institutions, course additions, and post-approval compliance tracking across 10 specialized stakeholder perspectives.

---

## 👥 The 10 Dedicated Role Workbenches

AEGIS organizes the regulatory lifecycle into 10 role-specific, purpose-built portals:

| # | Role & Portal | Route | Key Capabilities |
| :---: | :--- | :--- | :--- |
| **1** | **Institution Portal** | `/institution` | 0–100 Compliance Health Ring (radial gauge), urgent attention lease alert carousel, 30-year lease validity vault, and application stage steppers. |
| **2** | **Scrutiny Officer** | `/scrutiny` | Split-pane Scrutiny Workbench with ageing heat-strips, statutory checklist evaluation matrix (Pass/Deficient/NA with remarks), and one-click electronic case summaries. |
| **3** | **Regional Officer** | `/regional` | Interactive India SVG Heat Map across 5 AICTE zones, stage-wise processing funnels, and officer workload swimlanes with case rebalancing. |
| **4** | **Bureau Officer** | `/bureau` | National Pulse command dashboard, comparative regional bar race analytics, pendency trendlines, and a persistent national alerts rail. |
| **5** | **EVC Coordinator** | `/evc` | Inspection management with an **Automated Conflict-of-Interest Guard** (blocks experts from same state/affiliating university) and a Gantt visit schedule. |
| **6** | **Committee Member** | `/committee` | Appellate hearing desk (SAC/SHC), side-by-side case dossier inspection, advisory opinion editor, and conditional approval with time-bound undertakings. |
| **7** | **Compliance Officer** | `/compliance` | Post-approval compliance follow-up with a **6-stage undertakings Kanban board**, concentric lease/NOC expiry radar (30/60/90 days), and bulk reminder engine. |
| **8** | **Senior Authority** | `/authority` | Executive Council briefing, top-of-ladder escalations, and formal decision bench. **Strict human-in-the-loop safeguard:** approvals/rejections require entering a mandatory statutory reason. |
| **9** | **System Administrator** | `/admin` | Visual node-graph workflow designer, live execution trace simulation, SLA & timeline rule configurator, and multi-level escalation ladders. |
| **10** | **Statutory Auditor** | `/auditor` | Read-only forensic audit trail, **immutable SHA-256 hash-chained ledger**, tamper-evident verification, and case provenance reconstruction playback scrubber. |

---

## ⚙️ Core Technical Architecture

```
d:\SIH 2026\
├── frontend/                     # Pure AEGIS React + TypeScript + Vite SPA
│   ├── src/
│   │   ├── app/                  # Routing, App entry, Landing, RoleRouteGuard
│   │   ├── config/               # Standardized institutional role configurations
│   │   ├── engine/               # SLA calculator, SHA-256 hash-chaining engine
│   │   ├── mock/                 # In-browser mock API & simulated state
│   │   ├── roles/                # 10 dedicated role modules
│   │   ├── shared/               # Header, AuditDrawer, CommandPalette, TimeMachine
│   │   ├── store/                # Unified Zustand state management store
│   │   ├── types/                # Domain models, enum definitions
│   │   ├── main.tsx              # TypeScript React root
│   │   └── index.css             # Institutional design tokens & Tailwind styles
│   └── public/                   # Shield branding icons & web player
├── backend/                      # Optional FastAPI statutory microservice
│   ├── app/                      # API routes, auth, forensic document processor
│   ├── rules/                    # APH statutory evaluation rule definitions
│   └── requirements.txt          # Python dependencies
├── watch_demo.html               # Zero-dependency browser walkthrough player
├── generate_synced_demo.py       # Full HD Playwright video recorder (SRT-timed)
└── AEGIS_Demo_Walkthrough.mp4    # 1080p Full HD synced demonstration video
```

### Key Technical Innovations:
1. **Interactive Simulated Clock (Time Machine):** Built-in time accelerator (`+7d`, `+30d`) allows instant live demonstration of reactive SLA breaches, auto-escalations, and deadline triggers.
2. **Cryptographic Provenance:** Every state change, role switch, document submission, and decision is cryptographically chained using SHA-256 hashes for courtroom-ready legal defense.
3. **Automated Conflict-of-Interest Filter:** Algorithmic verification prevents assigning experts to inspect colleges in their own jurisdiction, state, or affiliating university.
4. **Concentric Document Expiry Radar:** Categorizes critical institutional land leases, fire safety NOCs, and structural certificates into 30, 60, and 90-day expiration horizons.

---

## 🚀 Quick Start Guide

### Frontend (AEGIS Modern Government Portal)
```bash
cd frontend
npm install
npm run dev
```
Open **[http://localhost:5173](http://localhost:5173)** in your browser.

### Backend (Optional FastAPI Service)
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

---

## 🎬 Demonstration Video

A synchronized Full HD walkthrough demonstrating all 10 roles is included:
- **Interactive Player with Chapters:** Open [`watch_demo.html`](watch_demo.html) in your browser.
- **Walkthrough Video:** `AEGIS_Demo_Walkthrough.mp4` (1080p Full HD, 3m 15s duration).

---

## ⚖️ Governance & Compliance Standards
Built in strict adherence to:
- **AICTE Approval Process Handbook (APH)** norms
- **National Informatics Centre (NIC)** Government of India visual design guidelines
- **WCAG 2.1 AA** color contrast and accessibility benchmarks
