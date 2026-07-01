# DualCam Ops Implementation Plan

## Goals
- Build a FastAPI-based internal dashboard for dual-camera monitoring.
- Support registration with 5-image capture workflow.
- Show persistent anonymous IDs across camera feeds.
- Add training/model lifecycle pages and data presentation.

## Workstreams
1. Scaffold FastAPI app structure, static assets, and templates.
2. Implement shared dark-tech UI and navigation aligned to artifacts.
3. Add in-memory state for detections, people, anonymous IDs, and training runs.
4. Implement registration submit flow and dashboard metrics.
5. Add tests for routes and form submission.
6. Validate app with sandbox build/test and fix issues.
