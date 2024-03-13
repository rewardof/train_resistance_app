class CONSTANTS:

    class VAGON_TYPE:
        KR = 'kr'
        PR = 'pr'
        PL = 'pl'
        SYS = 'sys'
        XP = 'xp'
        PV = 'pv'
        RF = 'rf'

        CHOICES = (
            (KR, KR),
            (PR, PR),
            (PL, PL),
            (SYS, SYS),
            (XP, XP),
            (PV, PV),
            (RF, RF),
        )

    class ROAD_TYPE:
        MAIN = 'main'
        SORTING_ROAD = 'sorting_road'

        CHOICES = (
            (MAIN, MAIN),
            (SORTING_ROAD, SORTING_ROAD),
        )
