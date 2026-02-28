# LLM Agent för Avståndsmätning

Detta projekt använder LangChain och OpenAI för att skapa en AI-agent som kan beräkna avstånd mellan städer.

## Innehåll
- [Installation av Python](#installation-av-python)
- [Installation av Dependencies](#installation-av-dependencies)
- [Ange din Epost för openstreetmap](#Ange-din-Epost-för-openstreetmap)
- [Konfigurera OpenAI API-nyckel](#konfigurera-openai-api-nyckel)
- [Köra testerna](#köra-testerna)
- [Köra LLM-agenten](#köra-llm-agenten)
- [Om du hellre vill använda Azure LLM 🎯](#Om-du-hellre-vill-använda-Azure-LLM)
---

## Installation av Python

### Windows

1. **Ladda ner Python:**
   - Gå till [python.org/downloads](https://www.python.org/downloads/)
   - Ladda ner senaste versionen av Python (3.10 eller senare rekommenderas)

2. **Installera Python:**
   - Kör installationsfilen
   - **VIKTIGT:** Kryssa i "Add Python to PATH" längst ner i installationsfönstret
   - Klicka på "Install Now"

3. **Verifiera installationen:**
   ```cmd
   python --version
   ```

### macOS

1. **Installera Homebrew (om du inte redan har det):**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Installera Python:**
   ```bash
   brew install python@3.11
   ```

3. **Verifiera installationen:**
   ```bash
   python3 --version
   ```

---

## Installation av Dependencies

### Windows

1. **Öppna Command Prompt eller PowerShell**

2. **Navigera till projektmappen:**
   ```cmd
   cd sökväg\till\ditt\projekt
   ```

3. **Skapa en virtuell miljö (rekommenderas):**
   ```cmd
   python -m venv venv
   ```

4. **Aktivera den virtuella miljön:**
   ```cmd
   venv\Scripts\activate
   ```
   
   Du bör nu se `(venv)` i början av din kommandorad.

5. **Installera dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

6. **Installera pytest för att köra tester:**
   ```cmd
   pip install pytest
   ```

### macOS

1. **Öppna Terminal**

2. **Navigera till projektmappen:**
   ```bash
   cd sökväg/till/ditt/projekt
   ```

3. **Skapa en virtuell miljö (rekommenderas):**
   ```bash
   python3 -m venv venv
   ```

4. **Aktivera den virtuella miljön:**
   ```bash
   source venv/bin/activate
   ```
   
   Du bör nu se `(venv)` i början av din kommandorad.

5. **Installera dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Installera pytest för att köra tester:**
   ```bash
   pip install pytest
   ```

---

## Ange din Epost för openstreetmap

Redigera `agents.py` och ersätt `"din.epost@adress.com"` med din riktiga Epostadress:
```python
params = {
        "q": location_name,
        "format": "json",
        "email": "darth.vader@empire.com",
        "limit": 1
    }
```

## Konfigurera OpenAI API-nyckel

Du behöver en OpenAI API-nyckel för att köra LLM-agenten.

### Skaffa API-nyckel

1. Gå till [platform.openai.com](https://platform.openai.com)
2. Skapa ett konto eller logga in
3. Navigera till API-nycklar
4. Skapa en ny API-nyckel

### Sätt API-nyckeln

**Alternativ 1: Miljövariabel (rekommenderas)**

#### Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=din-api-nyckel-här
```

#### Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="din-api-nyckel-här"
```

#### macOS/Linux:
```bash
export OPENAI_API_KEY=din-api-nyckel-här
```

**Alternativ 2: Direkt i koden**

Redigera `llm.py` och ersätt `"din api nyckel"` med din riktiga API-nyckel:
```python
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key="sk-proj-xxxxxxxxxxxxxxxxxx"  # Din riktiga nyckel
)
```

⚠️ **VARNING:** Lägg aldrig API-nycklar i Git! Lägg till `.env` i `.gitignore` om du använder miljövariabler.

---

## Köra testerna

Testerna validerar att funktionerna för geokodning och avståndsmätning fungerar korrekt.

### Windows
```cmd
pytest test_agents.py -v
```

### macOS
```bash
pytest test_agents.py -v
```

### Förväntad output
```
test_agents.py::test_geocode_location_success PASSED
test_agents.py::test_geocode_location_not_found PASSED
test_agents.py::test_haversine_distance_stockholm_lulea PASSED
test_agents.py::test_calculate_city_distance_success PASSED
test_agents.py::test_calculate_city_distance_failure PASSED
```

---

## Köra LLM-agenten

LLM-agenten använder AI för att besvara frågor om avstånd mellan städer.

### Windows
```cmd
python llm.py
```

### macOS
```bash
python3 llm.py
```

### Vad händer?

Agenten kommer att:
1. Läsa frågan "Hur långt är det från Stockholm till Göteborg?"
2. Använda `geocoder`-verktyget för att hitta koordinater för Stockholm
3. Använda `geocoder`-verktyget för att hitta koordinater för Göteborg
4. Använda `distance_calc`-verktyget för att beräkna avståndet
5. Ge ett svar i naturligt språk

### Exempel på output
```
> Entering new AgentExecutor chain...
I need to find the coordinates for Stockholm and Göteborg first, then calculate the distance.

Action: geocoder
Action Input: Stockholm
...
Final Answer: Avståndet mellan Stockholm och Göteborg är cirka 399 km.
```

## Felsökning

### "python kommandot hittades inte"
- **Windows:** Se till att Python är tillagt i PATH under installationen
- **macOS:** Använd `python3` istället för `python`

### "ModuleNotFoundError: No module named 'langchain'"
- Kontrollera att du aktiverat den virtuella miljön (`venv`)
- Kör `pip install -r requirements.txt` igen

### "OpenAI API error: Invalid API key"
- Kontrollera att din API-nyckel är korrekt
- Se till att du har tillräcklig kredit på ditt OpenAI-konto
- Verifiera att miljövariabeln är satt (kör `echo %OPENAI_API_KEY%` på Windows eller `echo $OPENAI_API_KEY` på macOS)

### "Rate limit exceeded"
- Du har överskridit OpenAI:s API-gränser
- Vänta en stund och försök igen
- Överväg att uppgradera din OpenAI-plan

---

## Nästa steg

- Modifiera frågan i `llm.py` för att testa med andra städer
- Lägg till fler verktyg (tools) för agenten
- Experimentera med olika LLM-modeller (t.ex. `gpt-4`)

## Om du hellre vill använda Azure LLM
- [Öppna detta dokument i Azure branchen](https://github.com/petbjo1/ai-agents-demo/tree/azureai-version)
- Eller klona Azure branchen direkt
  ```bash
   git clone --branch azureai-version --single-branch git@github.com:petbjo1/ai-agents-demo.git
   ```
## Licens

Detta är ett utbildningsprojekt.