# Humanizer på dansk

Den danske udgave er en selvstændig skill med navnet `humanizer-da`. Hele vejledningen og alle eksempler er på dansk. Den har 26 mønstre og bevarer tekstens oplysninger, usikkerhed og stemme.

- [Den danske skill](SKILL.md), version 1.0.0
- [Udgivelsesnoter](CHANGELOG.md)
- [Licens](LICENSE)

Mappen indeholder hele den danske udgave. Den har ingen lokale afhængigheder til den engelske Humanizer.

## Installation

Alle nødvendige filer ligger i denne mappe. Installationen kræver ikke den engelske udgave.

1. Find mappen, hvor din agent læser skills. Du kan bruge en global mappe eller en mappe til det aktuelle projekt.
2. Kopier hele mappen `humanizer-da` ind i denne mappe. Bevar en eventuel engelsk `humanizer`-mappe.
3. Genindlæs agentens skills, hvis agenten kræver det.

Resultatet skal være:

```text
<din-skills-mappe>/humanizer-da/SKILL.md
```

`<din-skills-mappe>` er din agents mappe til skills, ikke en mappe med det bogstavelige navn. Du skal hverken omdøbe filer eller kopiere noget fra den engelske udgave.

## Brug

Hvis agenten understøtter direkte skill-kommandoer:

```text
/humanizer-da

Gør denne tekst mere naturlig. Bevar oplysningerne og graden af usikkerhed:
[indsæt dansk tekst]
```

Du kan også skrive:

```text
Brug humanizer-da til at omskrive denne tekst:
[indsæt dansk tekst]
```

Du får som standard kun den færdige omskrivning. Bed om et udkast og en kort kritik, hvis du vil se dem.

Ved filredigering gemmes kun den færdige prosa. Kode, kommandoer, stier, data, frontmatter og linkmål bevares. Giv gerne en prøve på din egen skrivestil.

## Eksempel

**Før:**
> Selvfølgelig! Lad os dykke ned i vores banebrydende opdatering. Fra 1. november 2026 kan to personer redigere samme dokument samtidig. Det er ikke bare en funktion, men en helt ny måde at samarbejde på. Funktionen er gratis på alle abonnementer. Håber det hjælper!

**Efter:**
> Fra 1. november 2026 kan to personer redigere samme dokument samtidig. Funktionen er gratis på alle abonnementer.

## Danske sprogregler

Vejledningen tager højde for sammensatte ord, nødvendige bindestreger som i `AI-værktøj` og `e-mail`, naturlig passiv, kommapraksis og danske anførselstegn. Den forbyder ikke almindelige ord eller enkelte tankestreger. Egennavne og præcise fagudtryk bevares.

Den danske udgave er redigeringshjælp, ikke en AI-detektor. Den bygger på [Wikipedias tegn på AI-sprog](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), tilpasset til dansk.
