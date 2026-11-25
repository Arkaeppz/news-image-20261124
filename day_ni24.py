# DAY dict for the v2 entry: Tuesday 24 November 2026 (news-image-20261124).
# Starts from v1's 17 verified stories and adds 11 more cross-checked in the
# day's published summaries (Daily Summary Of's 30-story final edition,
# Principia, Horizon, Just Security's Early Edition, IQMia). Timeline times
# are Daily Summary Of's "First reported 24 Nov" UTC stamps — none invented.
# Tags: CONFIRMED = 2+ summaries, REPORTED = 1, CLAIM = one side's account,
# ONGOING = still unfolding. The Hormuz tanker story is tagged CLAIM and its
# headline attributed to Iran: the Joint Maritime Information Centre called
# the mine claims unconfirmed (a faithfulness fix vs v1's CONFIRMED).
DAY = {
    "date_line": "Tuesday 24 November 2026",
    "date_short": "Tuesday 24 November",
    "story_count": 28,
    "region_count": 6,
    "kicker": "Huawei convicted in America · Iran says four tankers hit mines in Hormuz · World backs the Rohingya ruling",
    "regions": [("EUROPE", 5), ("MIDDLE EAST", 6), ("AFRICA", 3), ("ASIA", 6), ("AMERICAS", 6), ("WORLD", 2)],
    "timeline": [
        ("00:00", "Iran: 4 tankers mined"), ("08:14", "Ukraine strikes ships"),
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
            "sum": "Tehran says a fourth tanker struck a mine and orders the strait closed further; the IRGC also attacked a container ship. A maritime centre calls the mine claims unconfirmed.",
            "src": "Daily Summary Of",
        },
        {
            "n": 3, "loc": "The Hague", "tag": "CONFIRMED", "scene": "gavel",
            "cat": "World Court · Myanmar",
            "head": "World backs ICJ ruling: genocide against Rohingya",
            "sum": "Fourteen countries affirm the judgment; Britain sanctions Myanmar's generals.",
            "src": "Principia · Horizon",
        },
    ],
    "numbers": [
        ("4", "tankers hit mines in Hormuz, Iran says"),
        ("6,803", "Myanmar nationals Malaysia will send back"),
        ("$41bn", "Sanofi's takeover of biotech firm Insmed"),
        ("25", "hostages seized at a Cartagena supermarket"),
        ("5-1", "Real Madrid's rout of PSV in Europe"),
        ("77 yrs", "of Gaza development the UN says is undone"),
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
            "n": 6, "loc": "Paris, France", "tag": "REPORTED", "scene": "health", "art_label": "$41bn",
            "cat": "France · Business",
            "head": "Sanofi buys Insmed for $41 billion",
            "sum": "The biggest biotech takeover in nearly three years.",
            "src": "Principia",
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
            "sum": "Down to an early penalty, Madrid score five after half-time; Mbappé nets two.",
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
        (11, "TUR", "Military helicopter crashes, five crew killed"),
        (12, "COL", "Car bomb at Villavicencio offices injures 23"),
        (13, "NPL", "Magnitude 5.6 quake near the China border"),
        (14, "CHN", "Tiangong opens to first foreign astronaut"),
        (15, "YEM", "Houthis 60 km from Aden, ready to attack"),
        (16, "USA", "US states sue Musk firms over Grok images"),
        (17, "MKT", "Bitcoin falls below $60,000"),
        (18, "COL", "Armed men hold 25 hostages at a supermarket"),
        (19, "MYS", "Malaysia to send back 6,803 Myanmar migrants"),
        (20, "PSE", "Israel kills Hamas internal security chief"),
        (21, "PSE", "UN: Gaza war undoes 77 years of development"),
        (22, "COD", "Fighting in Ituri traps Ebola teams — WHO"),
        (23, "KOR", "Seoul scrambles jets as Russian aircraft near"),
        (24, "IRQ", "Baghdad orders federal control of Kurdish oil"),
        (25, "LBY", "Libya's Haftar visits Turkey for first time"),
        (26, "BGD", "Ex-PM Hasina says she will return on 16 Dec"),
        (27, "USA", "FDA approves first limb-girdle dystrophy drug"),
        (28, "NATO", "NATO vows space defence over satellite reports"),
    ],
    "pins": [(10, 6), (48, 9), (36, 4), (41, 3), (39, 8), (33, 5), (14, 8), (33, 11), (31, 7), (44, 11)],
    "date_check": "All stories happened or were first reported on Tuesday 24 November 2026 (UTC). Left out as earlier news: Nvidia restored Jensen Huang on Mon 23 Nov · the ICJ's Rohingya ruling came last week (Tuesday's story is the response) · 'El Chapo Isidro' was captured Sat 21 Nov.",
    "legend_tail": "Scenes are drawn illustrations, not photographs.",
}
