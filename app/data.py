from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from random import Random
from typing import List


rng = Random(42)


@dataclass
class DetectionEvent:
    label: str
    feed: str
    confidence: float
    seen_at: str
    status: str


@dataclass
class PersonRecord:
    name: str
    person_id: str
    last_seen: str
    confidence: float
    samples: int


@dataclass
class AnonymousTrack:
    anon_id: str
    last_seen: str
    feeds: str
    linked_to: str | None = None


@dataclass
class TrainingRun:
    run_id: str
    dataset: str
    status: str
    epoch: int
    total_epochs: int
    loss: float
    accuracy: float
    eta: str


@dataclass
class AppState:
    active_feeds: int
    detected_ids: int
    model_version: str
    queue_size: int
    capture_progress: int
    capture_target: int
    detections: List[DetectionEvent] = field(default_factory=list)
    people: List[PersonRecord] = field(default_factory=list)
    anonymous: List[AnonymousTrack] = field(default_factory=list)
    training: TrainingRun | None = None

    @classmethod
    def sample(cls) -> "AppState":
        now = datetime.utcnow()
        return cls(
            active_feeds=2,
            detected_ids=17,
            model_version="YOLOv8n-3.1",
            queue_size=1,
            capture_progress=3,
            capture_target=5,
            detections=[
                DetectionEvent("Priya Sharma", "Inbuilt Camera", 98.1, cls._ago(now, 2), "registered"),
                DetectionEvent("Anon 7F3A", "External Webcam", 71.6, cls._ago(now, 6), "anonymous"),
                DetectionEvent("Mateo Ruiz", "Inbuilt Camera", 95.4, cls._ago(now, 12), "registered"),
            ],
            people=[
                PersonRecord("Priya Sharma", "ID 204", cls._ago(now, 2), 98.1, 5),
                PersonRecord("Mateo Ruiz", "ID 118", cls._ago(now, 12), 95.4, 5),
                PersonRecord("Aisha Johnson", "ID 061", cls._ago(now, 36), 93.8, 5),
            ],
            anonymous=[
                AnonymousTrack("Anon 7F3A", cls._ago(now, 6), "External Webcam"),
                AnonymousTrack("Anon 91C2", cls._ago(now, 18), "Inbuilt Camera"),
                AnonymousTrack("Anon 55B9", cls._ago(now, 60), "External Webcam"),
            ],
            training=TrainingRun("Run 18C7", "Capture Set 09", "running", 7, 20, 0.62, 91.4, "12m"),
        )

    @staticmethod
    def _ago(now: datetime, minutes: int) -> str:
        delta = now - timedelta(minutes=minutes)
        return delta.strftime("%I:%M %p")
