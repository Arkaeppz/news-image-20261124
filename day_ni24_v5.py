# DAY dict for the v5 entry: Tuesday 24 November 2026 (news-image-20261124).
# V5 = v4 + the round-3 leader evaluation (ni24-r3-leader-eval.md):
# - DATE PURITY: the COP31 card and the Ukraine-ships/corvette card are OUT;
#   both are now named in the date-check as Sun 22 Nov exclusions, with the
#   EU 22nd-sanctions proposal (Mon 23) noted among the same earlier-news set.
# - SELECTION: the day's signature stories the leaders all carry are in —
#   Chen Jining probe (lead), Sanofi $41bn (card), Zaporizhzhia raid (card),
#   Ariane 6 (card), England heat deaths (card), Dow 50,018 + Kospi/Taiex
#   (numbers + brief); Riyadh promoted, Rohingya demoted to a brief on its
#   24 Nov hook (affirmations + UK sanctions, not the ruling itself).
# - 38 stories: 12 illustrated cards + 26 briefs; every brief carries a
#   certainty tier (tier field: C/O/R/CL) and a source; card sources are
#   relabelled to the attributed wires where the day's record names them
#   (leader pages + v4-extra-stories.md), never invented.
# - Regions split to 10 buckets; masthead states 16 fields (counted from the
#   per-story field tags in the build notes).
# Region counts: EUROPE 6 · MIDDLE EAST 8 · AFRICA 4 · E ASIA 3 · S ASIA 1 ·
# SE ASIA 4 · N AMERICA 4 · LAT AMERICA 2 · OCEANIA 2 · WORLD 4 = 38.
DAY = {
    "date_line": "Tuesday 24 November 2026",
    "date_short": "Tuesday 24 November",
    "story_count": 38,
    "region_count": 10,
    "field_count": 16,
    "kicker": "Huawei convicted in America · China probes Shanghai's party chief · Sanofi buys Insmed for $41bn",
    "regions": [("EUROPE", 6), ("MIDDLE EAST", 8), ("AFRICA", 4), ("E ASIA", 3), ("S ASIA", 1), ("SE ASIA", 4), ("N AMERICA", 4), ("LAT AMERICA", 2), ("OCEANIA", 2), ("WORLD", 4)],
    "timeline": [
        ("00:00", "Mine claim"), ("05:30", "Sanofi $41bn"), ("11:14", "Ariane 6"),
        ("14:27", "Riyadh hit"), ("17:35", "Hostages"), ("20:41", "Huawei guilty"),
        ("21:00", "Dow 50,018"),
    ],
    "hero": {
        "n": 1, "loc": "Brooklyn, New York", "tag": "CONFIRMED", "scene": "scales",
        "cat": "US · Courts", "pill": "10 OF 12 COUNTS",
        "head": "US jury convicts Huawei of trade-secret theft",
        "sum": "Guilty of conspiracy to steal trade secrets and bank fraud — 10 of 12 counts — but acquitted of racketeering.",
        "src": "AP · CNN",
    },
    "leads": [
        {
            "n": 2, "loc": "Shanghai", "tag": "OFFICIAL", "scene": "gavel",
            "cat": "China · Politics", "pill": "UNDER INVESTIGATION",
            "head": "China probes Shanghai's party chief",
            "sum": "Politburo member Chen Jining, 62, is under investigation for 'serious violations', state media say.",
            "src": "Xinhua",
        },
    ],
    "numbers": [
        ("50,018", "Dow's first close above 50,000"),
        ("$41bn", "Sanofi pays cash for Insmed"),
        ("5,258", "heat deaths in England, a record"),
        ("25", "hostages held in a Cartagena store"),
        ("10 of 12", "counts Huawei was convicted on"),
        ("+8.99%", "Taiwan stocks' record surge"),
    ],
    "row_b": [
        {
            "n": 3, "loc": "Iran", "tag": "CLAIM", "scene": "ship",
            "cat": "Hormuz · Shipping", "pill": "4 TANKERS — IRAN SAYS",
            "head": "Ships hit in Hormuz; Iran claims mines",
            "sum": "UKMTO: crews safe; Iran says a 4th ship hit a mine.",
            "src": "UKMTO · Reuters",
        },
        {
            "n": 4, "loc": "Paris", "tag": "OFFICIAL", "scene": "health",
            "cat": "France · Pharma", "pill": "$41BN DEAL",
            "head": "Sanofi to buy Insmed for $41bn",
            "sum": "$175 a share in cash for the US lung-drug maker.",
            "src": "Sanofi",
        },
        {
            "n": 5, "loc": "Ukraine", "tag": "CONFIRMED", "scene": "drones",
            "cat": "Zaporizhzhia · War", "pill": "2 DEAD · 40 HURT",
            "head": "Russian raid kills 2 in Zaporizhzhia",
            "sum": "About 40 hurt, children among them, as flats are hit.",
            "src": "Reuters",
        },
        {
            "n": 6, "loc": "Riyadh", "tag": "CONFIRMED", "scene": "fire",
            "cat": "Saudi Arabia · Attack", "pill": "11 HURT",
            "head": "Drone hits Riyadh's PIF tower",
            "sum": "Second hit in a week; a Houthi drone is blamed.",
            "src": "Al Jazeera · AA",
        },
        {
            "n": 7, "loc": "Cartagena", "tag": "CONFIRMED", "scene": "store",
            "cat": "Colombia · Crime", "pill": "25 HOSTAGES",
            "head": "25 hostages held at a supermarket",
            "sum": "Gunmen seize 25 people in a Cartagena store.",
            "src": "Reuters",
        },
    ],
    "row_c": [
        {
            "n": 8, "loc": "USA", "tag": "CONFIRMED", "scene": "virus",
            "cat": "Pennsylvania · Health", "pill": "25-YEAR STATUS LOST",
            "head": "US loses measles elimination status",
            "sum": "Gone after 25 years; a ninth death in Pennsylvania.",
            "src": "Principia · Horizon",
        },
        {
            "n": 9, "loc": "Senegal", "tag": "OFFICIAL", "scene": "score", "art_label": "AFCON",
            "cat": "Africa · Sport", "pill": "1-0 WIN STANDS",
            "head": "Senegal restored as African champions",
            "sum": "Sport's top court voids CAF's award to Morocco.",
            "src": "CAS · AFP",
        },
        {
            "n": 10, "loc": "Madrid", "tag": "CONFIRMED", "scene": "score", "art_label": "5-1",
            "cat": "Europe · Sport", "pill": "FIVE AFTER HALF-TIME",
            "head": "Real Madrid rout PSV 5-1",
            "sum": "Five goals after half-time; Mbappé scores twice.",
            "src": "AllSports",
        },
        {
            "n": 11, "loc": "Kourou", "tag": "CONFIRMED", "scene": "rocket",
            "cat": "Europe · Space", "pill": "36 SATELLITES",
            "head": "Ariane 6 lofts 36 Amazon satellites",
            "sum": "Lift-off 11:14 UTC from French Guiana after a scrub.",
            "src": "AIAA · Xinhua",
        },
        {
            "n": 12, "loc": "England", "tag": "OFFICIAL", "scene": "sun",
            "cat": "Britain · Climate", "pill": "5,258 DEATHS",
            "head": "England's heat deaths hit a record",
            "sum": "UKHSA: 5,258 in summer 2026; old record 2,985.",
            "src": "UKHSA",
        },
    ],
    # briefs: (n, code, text, source, tier) — tier C = 2+ outlets,
    # O = on the record, R = single outlet, CL = one side's account.
    "also": [
        (13, "MYS", "Malaysia returns 6,803 Myanmar migrants", "Horizon", "R"),
        (14, "PSE", "UN: Gaza loses 77 years of development", "Principia", "O"),
        (15, "AUS", "Online-safety fines up to 5% for tech", "AP", "O"),
        (16, "TUR", "Turkish helicopter crash kills 5 crew", "Anadolu", "C"),
        (17, "COL", "Car bomb in Villavicencio hurts 23", "AP", "C"),
        (18, "IRQ", "Baghdad orders control of Kurdish oil", "The National", "O"),
        (19, "PSE", "Israel kills Hamas security chief", "Washington Post", "C"),
        (20, "COD", "Ituri fighting traps Ebola teams: WHO", "Horizon", "R"),
        (21, "KOR", "Seoul scrambles jets as Russians near", "Korea Herald", "C"),
        (22, "NPL", "M5.6 quake near the China border", "Horizon", "R"),
        (23, "CHN", "First foreign astronaut for Tiangong", "AP", "C"),
        (24, "YEM", "Houthis mass 60 km from Aden", "Horizon", "CL"),
        (25, "USA", "States sue Musk's firms over Grok", "Just Security", "R"),
        (26, "LBY", "Haftar visits Turkey for first time", "IQMia", "R"),
        (27, "MKT", "Bitcoin falls below $60,000", "Invezz", "C"),
        (28, "SLB", "Solomons to let China pact lapse", "SMH · ABC", "R"),
        (29, "PSE", "Gaza meningitis alert: 272 cases", "Guardian", "C"),
        (30, "VNM", "Hanoi restaurant blast kills six", "AP", "C"),
        (31, "GBR", "UK sanctions Houthis, four officials", "gov.uk", "O"),
        (32, "EST", "Estonia shuts its Russia border", "Politico Europe", "C"),
        (33, "CAN", "Pentagon raps Canada: fleet 41.9% ready", "AP", "O"),
        (34, "SGP", "US blacklists Megaspeed in chip scandal", "Politico", "O"),
        (35, "NATO", "NATO space vow amid 'Sputnik-S' reports", "BBC", "R"),
        (36, "MMR", "Rohingya: states affirm, UK sanctions", "Principia", "C"),
        (37, "SEN", "175 migrants missing on boat from Dakar", "Reuters", "R"),
        (38, "MKT", "Dow tops 50,000; Kospi, Taiex records", "ABC News", "C"),
    ],
    "pins": [(11, 5), (56, 9), (42, 8), (34, 4), (38, 4), (41, 8), (12, 11), (10, 6), (31, 9), (33, 5), (16, 10), (33, 3)],
    "date_check": "All stories happened or were first reported Tue 24 Nov 2026 (UTC). Left out as earlier news: COP31 collapse (Sun 22) · Libya corvette sinking (Sun 22) · Nvidia restores Huang (Mon 23) · ICJ Rohingya ruling itself (19 Nov) · 'El Chapo Isidro' captured (Sat 21) · first MD drug approved (Mon 23).",
    "legend_tail": "CONFIRMED = 2+ outlets · OFFICIAL = on the record · REPORTED = single outlet · CLAIM = one side's account",
    "map_note": "Scenes are drawn illustrations, not photographs.",
}
