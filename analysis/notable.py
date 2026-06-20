def find_notable_events(timeline):

    ALERT_CATEGORIES = {

        "Cybersecurity Tools": [
            "nmap",
            "zenmap",
            "zmap",
            "angryip",
            "intelx",
            "metasploit",
            "mimikatz",
            "wireshark",
            "burpsuite",
            "sqlmap",
            "hydra",
            "john",
            "hashcat",
            "aircrack"
        ],

        "Weapons": [
            "gun",
            "firearm",
            "rifle",
            "pistol",
            "shotgun",
            "ammunition",
            "ammo"
        ],

        "Poison": [
            "poison",
            "cyanide",
            "arsenic",
            "ricin",
            "toxin"
        ],

        "Drugs": [
            "cocaine",
            "heroin",
            "methamphetamine",
            "meth",
            "ecstasy",
            "lsd"
        ],

        "Adult Content": [
            "porn",
            "pornhub",
            "xvideos",
            "xnxx",
            "adult video",
            "sex video"
        ],

        "Hacking Searches": [
            "hack",
            "hacking",
            "exploit",
            "payload",
            "privilege escalation",
            "reverse shell",
            "password cracking"
        ]
    }

    notable = []

    for event in timeline:

        target = str(
            event.get(
                "target",
                ""
            )
        ).lower()

        artifact = event.get(
            "artifact",
            ""
        )

        # Keyword matching
        for category, keywords in ALERT_CATEGORIES.items():

            for keyword in keywords:

                if keyword in target:

                    notable.append({

                        "reason":
                            f"{category} Keyword Match",

                        "event":
                            event

                    })

                    break

        # Executable Downloads

        if artifact == "Download":

            if (

                target.endswith(".exe")
                or target.endswith(".msi")
                or target.endswith(".bat")
                or target.endswith(".ps1")
                or target.endswith(".vbs")

            ):

                notable.append({

                    "reason":
                        "Executable Download",

                    "event":
                        event

                })

        # USB Activity

        if artifact == "USB":

            notable.append({

                "reason":
                    "USB Device Activity",

                "event":
                    event

            })

        # Recycle Bin Activity

        if artifact == "Recycle Bin":

            notable.append({

                "reason":
                    "Deleted File",

                "event":
                    event

            })

    return notable