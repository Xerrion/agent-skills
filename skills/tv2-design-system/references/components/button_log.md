# Button

[View in Figma](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=2827-29110)

## 2.1.2
**15.9.2026**

- red.525 → red.500
- Den rødeknap bruger nu red.500 og ikke red.525

## 2.1.1
**8.9.2026**

- On Image varianten har fået en disabled state
- Efter feedback fra Mike (PCS) har on-image knappen fået en disabled state.  Dette gør også komponentet nemmere at bruge i figma. Farverne peger på primitive, da vi ikke burger light/dark logik på on-image. Der er ikke brugt wcag kontrast tjekt, da vi ikke kender baggrundsfarven ved billeder.

## 2.1.0
**26.8.2026**

- Navneændringer
- Default er omdøbt til Medium (default)  For at tydeliggøre størrelseshierarkiet.
- Live og Play entry er samlet under den nye variant Brand,  Sikre at knappen kan anvendes på tværs af flere produkter og domæner.
- Typografi
- Medium (default) benytter nu utility/large/medium i stedet for utility/medium/medium. Sikrer bedre sammenhæng mellem labels, tekst, knapper og logoer på tværs af systemet.
- Størrelsesjusteringer
- Small er justeret fra 34 px til 32 px  for at harmonere med størrelsesskalaen.
- Ny kompakt knapstørrelse på 24 px er tilføjet  Rule of 3”-princip - og understøtter nu specifikke use cases og arbejdet med Rebus-komponenter.
- Komponentændringer
- Leading icon er nu slukket som default for at forenkle komponenten og forbedre brugervenligheden
- Ændringerne understøtter et mere konsistent samspil mellem labels, tekst, knapper og logoer på tværs af produkter.

## 2.0.0
**26.2.2026**

- Flere primary knapper igen Live, breaking, commercial, play entry er blevet tilføjet som type i figma. De har nu mere guidende navngivning med tilhørende dokumentation.
- Ændringer aftalt på UI guild

## 1.0.0
**2.5.2025**

- XS-knap (H: 28 px / Text: 12 pt) I december 2023 blev XS-knappen tilføjet for at håndtere behovet for en diskret knap på liveblogs. I praksis anvendes dog en 24 px-knap i produktion. Ifølge vores “Rule of 3”-princip er XS‑knappen ikke tilstrækkeligt udbredt til at inkluderes i DS | Shared.
- Oprydning i mængden af primære knapper For at skabe større klarhed har vi fjernet “Neutral primary” knappen.  Fremover er der kun én branded primærknap, hvilket gør knapvalget tydeligere for designere.
- Ny “Button commercial”  Vi har tilføjet en kommerciel variant til primary button, med særlig farve, som imødekommer kommerciel afdelings ønsker. Bemærk: Der bør stadig kun forekomme én primary button i et viewport.

