# Sitemap

## Project Assessment
An internal-facing computer-vision dashboard that orchestrates two camera feeds, user registration (capture 5 images), model training, and live detection. The scope is a small multi-view app: a primary live monitoring dashboard plus focused flows for registration and identity management.

## Page Inventory

### Live Monitoring Dashboard
- **URL:** /
- **Purpose:** View both camera feeds, live detections, and system status in real time.
- **Key Sections:**
  1. Dual Camera Live Feeds — inbuilt + external webcam with overlays.
  2. Detection Stream — recent detections with assigned IDs and confidence.
  3. Model Status — current model version, training state, FPS, device health.
  4. Quick Actions — start/stop capture, trigger training, open registration.

### Registration & Capture
- **URL:** /register
- **Purpose:** Register a new person and capture 5 images for training.
- **Key Sections:**
  1. Registration Form — name/label + optional metadata.
  2. Capture Progress — 5-shot counter with thumbnails.
  3. Camera Selector — choose inbuilt/external for capture.
  4. Submission & Validation — save and queue for training.

### People & Identity Management
- **URL:** /people
- **Purpose:** View registered people and anonymous IDs across feeds.
- **Key Sections:**
  1. Registered People List — name, last seen, sample images.
  2. Anonymous IDs — randomly assigned IDs, cross-camera linkage.
  3. Merge / Promote Actions — convert anonymous to registered.

### Training & Model Control
- **URL:** /training
- **Purpose:** Manage training runs and model lifecycle.
- **Key Sections:**
  1. Training Queue — pending/active jobs.
  2. Metrics — loss, accuracy, epoch progress.
  3. Model Versions — deploy/rollback actions.

## URL Map

| Page | URL | Purpose |
|------|-----|---------|
| Live Monitoring Dashboard | / | Real-time feeds + detections + system status |
| Registration & Capture | /register | Capture 5 images for new person |
| People & Identity Management | /people | Manage registered and anonymous IDs |
| Training & Model Control | /training | Run and monitor model training |

## Primary User Flow
1. Operator opens the Live Monitoring Dashboard to view both feeds and detections.
2. When a new person needs registration, they navigate to Registration & Capture.
3. Capture 5 images, submit, and queue training.
4. Monitor training status and deploy the new model.
5. Return to the Dashboard to verify live detection accuracy.

## Navigation
Primary navigation is a left sidebar with links to Dashboard, Register, People, and Training. A compact header houses global status, camera health, and quick actions.