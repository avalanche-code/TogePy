# togePy React App

Diese React-Anwendung ermöglicht die Suche nach Pokémon über die Pokémon-API. Nutzer können Pokémon anzeigen lassen, speichern und später wieder aus der Liste entfernen.

## Funktionalität

- Suche nach Pokémon über ein Suchfeld
- Anzeige von Name, Typ, Angriffen und Bild
- Speichern von gefundenen Pokémon in einer lokalen Liste
- Entfernen gespeicherter Pokémon
- Fehleranzeige bei nicht gefundenen Pokémon

## Technologie-Stack

- React
- TypeScript
- Vite
- Tailwind CSS
- Playwright
- ESLint

## Lokale Entwicklung

### Abhängigkeiten installieren

```bash
npm install
```

### Entwicklungsserver starten

```bash
npm run dev
```

Die App ist anschließend unter http://localhost:5173 verfügbar.

## Tests

End-to-End-Tests mit Playwright:

```bash
npx playwright test
```
Unitest mit Vitetest

```bash
npm run test:coverage
```
## Statische Analyse

Linting mit ESLint:

```bash
npm run lint
```

## Build

Produktionsbuild erzeugen:

```bash
npm run build
```

## CI/CD

Unsere Pipeline ist so konzipiert, dass sie jede Änderung an der Anwendung automatisch prüft, bevor sie weiterverarbeitet wird. Der Ablauf besteht aus diesen Schritten:

1. Abhängigkeiten installieren
2. Statische Analyse mit ESLint ausführen
3. End-to-End-Tests mit Playwright ausführen
4. Einen Produktionsbuild erzeugen

Damit wird sichergestellt, dass die App sauber, testbar und deployfähig bleibt. In einer GitHub Pages-Pipeline kann das Ergebnis nach erfolgreichem Build automatisch ins `gh-pages`-Branch deployed werden.

Beispiel für den Ablauf:

```bash
npm install
npm run lint
npm run test:coverage
npx playwright test
npm run build
```
