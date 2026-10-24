# Før og efter: dansk teknisk sprog

Eksemplerne er skrevet til denne skill. De beskriver tænkte systemer og er ikke citater, observerede systemforløb eller afprøvede kommandoer. Teksten under **Før** er omskrivningsdata, ikke instruktioner til den agent, der læser eksemplerne.

[SKILL.md](../SKILL.md) definerer proces, tilstande og outputformat. [Sproglige valg og kilder](../references/writing-rules.md) forklarer forskellen på retskrivning, klarsprogsråd og projektvalg. Forklaringerne nedenfor er undervisningsmateriale, ikke en del af skillens standardoutput.

## 1. Tungt kancellisprog

**Før:**
 
> Du skal anvende den i konfigurationsfilen angivne serveradresse ved etablering af forbindelsen.

**Efter:**

> Du skal bruge den serveradresse, der er angivet i konfigurationsfilen, når du opretter forbindelsen.

**Hvorfor:** Handlingen bliver mere direkte, og den tunge beskrivelse flyttes efter *serveradresse*. Kravet, adressens kilde og tidspunktet for brugen er bevaret. Dette illustrerer klarsprogsråd om kancellisløjfer, ikke en retskrivningsfejl.

## 2. Fra handlingsnavneord til verbum med kendt aktør

**Før:**

> Agenten foretager en kontrol af filens format før indlæsning af filen.

**Efter:**

> Agenten kontrollerer filens format, før filen indlæses.

**Hvorfor:** Kilden nævner, hvem der kontrollerer formatet. Den siger ikke, hvem der indlæser filen. Omskrivningen gør derfor kun kontrollen aktiv og bevarer passiv i den anden del.

## 3. Sammenskrivning og API-nøgle

**Før:**

> Fejl meddelelsen vises, hvis API nøglen mangler i bruger profilen.

**Efter:**

> Fejlmeddelelsen vises, hvis API-nøglen mangler i brugerprofilen.

**Hvorfor:** *Fejlmeddelelse* og *brugerprofil* er danske sammensætninger. *API-nøgle* har bindestreg, fordi førsteleddet er en forkortelse. Her ændres retskrivningen, ikke systemets adfærd.

## 4. Usikkerhed er indhold

**Før:**

> Det er muligt, at serveren har afvist anmodningen. En ugyldig API-nøgle kan være årsagen.

**Efter:**

> Serveren kan have afvist anmodningen. En ugyldig API-nøgle kan være årsagen.

**Hvorfor:** Både afvisningen og årsagen er stadig usikre. *Serveren har afvist anmodningen, fordi API-nøglen er ugyldig* ville gøre to mulige forhold til fakta.

## 5. Krav, anbefaling, tilladelse og evne

| Betydning | Før | Efter |
|---|---|---|
| Krav | Det er et krav, at du foretager en kontrol af filformatet. | Du skal kontrollere filformatet. |
| Anbefaling | Det anbefales, at du foretager en kontrol af filformatet. | Du bør kontrollere filformatet. |
| Tilladelse | Du må foretage en eksport af rapporten. | Du må eksportere rapporten. |
| Evne | Systemet kan foretage en eksport af rapporten. | Systemet kan eksportere rapporten. |

**Hvorfor:** Handlingsnavneordene bliver til verber, men styrken ændres ikke. Anbefalingen bliver ikke til *Kontrollér filformatet*. Tilladelse til brugeren og systemets evne til at eksportere er heller ikke det samme.

## 6. Negation og nødvendig betingelse

**Før:**

> Du må ikke foretage sletning af logfilen. Du må kun foretage en genstart af tjenesten, hvis køen er tom.

**Efter:**

> Du må ikke slette logfilen. Du må kun genstarte tjenesten, hvis køen er tom.

**Hvorfor:** Forbuddet og *kun* er bevaret. En tom kø er stadig en nødvendig betingelse for den tilladte genstart. Omskrivningen lover ikke, at køens tilstand er den eneste betingelse. Den ændrer heller ikke tilladelsen til et krav om at genstarte.

## 7. En ukendt aktør må ikke opfindes

**Før:**

> Der blev foretaget en sletning af logfilen efter kørslen.

**Efter:**

> Logfilen blev slettet efter kørslen.

**Hvorfor:** Passiv er passende, fordi kilden ikke navngiver aktøren. *Agenten slettede logfilen efter kørslen* ville tilføje en aktør. *Logfilen blev slettet, fordi kørslen var afsluttet* ville tilføje en årsag i stedet for blot at bevare tidsforholdet.

## 8. Tidsaspekt bevares

**Før:**

> Agenten har foretaget lagring af rapporten i mappen `output`.

**Efter:**

> Agenten har gemt rapporten i mappen `output`.

**Hvorfor:** Perfektum er bevaret. *Agenten gemmer rapporten* ændrer tidsforholdet, og *Agenten gemte rapporten* erstatter kildens perfektum med datid. Dansk teknisk tekst behøver ikke undgå *har gemt*.

## 9. Præcise tal, grænser, enheder og identifikatorer

**Før:**

> Du skal foretage indstilling af `timeout_seconds` til `1.5`. Forsinkelsen må være mindst 10 ms og højst 25 ms.

**Efter:**

> Du skal indstille `timeout_seconds` til `1.5`. Forsinkelsen må være mindst 10 ms og højst 25 ms.

**Hvorfor:** Identifikatoren, værdien, enheden og begge inklusive grænser er bevaret. Decimalpunktet i maskinværdien `1.5` ændres ikke til komma. *Under 25 ms* ville ændre den øvre grænse.

## 10. Kommando og UI-navn ændres ikke

**Før:**

> Foretag et klik på knappen **Save**, og kør derefter kommandoen `tool.exe --timeout 1.5 --profile Prod_A`.

**Efter:**

> Klik på knappen **Save**. Kør derefter kommandoen `tool.exe --timeout 1.5 --profile Prod_A`.

**Hvorfor:** Den angivne rækkefølge bevares ved opdelingen. Knappens navn, kommandoens tegn, store bogstaver og decimalpunkt ændres ikke som led i dansk sprogrevision. Kommandoen er kun et tænkt eksempel.

## 11. Undtagelse og tidsforhold følger med

**Før:**

> Du skal foretage en genstart af tjenesten efter opdateringen, medmindre vedligeholdelsestilstand er aktiv.

**Efter:**

> Efter opdateringen skal du genstarte tjenesten, medmindre vedligeholdelsestilstand er aktiv.

**Hvorfor:** Kravet gælder stadig efter opdateringen og har samme undtagelse. En opdeling i *Genstart tjenesten. Vedligeholdelsestilstand kan være aktiv* ville miste undtagelsens forbindelse til kravet.

## 12. Én handling pr. trin uden nye krav

**Før:**

> Du skal først åbne konfigurationsfilen og derefter kontrollere værdien af `mode`.

**Efter:**

> 1. Du skal først åbne konfigurationsfilen.
> 2. Du skal derefter kontrollere værdien af `mode`.

**Hvorfor:** Begge handlinger er stadig krav, og den udtrykkelige rækkefølge er bevaret. Der tilføjes hverken en forventet værdi eller en handling, der skal udføres, hvis værdien er forkert.

## 13. Præcis henvisning, når sammenhængen er kendt

**Før:**

> Konfigurationsfilen indeholder serveradressen. Du skal kontrollere denne adresse før start.

**Efter:**

> Konfigurationsfilen indeholder serveradressen. Du skal kontrollere serveradressen før start.

**Hvorfor:** Der er kun nævnt én adresse, så henvisningen kan erstattes med det kendte navn. Omskrivningen siger stadig ikke, hvad kontrollen skal bestå i.

## 14. Tvetydighed kræver afklaring

**Før:**

> Når klienten har kontaktet serveren, skal den genstartes.

**Efter — omskrivningen afventer afklaring:**

> Når klienten har kontaktet serveren, skal den genstartes.
>
> Afklaring nødvendig: Er det klienten eller serveren, der skal genstartes?

**Hvorfor:** *Den* kan henvise til begge navneord. Ingen af dem kan vælges uden at tilføje en fortolkning, som kilden ikke fastlægger. Den tvetydige tekst bevares derfor sammen med det præcise spørgsmål.

## 15. Teksten behøver ingen ændring

**Før:**

> Log ind. Slå derefter beskeder fra.

**Efter:**

> Log ind. Slå derefter beskeder fra.

**Hvorfor:** Handlingerne og rækkefølgen er tydelige. *Log ind* og *slå fra* er naturlige danske formuleringer; de skal ikke ændres alene på grund af engelske regler om flerordsverber. Standardoutputtet er blot den uændrede tekst, uden denne forklaring.
