# -*- coding: utf-8 -*-
import json
from pathlib import Path

ARTIST_NAME = "Max Musikmann"

path = Path(__file__).resolve().parent / "index.html"
text = path.read_text(encoding="utf-8")

schedule_intern = [
  {"date": "2026-08-23", "time": "09:30", "dateLabel": "So 23.08.", "cat": "ANKUNFT", "name": "Ankunft {{ARTIST}}", "detail": "Empfang durch Abendspielleitung", "place": "Eingang Süd", "people": "Grâce Andrianjatovo", "status": "BESTÄTIGT", "note": "GET IN_GET OUT · KBB Template v3", "type": "normal"},
  {"date": "2026-08-23", "time": "09:45", "dateLabel": "So 23.08.", "cat": "STIMMUNG", "name": "STIMMUNG 1 — Martin Hofer", "detail": "442 Hz · vor Probe", "place": "Bühne / Auditorium", "people": "Martin Hofer · +43 676 412 88 33", "status": "BESTÄTIGT", "note": "Steinway D · Nr. 578 234", "type": "piano"},
  {"date": "2026-08-23", "time": "10:00", "dateLabel": "So 23.08.", "cat": "LOGE", "name": "Einrichtung Loge · Catering Mittag", "detail": "Übergabe Getränke & Speisen", "place": "Loge B2", "people": "KBB / Catering", "status": "BESTÄTIGT", "note": "", "type": "normal"},
  {"date": "2026-08-23", "time": "10:15", "dateLabel": "So 23.08.", "cat": "PROBE", "name": "Türöffnung Bühne — Probe 1", "detail": "Freies Spielen", "place": "Auditorium — Bühne", "people": ARTIST_NAME, "status": "BESTÄTIGT", "note": "", "type": "rehearsal"},
  {"date": "2026-08-23", "time": "12:00", "dateLabel": "So 23.08.", "cat": "PAUSE", "name": "Mittagspause — Catering in der Loge", "detail": "", "place": "Loge B2", "people": "Catering", "status": "INFO", "note": "", "type": "normal"},
  {"date": "2026-08-23", "time": "13:45", "dateLabel": "So 23.08.", "cat": "STIMMUNG", "name": "STIMMUNG 2 — Martin Hofer", "detail": "442 Hz · vor Generalprobe", "place": "Bühne / Auditorium", "people": "Martin Hofer · Klavierstimmer", "status": "BESTÄTIGT", "note": "", "type": "piano"},
  {"date": "2026-08-23", "time": "14:00", "dateLabel": "So 23.08.", "cat": "PROBE", "name": "Generalprobe — Goldberg-Variationen komplett", "detail": "", "place": "Auditorium — Bühne", "people": ARTIST_NAME, "status": "BESTÄTIGT", "note": "Film: nur laut Freigabe 14:00–16:00", "type": "rehearsal"},
  {"date": "2026-08-23", "time": "16:00", "dateLabel": "So 23.08.", "cat": "RUHE", "name": "Ruhezeit Künstler", "detail": "Keine Störungen", "place": "Loge B2", "people": "—", "status": "INFO", "note": "", "type": "normal"},
  {"date": "2026-08-23", "time": "18:00", "dateLabel": "So 23.08.", "cat": "CATERING", "name": "Abendessen in der Loge", "detail": "", "place": "Loge B2", "people": "Catering", "status": "BESTÄTIGT", "note": "Lieferzeit laut Rider bis 18:00", "type": "normal"},
  {"date": "2026-08-23", "time": "18:30", "dateLabel": "So 23.08.", "cat": "STIMMUNG", "name": "STIMMUNG 3 — letzte Kontrolle vor Konzert", "detail": "Martin Hofer", "place": "Bühne / Auditorium", "people": "Klavierstimmer", "status": "BESTÄTIGT", "note": "", "type": "piano"},
  {"date": "2026-08-23", "time": "19:00", "dateLabel": "So 23.08.", "cat": "BACKSTAGE", "name": "Einkleiden", "detail": "Abendspielleitung anwesend", "place": "Backstage", "people": "Grâce Andrianjatovo", "status": "BESTÄTIGT", "note": "", "type": "normal"},
  {"date": "2026-08-23", "time": "19:20", "dateLabel": "So 23.08.", "cat": "EINLASS", "name": "Einlass Publikum", "detail": "", "place": "Auditorium", "people": "Publikumsdienst", "status": "BESTÄTIGT", "note": "", "type": "normal"},
  {"date": "2026-08-23", "time": "19:25", "dateLabel": "So 23.08.", "cat": "BACKSTAGE", "name": "Künstler bereit — Check-in ASL", "detail": "", "place": "Backstage", "people": "Grâce Andrianjatovo", "status": "BESTÄTIGT", "note": "", "type": "normal"},
  {"date": "2026-08-23", "time": "19:30", "dateLabel": "So 23.08.", "cat": "KONZERT", "name": "KONZERTBEGINN — Goldberg-Variationen BWV 988", "detail": "Récital de Piano", "place": "Bühne", "people": ARTIST_NAME, "status": "BESTÄTIGT", "note": "GFG-2026-047 · Notfall KBB +43 670 195 6166", "type": "concert"},
  {"date": "2026-08-23", "time": "20:45", "dateLabel": "So 23.08.", "cat": "PAUSE", "name": "Pause — 20 Minuten", "detail": "", "place": "Loge B2", "people": "—", "status": "INFO", "note": "", "type": "normal"},
  {"date": "2026-08-23", "time": "21:05", "dateLabel": "So 23.08.", "cat": "KONZERT", "name": "2. Programmteil", "detail": "", "place": "Bühne", "people": ARTIST_NAME, "status": "BESTÄTIGT", "note": "", "type": "concert"},
  {"date": "2026-08-23", "time": "21:35", "dateLabel": "So 23.08.", "cat": "KONZERT", "name": "Zugabe", "detail": "Geplant ca. 10–15 Min.", "place": "Bühne", "people": ARTIST_NAME, "status": "IN PLANUNG", "note": "", "type": "concert"},
  {"date": "2026-08-23", "time": "21:50", "dateLabel": "So 23.08.", "cat": "ENDE", "name": "Konzertende — kurze Ruhephase", "detail": "", "place": "Backstage", "people": "Grâce Andrianjatovo", "status": "INFO", "note": "", "type": "normal"},
  {"date": "2026-08-23", "time": "22:00", "dateLabel": "So 23.08.", "cat": "EMPFANG", "name": "Backstage-Empfang", "detail": "Auf Wunsch des Künstlers", "place": "Foyer / Backstage", "people": "KBB / Intendanz", "status": "IN PLANUNG", "note": "", "type": "normal"},
  {"date": "2026-08-23", "time": "22:30", "dateLabel": "So 23.08.", "cat": "GET-OUT", "name": "GET OUT — Abfahrt Hotel Krems", "detail": "Thomas Gruber", "place": "Eingang Süd", "people": "Grâce Andrianjatovo", "status": "BESTÄTIGT", "note": "Transfer laut LOGISTIK-Tab", "type": "normal"},
]

parking_intern = [
  {"who": "Solist — Transfer / Begleitung", "plate": "—", "zone": "Zone A – Künstler (VIP)", "when": "23.08.2026 · Tagesbetrieb", "note": "{{ARTIST}} · Fahrer: Thomas Gruber · +43 664 312 77 55"},
  {"who": "Klavierstimmer — PKW", "plate": "[Kennzeichen]", "zone": "Zone A – Künstler / Technik", "when": "23.08. · 09:30–19:45", "note": "Martin Hofer · 3× Stimmung"},
  {"who": "KBB / Abendspielleitung", "plate": "—", "zone": "Backstage / Eingang Süd", "when": "23.08. · ab 08:00", "note": "Grâce Andrianjatovo · Notfall KBB +43 670 195 6166"},
  {"who": "Aufnahme — Hausproduktion", "plate": "—", "zone": "FOH / Technik", "when": "23.08. · GP + Konzert", "note": "2 Personen · Ton laut Produktionstab"},
  {"who": "Lieferant — Catering", "plate": "[Kennzeichen]", "zone": "Zone C – Lieferanten", "when": "23.08. · Zeitfenster KBB", "note": "Mittag + Abend · Loge B2"},
]

start = text.find("/* Quelle: Grafenegg_ProductionPlan_v5.xlsx")
end = text.find("var SCHEDULE=SCHEDULE_ARTIST", start)
if start < 0 or end < 0:
    raise SystemExit("markers not found")

sched_js = json.dumps(schedule_intern, ensure_ascii=False, separators=(",", ":"))
park_js = json.dumps(parking_intern, ensure_ascii=False, separators=(",", ":"))

new_block = (
    "/* Quelle: KBB_Grafenegg_Produktionstemplate_v3 · PRODUCTION + GET IN_GET OUT · 23.08.2026 · {{ARTIST}} */\n"
    f"var SCHEDULE_INTERN = {sched_js};\n"
    f"var PARKING_INTERN={park_js};\n\n"
)

path.write_text(text[:start] + new_block + text[end:], encoding="utf-8")
print("patched OK")
