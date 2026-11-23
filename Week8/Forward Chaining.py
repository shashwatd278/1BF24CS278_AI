facts = {
    ("American", "Robert"),
    ("Missile", "M1"),
    ("Owns", "A", "M1"),
    ("Enemy", "A", "America")
}

def forward_chaining(facts, query):

    facts = set(facts)

    while True:
        new_facts = set()

        for f in facts:
            if f[0] == "Missile":
                new_facts.add(("Weapon", f[1]))

        for f in facts:
            if f == ("Enemy", "A", "America"):
                new_facts.add(("Hostile", "A"))

        for f in facts:
            if f[0] == "Owns" and f[1] == "A":
                missile = f[2]
                if ("Missile", missile) in facts:
                    new_facts.add(
                        ("Sells", "Robert", missile, "A")
                    )

        for american in facts:
            if american[0] == "American":
                person = american[1]

                for weapon in facts:
                    if weapon[0] == "Weapon":

                        for sale in facts:
                            if (sale[0] == "Sells"
                                and sale[1] == person
                                and sale[2] == weapon[1]):

                                nation = sale[3]

                                if ("Hostile", nation) in facts:
                                    new_facts.add(
                                        ("Criminal", person)
                                    )

        new_facts = new_facts - facts

        if not new_facts:
            break

        for f in new_facts:
            print("Derived:", f)

        facts.update(new_facts)

        if query in facts:
            print("\nQuery is PROVED")
            return True

    print("\nQuery cannot be proved")
    return False


print("Initial Knowledge Base:")
for fact in facts:
    print(fact)

query = ("Criminal", "Robert")

print("\nQuery:", query)
forward_chaining(facts, query)

