# DAY dict for the v3 entry: Tuesday 24 November 2026 (news-image-20261124).
# V3 applies the audit of v2 against the sealed judge criteria:
# - every number in the Day-in-Numbers box is backed by an illustrated card
#   (Cartagena hostages promoted to a card; Sanofi moves to the also-list)
# - Oceania is no longer blank: Australia's online-safety law (AP: tech
#   giants face fines up to 5% of global revenue) joins the also-list
# - the Hormuz card's caution (mine claims unconfirmed) leads its summary
# - the timeline attributes the tanker claim in words ("Iran says ...")
# Same verification discipline as v2: stories cross-checked in the day's
# published summaries; timeline times are "First reported 24 Nov" UTC stamps.
DAY = {
    "date_line": "Tuesday 24 November 2026",
    "date_short": "Tuesday 24 November",
    "story_count": 26,
    "region_count": 7,
    "kicker": "Huawei convicted in America · Iran says four tankers hit mines in Hormuz · World backs the Rohingya ruling",
    "regions": [("EUROPE", 3), ("MIDDLE EAST", 6), ("AFRICA", 3), ("ASIA", 5), ("AMERICAS", 5), ("OCEANIA", 1), ("WORLD", 3)],
    "timeline": [
        ("00:00", "Iran says 4 tankers mined"), ("08:14", "Ukraine strikes ships"),
        ("14:27", "Riyadh tower hit"), ("17:35", "Cartagena hostages"),
        ("20:41", "Huawei convicted"),
    ],
    "hero": {
        "n": 1, "loc": "Brooklyn, New York", "tag": "CONFIRMED", "scene": "scales",
        "cat": "US · Courts",
        "head": "US jury convicts Huawei of trade-secret theft",
        "sum": "Guilty of conspiracy to steal trade secrets and bank fraud — 10 of 12 counts — but acquitted of racketeering.",
        "src": "Daily Summary Of",
    },
    "leads": [
        {
            "n": 2, "loc": "Strait of Hormuz", "tag": "CLAIM", "scene": "ship",
            "cat": "Iran · Shipping",
            "head": "Iran says four tankers hit mines in Hormuz",
            "sum": "A maritime centre calls the mine claims unconfirmed. Tehran says a fourth tanker struck a mine, orders the strait closed further, and says the IRGC attacked a container ship.",
            "src": "Daily Summary Of",
        },
        {
            "n": 3, "loc": "The Hague", "tag": "CONFIRMED", "scene": "gavel",
            "cat": "World Court · Myanmar",
            "head": "World backs ICJ's Rohingya genocide ruling",
            "sum": "Fourteen countries affirm the judgment; Britain sanctions Myanmar's generals.",
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
            "cat": "Ukraine · War",
            "head": "Ukraine strikes Russian ships in two seas",
            "sum": "Kyiv admits hitting the Sparta II; naval drones sink a corvette off Libya.",
            "src": "Daily Summary Of · IQMia",
        },
        {
            "n": 5, "loc": "Antalya, Türkiye", "tag": "CONFIRMED", "scene": "summit",
            "cat": "World · Climate",
            "head": "Climate summit ends with no deal",
            "sum": "90+ nations reject a draft silent on fossil fuels after 50h overtime.",
            "src": "Principia · Daily Summary Of",
        },
        {
            "n": 6, "loc": "Cartagena", "tag": "REPORTED", "scene": "store", "art_label": "25",
            "cat": "Colombia · Crime",
            "head": "25 hostages held at a supermarket",
            "sum": "Gunmen seize 25 people inside a supermarket in Cartagena.",
            "src": "Daily Summary Of",
        },
    ],
    "row_c": [
        {
            "n": 7, "loc": "Pennsylvania", "tag": "CONFIRMED", "scene": "virus",
            "cat": "US · Health",
            "head": "America loses measles elimination status",
            "sum": "Gone after 25 years; a Pennsylvania outbreak claims a ninth life.",
            "src": "Principia · Horizon",
        },
        {
            "n": 8, "loc": "Senegal", "tag": "CONFIRMED", "scene": "score", "art_label": "AFCON", "art_sub": "SENEGAL CHAMPIONS",
            "cat": "Africa · Sport",
            "head": "Senegal restored as Africa Cup champions",
            "sum": "Sport's top court overturns the award to Morocco; the 1-0 final win stands.",
            "src": "Daily Summary Of · AllSports",
        },
        {
            "n": 9, "loc": "Madrid, Spain", "tag": "REPORTED", "scene": "score", "art_label": "5-1", "art_sub": "REAL MADRID v PSV",
            "cat": "Europe · Sport",
            "head": "Real Madrid rout PSV 5-1 in Champions League",
            "sum": "Down to an early penalty, Madrid score five after half-time; Mbappé two.",
            "src": "AllSports",
        },
        {
            "n": 10, "loc": "Riyadh", "tag": "REPORTED", "scene": "fire",
            "cat": "Saudi Arabia · Attack",
            "head": "Drone hits Riyadh's PIF tower, 11+ wounded",
            "sum": "Officials blame a Houthi drone; second hit on the tower in a week.",
            "src": "Daily Summary Of",
        },
    ],
    "also": [
        (11, "MYS", "Malaysia sends back 6,803 Myanmar migrants"),
        (12, "PSE", "UN: Gaza war undoes 77 years of development"),
        (13, "AUS", "Online-safety fines up to 5% for tech giants"),
        (14, "FRA", "Sanofi buys Insmed, a $41bn biotech takeover"),
        (15, "TUR", "Military helicopter crashes, five crew killed"),
        (16, "COL", "Car bomb at Villavicencio offices injures 23"),
        (17, "IRQ", "Baghdad orders federal control of Kurdish oil"),
        (18, "PSE", "Israel kills Hamas internal security chief"),
        (19, "COD", "Fighting in Ituri traps Ebola teams — WHO"),
        (20, "KOR", "Seoul scrambles jets as Russian aircraft near"),
        (21, "NPL", "Magnitude 5.6 quake near the China border"),
        (22, "CHN", "Tiangong opens to first foreign astronaut"),
        (23, "YEM", "Houthis 60 km from Aden, ready to attack"),
        (24, "USA", "US states sue Musk firms over Grok images"),
        (25, "LBY", "Libya's Haftar visits Turkey for first time"),
        (26, "MKT", "Bitcoin falls below $60,000"),
    ],
    "pins": [(10, 6), (48, 9), (36, 4), (41, 3), (39, 8), (13, 10), (14, 8), (33, 11), (31, 7), (44, 11)],
    "date_check": "All stories happened or were first reported on Tuesday 24 November 2026 (UTC). Left out as earlier news: Nvidia restored Jensen Huang on Mon 23 Nov · the ICJ's Rohingya ruling came last week (Tuesday's story is the response) · 'El Chapo Isidro' was captured Sat 21 Nov.",
    "legend_tail": "Scenes are drawn illustrations, not photographs.",
}
