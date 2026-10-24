# Dansk teknisk sprog: sproglige valg og kilder

Denne reference forklarer de sproglige valg i [dansk-teknisk-sprog](../SKILL.md). Skillens proces, tilstande og outputformat er beskrevet i SKILL.md. Se [før/efter-eksemplerne](../examples/before-after.md) for konkrete omskrivninger.

Dette er ikke en officiel dansk oversættelse af ASD-STE100 eller en dansk standard. Det er en selvstændig vejledning til dansk teknisk kommunikation, inspireret af originalens præcisionsprincipper. Der findes ingen godkendt dansk ordliste i denne skill.

## Tre forskellige grundlag

| Grundlag | Hvad det omfatter her | Hvad det ikke betyder |
|---|---|---|
| Dansk retskrivning | Sammenskrivning og bindestreg i sammensætninger, forklaret på sproget.dk [1]. | At engelske skrivemåder automatisk er korrekte i dansk løbetekst. |
| Klarsprogsråd | Sætningsbygning, aktiv og passiv, handlingsnavneord og mindre kancellisprog [2]. | At alle passiver, lange sætninger eller handlingsnavneord er forkerte. |
| Projektets egne valg | Betydningsbevarelse, konsistent teknisk terminologi, handlingsopdeling og vejledende længdemål. | At disse valg er officielle danske retskrivningsregler eller krav fra de danske kilder. |

## Dansk retskrivning: sammensætninger

Danske sammensatte navneord skrives normalt i ét ord: *fejlmeddelelse*, *sikkerhedskopi* og *brugerprofil*. Engelske mellemrum kan derfor ikke overføres direkte til dansk. Sammensætninger med forkortelser, tal eller symboler kræver typisk bindestreg, eksempelvis *API-nøgle* [1].

En lang sammensætning kan være korrekt stavet og stadig være tung at læse. En forklarende formulering kan da være bedre end både et langt ord og en forkert opsplitning. Valget afhænger af betydningen og af, om ordet er en fast fagterm.

Retskrivning i løbetekst er ikke en begrundelse for at ændre tekniske navne. Et feltnavn som `api_key`, en kommando eller en knap med navnet **Save** gengives nøjagtigt. Denne skelnen er et projektvalg om teknisk præcision.

## Klarsprogsråd: sætningsbygning og forvægt

En sætning bliver ofte lettere at læse, når hovedudsagnet står tidligt, og afstanden mellem aktør og handling er kort. Tunge indskud og lange kæder af forbehold kan skjule det centrale budskab. Håndbogen anbefaler kortere, varierede sætninger og mindre forvægt [2, s. 12 og 29–35].

En *kancellisløjfe* placerer en tung beskrivelse foran navneordet: *den i konfigurationsfilen angivne adresse*. Formen *den adresse, der er angivet i konfigurationsfilen* er ofte lettere at følge [2, s. 39].

En nødvendig betingelse kan med fordel stå før den handling, den gælder for. Mindre forvægt er ikke en grund til at flytte en sikkerhedsbetingelse så langt væk, at læseren overser den. Den prioritering er projektets anvendelse af klarsprogsrådene på tekniske instruktioner.

## Klarsprogsråd: aktiv, når aktøren er kendt

Aktiv form kan gøre ansvaret tydeligt: *Agenten kontrollerer filen* i stedet for *Filen kontrolleres af agenten*. Håndbogen anbefaler aktiv, når det er vigtigt, hvem der handler [2, s. 35–36].

Passiv er ikke en fejl i sig selv. Den kan være passende, når aktøren er ukendt eller uvigtig. *Logfilen blev slettet* siger ikke, hvem der slettede den. At ændre det til *Agenten slettede logfilen* ville tilføje en oplysning. Projektets krav om at bevare indholdet går derfor forud for ønsket om aktiv form.

## Klarsprogsråd: handlinger som verber

Formuleringer som *foretage en kontrol* og *udføre en beregning* kan ofte erstattes af *kontrollere* og *beregne*. Det gør handlingen mere direkte. Håndbogens råd retter sig mod unødvendig eller overdreven brug af handlingsnavneord, ikke mod alle navneord afledt af verber [2, s. 36–37].

Ord som *godkendelse*, *anmodning* og *konfiguration* kan betegne nødvendige tekniske begreber eller resultater. De skal ikke mekanisk fjernes. En omskrivning til et verbum er kun nyttig, hvis handling, aktør og betydning stadig er de samme.

## Projektvalg: præcision før korthed

De følgende hensyn er skillens egne valg til teknisk kommunikation, ikke retskrivningsregler:

- **Modalitet:** *Skal*, *bør*, *må*, *kan* og *må ikke* udtrykker forskellige forhold. Et krav må ikke blive en anbefaling, og en anbefaling må ikke blive en ordre. *Kan* kan udtrykke evne eller mulighed; sammenhængen afgør betydningen.
- **Usikkerhed:** *Kan have fejlet* er ikke det samme som *har fejlet*. Forbehold kan være en nødvendig oplysning om, hvad afsenderen ved.
- **Logik og afgrænsning:** Negation, *kun hvis*, undtagelser og ord som *mindst*, *højst* og *alle* er en del af indholdet. *Kun hvis* angiver en nødvendig betingelse; det lover ikke, at betingelsen alene er tilstrækkelig.
- **Tid og rækkefølge:** *Har gemt*, *gemte* og *gemmer* kan sige forskellige ting. *Før*, *efter*, *derefter* og *mens* må ikke forsvinde ved opdeling af sætninger.
- **Tal og tekniske tegn:** Værdier, enheder, grænser, versionsnumre, stier, kommandoer og identifikatorer bevares. Decimalpunkt i kode eller maskindata ændres ikke automatisk til decimalkomma.
- **Henvisninger:** Et navn er ofte tydeligere end *den*, *det* eller *ovenstående*. Navnet kan kun indsættes, når det faktisk fremgår, hvad henvisningen gælder.
- **Terminologi:** Samme begreb får samme betegnelse i dokumentet. Forskellige tekniske begreber slås ikke sammen, blot fordi ordene ligner hinanden. Nødvendige fagtermer bevares og forklares, når læseren har brug for det.
- **Handlinger og trin:** Én handling pr. trin gør en rækkefølge lettere at følge. Opdeling må ikke udviske en fælles betingelse eller skabe en rækkefølge, som kilden ikke angiver.

Projektets vejledende længdemål er højst 20 ord pr. instruktionssætning og 25 ord pr. forklarende sætning. De er lokale pejlemærker, ikke officielle danske grænser. Nødvendig præcision går altid forud for dem. Håndbogens råd om korte og varierede sætninger er et sprogligt udgangspunkt, ikke dokumentation for disse to projektgrænser [2, s. 12 og 29–35].

Tilstandene **Streng** og **Vejledende** ændrer ikke kravet om at bevare betydningen. Deres anvendelse er defineret i [SKILL.md](../SKILL.md).

## Engelske regler, der ikke overføres mekanisk

Denne skill behandler dansk som dansk, ikke som engelsk med danske ord:

- *Log ind* og *slå fra* kan være præcist og naturligt dansk. Engelske regler mod flerordsverber er ikke et dansk forbud.
- *Har gemt* kan være nødvendigt for at bevare tidsaspektet. Perfektum er ikke generelt forbudt.
- Et dansk ord behøver ikke låses til én ordklasse efter en engelsk ordliste.
- Engelske grænser for antallet af ord i navneordsklynger afgør ikke, hvordan danske sammensætninger skal skrives.
- Semikolon er ikke generelt forbudt som dansk retskrivningsregel i denne skill. Punktum kan være et bedre stilvalg, når det gør sammenhængen tydeligere.

Disse afgrænsninger er projektvalg. De er ikke en påstand om, at en bestemt dansk formulering altid er bedst.

## Kilder

1. **sproget.dk: [Et eller flere ord](https://sproget.dk/typiske-problemer/et-eller-flere-ord/).** Se især afsnittet *Sammensætninger skrives i ét ord* og omtalen af bindestreg ved forkortelser, tal og symboler. Kilden forklarer retskrivningen, herunder forskellen på danske sammensætninger og engelske låneord.
2. **Pia Jarvad og Jørgen Schack: [Håndbog i klarsprog for ansatte hos Folketingets Ombudsmand](https://dsn.dk/wp-content/uploads/2021/01/Haandbog-i-klarsprog.pdf), 2008.** Appendiks om grammatisk komma er tilføjet i 2012. Henvisningerne bruger bogens trykte sidetal: s. 12 om sætningslængde og forvægt, s. 29–35 om sætningsbygning, s. 35–36 om aktiv og legitim passiv, s. 36–37 om handlingsnavneord og s. 39 om kancellisløjfer. Håndbogen er skrevet til ombudsmandens ansatte; dens råd bruges her som inspiration, ikke som universelle lovkrav.

Eksemplerne i denne skill er projektets egne illustrationer, ikke citater fra kilderne. Ingen af kilderne dokumenterer en officiel dansk ASD-STE100-standard eller en godkendt dansk teknisk ordliste.
