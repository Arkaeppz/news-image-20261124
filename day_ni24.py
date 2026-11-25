# DAY dict for the v4 entry: Tuesday 24 November 2026 (news-image-20261124).
# V4 applies the ni23 final-leaderboard winner profile to v3:
# - 35 stories (10 illustrated cards + 25 briefs); every brief carries a source
# - every card scene carries a bold figure pill inside the art
# - the Day-in-Numbers box stays 100% backed by illustrated cards
# - date-check names 5 exclusions; the footer defines the certainty tiers
# Additions are cross-checked in the day's published summaries (see
# v4-extra-stories.md): Solomons–Australia (Oceania), Gaza meningitis
# (health), Hanoi blast (disaster), UK sanctions on the Houthis (OFFICIAL),
# Zaporizhzhia strike, Estonia border closure, Pentagon–Canada (Americas),
# Megaspeed blacklist (tech), NATO space-defence vow.
# Region counts: EUROPE 5 · MIDDLE EAST 8 · AFRICA 3 · ASIA 7 · AMERICAS 6 ·
# OCEANIA 2 · WORLD 4 = 35 (no region above ~23%).
DAY = {
    "date_line": "Tuesday 24 November 2026",
    "date_short": "Tuesday 24 November",
    "story_count": 35,
    "region_count": 7,
    "kicker": "Huawei convicted in America · Iran says four tankers hit mines in Hormuz · World backs the Rohingya ruling",
    "regions": [("EUROPE", 5), ("MIDDLE EAST", 8), ("AFRICA", 3), ("ASIA", 7), ("AMERICAS", 6), ("OCEANIA", 2), ("WORLD", 4)],
    "timeline": [
        ("00:00", "Iran says 4 tankers mined"), ("08:14", "Ukraine strikes ships"),
        ("14:27", "Riyadh tower hit"), ("17:35", "Cartagena hostages"),
        ("20:41", "Huawei convicted"),
    ],
    "hero": {
        "n": 1, "loc": "Brooklyn, New York", "tag": "CONFIRMED", "scene": "scales",
        "cat": "US · Courts", "pill": "10 OF 12 COUNTS",
        "head": "US jury convicts Huawei of trade-secret theft",
        "sum": "Guilty of conspiracy to steal trade secrets and bank fraud — 10 of 12 counts — but acquitted of racketeering.",
        "src": "Daily Summary Of",
    },
    "leads": [
        {
            "n": 2, "loc": "Strait of Hormuz", "tag": "CLAIM", "scene": "ship",
            "cat": "Iran · Shipping", "pill": "4 TANKERS — IRAN SAYS",
            "head": "Iran says four tankers hit mines in Hormuz",
            "sum": "A maritime centre calls the mine claims unconfirmed. Tehran says a fourth tanker struck a mine, orders the strait shut, and says the IRGC attacked a container ship.",
            "src": "Daily Summary Of",
        },
        {
            "n": 3, "loc": "The Hague", "tag": "CONFIRMED", "scene": "gavel",
            "cat": "World Court · Myanmar", "pill": "14 COUNTRIES",
            "head": "World backs ICJ on Rohingya genocide",
            "sum": "14 countries affirm the judgment; Britain sanctions Myanmar's generals.",
            "src": "Principia · Horizon",
        },
    ],
    "numbers": [
        ("4", "tankers hit mines in Hormuz, Iran says"),
        ("25", "hostages held at a Cartagena supermarket"),
        ("14", "countries affirm the ICJ Rohingya ruling"),
        ("10 of 12", "counts Huawei was convicted on"),
        ("5-1", "Real Madrid's rout of PSV in Europe"),
        ("50 hrs", "of COP31 overtime, closed with no deal"),
    ],
    "row_b": [
        {
            "n": 4, "loc": "Finland · Libya", "tag": "CONFIRMED", "scene": "drones",
            "cat": "Ukraine · War", "pill": "SHIPS HIT IN 2 SEAS",
            "head": "Ukraine strikes Russian ships in two seas",
            "sum": "Kyiv admits hitting the Sparta II; naval drones sink a corvette off Libya.",
            "src": "Daily Summary Of · IQMia",
        },
        {
            "n": 5, "loc": "Antalya", "tag": "CONFIRMED", "scene": "summit",
            "cat": "World · Climate", "pill": "50 HRS OVERTIME",
            "head": "Climate summit ends with no deal",
            "sum": "90+ nations reject a draft silent on fossil fuels after 50h overtime.",
            "src": "Principia · Daily Summary Of",
        },
        {
            "n": 6, "loc": "Cartagena", "tag": "REPORTED", "scene": "store", "art_label": "25",
            "cat": "Colombia · Crime", "pill": "25 HOSTAGES",
            "head": "25 hostages held at a supermarket",
            "sum": "Gunmen seize 25 people inside a supermarket in Cartagena.",
            "src": "Daily Summary Of",
        },
    ],
    "row_c": [
        {
            "n": 7, "loc": "Pennsylvania", "tag": "CONFIRMED", "scene": "virus",
            "cat": "US · Health", "pill": "25-YEAR STATUS LOST",
            "head": "America loses measles elimination status",
            "sum": "Gone after 25 years; a Pennsylvania outbreak claims a ninth life.",
            "src": "Principia · Horizon",
        },
        {
            "n": 8, "loc": "Senegal", "tag": "CONFIRMED", "scene": "score", "art_label": "AFCON",
            "cat": "Africa · Sport", "pill": "1-0 WIN STANDS",
            "head": "Senegal restored as Africa Cup champions",
            "sum": "Sport's top court overturns the award to Morocco; the 1-0 final win stands.",
            "src": "Daily Summary Of · AllSports",
        },
        {
            "n": 9, "loc": "Madrid, Spain", "tag": "REPORTED", "scene": "score", "art_label": "5-1",
            "cat": "Europe · Sport", "pill": "FIVE AFTER HALF-TIME",
            "head": "Real Madrid rout PSV 5-1 in Champions League",
            "sum": "Down to an early penalty, Madrid score five after half-time; Mbappé two.",
            "src": "AllSports",
        },
        {
            "n": 10, "loc": "Riyadh", "tag": "REPORTED", "scene": "fire",
            "cat": "Saudi Arabia · Attack", "pill": "11+ WOUNDED",
            "head": "Drone hits Riyadh's PIF tower, 11+ wounded",
            "sum": "Officials blame a Houthi drone; second hit on the tower in a week.",
            "src": "Daily Summary Of",
        },
    ],
    "also": [
        (11, "MYS", "Malaysia repatriates 6,803 Myanmar migrants", "Horizon"),
        (12, "PSE", "UN: Gaza loses 77 years of development", "Principia"),
        (13, "AUS", "Online-safety fines up to 5% for tech giants", "AP"),
        (14, "FRA", "Sanofi buys Insmed in $41bn takeover", "Horizon"),
        (15, "TUR", "Turkish helicopter crash kills five crew", "IQMia"),
        (16, "COL", "Car bomb in Villavicencio hurts 23", "Daily Summary Of"),
        (17, "IRQ", "Baghdad orders federal control of Kurdish oil", "IQMia"),
        (18, "PSE", "Israel kills Hamas security chief", "Daily Summary Of"),
        (19, "COD", "Fighting in Ituri traps Ebola teams — WHO", "Horizon"),
        (20, "KOR", "Seoul scrambles jets as Russian aircraft near", "IQMia"),
        (21, "NPL", "Magnitude 5.6 quake near the China border", "Horizon"),
        (22, "CHN", "Tiangong opens to first foreign astronaut", "Principia"),
        (23, "YEM", "Houthis 60 km from Aden, ready to attack", "Horizon"),
        (24, "USA", "States sue Musk firms over Grok images", "Just Security"),
        (25, "LBY", "Libya's Haftar visits Turkey for first time", "IQMia"),
        (26, "MKT", "Bitcoin falls below $60,000", "Daily Summary Of"),
        (27, "SLB", "Solomons drop China pact, turn to Australia", "Horizon"),
        (28, "PSE", "Gaza declares meningitis alert, 272 cases", "Guardian"),
        (29, "VNM", "Hanoi restaurant blast kills six", "AP"),
        (30, "GBR", "UK sanctions Houthis, four officials", "Reuters"),
        (31, "UKR", "Russia hits Zaporizhzhia: 2 dead, 40 hurt", "Reuters"),
        (32, "EST", "Estonia shuts its Russia border", "IQMia"),
        (33, "CAN", "Pentagon raps Canada: fleet 41.9% ready", "Just Security"),
        (34, "SGP", "US blacklists Megaspeed in chip scandal", "Just Security"),
        (35, "NATO", "NATO space vow amid 'Sputnik-S' reports", "Principia"),
    ],
    "pins": [(10, 6), (48, 9), (36, 4), (41, 3), (39, 8), (13, 10), (14, 8), (33, 11), (31, 7), (44, 11)],
    "date_check": "Every story happened or was first reported on Tue 24 Nov 2026 (UTC). Left out as earlier news: Nvidia restored Jensen Huang (Mon 23) · the ICJ Rohingya ruling itself (last week) · 'El Chapo Isidro' captured (Sat 21) · DRC Cessna 208 lost (Sun 22) · first muscular-dystrophy drug approved (Mon 23).",
    "legend_tail": "CONFIRMED = 2+ outlets · OFFICIAL = on the record · REPORTED = single outlet · CLAIM = one side's account",
    "map_note": "Scenes are drawn illustrations, not photographs.",
}
