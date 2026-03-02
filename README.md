# LLM Agent för Avståndsmätning

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.13-1C3C3C)](https://python.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)](https://platform.openai.com/)
[![Last Commit](https://img.shields.io/github/last-commit/petbjo1/ai-agents-demo)](https://github.com/petbjo1/ai-agents-demo/commits/main)
[![GitHub Stars](https://img.shields.io/github/stars/petbjo1/ai-agents-demo?style=social)](https://github.com/petbjo1/ai-agents-demo/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/petbjo1/ai-agents-demo)](https://github.com/petbjo1/ai-agents-demo/issues)

Detta projekt använder LangChain och OpenAI för att skapa en AI-agent som kan beräkna avstånd mellan städer.

## Innehåll 📚
- 🐍 [Installation av Python](#installation-av-python)
- 📦 [Installation av Dependencies](#installation-av-dependencies)
- 📧 [Ange din Epost för openstreetmap](#ange-din-epost-for-openstreetmap)
- 🔑 [Konfigurera OpenAI API-nyckel](#konfigurera-openai-api-nyckel)
- 🧪 [Köra testerna](#kora-testerna)
- 🤖 [Köra LLM-agenten](#kora-llm-agenten)
---

<a id="installation-av-python"></a>
## Installation av Python 🐍

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

<a id="installation-av-dependencies"></a>
## Installation av Dependencies 📦

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

<a id="ange-din-epost-for-openstreetmap"></a>
## Ange din Epost för openstreetmap 📧

Redigera `agents.py` och ersätt `"din.epost@adress.com"` med din riktiga Epostadress:
```python
params = {
        "q": location_name,
        "format": "json",
        "email": "darth.vader@empire.com",
        "limit": 1
    }
```

<a id="konfigurera-openai-api-nyckel"></a>
## Konfigurera OpenAI API-nyckel 🔑

Du behöver en Azure OpenAI API-nyckel för att köra LLM-agenten.

### Skaffa API-nyckel

1. Gå till [ai.azure.com](https://ai.azure.com)
2. Logga in och gå till ditt projekt (project-agio-id)
3. Navigera till Models + endpoints
4. Välj gpt-4.1.
5. Här hittar du värden för API-nyckel, API-version, endpoint. Deployment name är det som listas under name vilket för den här modellen är 'gpt-4.1'.

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

**Alternativ 3: Genom en .env-fil**
Skapa en `.env.local` fil i projektmappen:

```bash
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT=gpt-4.1
AZURE_OPENAI_API_VERSION=2024-12-01-preview
```

⚠️ **VARNING:** Lägg aldrig API-nycklar i Git! Lägg till `.env` i `.gitignore` om du använder miljövariabler.

---

<a id="kora-testerna"></a>
## Köra testerna 🧪

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

<a id="kora-llm-agenten"></a>
## Köra LLM-agenten 🤖

LLM-agenten använder AI för att besvara frågor om avstånd mellan städer.

### Windows
```cmd
python llm.py
```

### macOS
```bash
python3 llm.py
```

### Vad händer? ⚙️

Agenten kommer att:
1. ❓ Läsa frågan "Hur långt är det från Stockholm till Göteborg?"
2. 📍 Använda `geocoder`-verktyget för att hitta koordinater för Stockholm
3. 📍 Använda `geocoder`-verktyget för att hitta koordinater för Göteborg
4. 📏 Använda `distance_calc`-verktyget för att beräkna avståndet
5. 🗣️ Ge ett svar i naturligt språk

### Exempel på output
```
> Entering new AgentExecutor chain...
I need to find the coordinates for Stockholm and Göteborg first, then calculate the distance.

Action: geocoder
Action Input: Stockholm
...
Final Answer: Avståndet mellan Stockholm och Göteborg är cirka 399 km.
```

## Felsökning 🛠️

### "python kommandot hittades inte"
- 🪟 **Windows:** Se till att Python är tillagt i PATH under installationen
- 🍎 **macOS:** Använd `python3` istället för `python`

### "ModuleNotFoundError: No module named 'langchain'"
- ✅ Kontrollera att du aktiverat den virtuella miljön (`venv`)
- 🔁 Kör `pip install -r requirements.txt` igen

### "OpenAI API error: Invalid API key"
- 🔍 Kontrollera att din API-nyckel är korrekt
- 💳 Se till att du har tillräcklig kredit på ditt OpenAI-konto
- 🌱 Verifiera att miljövariabeln är satt (kör `echo %OPENAI_API_KEY%` på Windows eller `echo $OPENAI_API_KEY` på macOS)

### "Rate limit exceeded"
- 🚦 Du har överskridit OpenAI:s API-gränser
- ⏳ Vänta en stund och försök igen
- 📈 Överväg att uppgradera din OpenAI-plan

---

## Nästa steg 🚀

- 🧠 Modifiera frågan i `llm.py` för att testa med andra städer
- 🧰 Lägg till fler verktyg (tools) för agenten
- 🧪 Experimentera med olika LLM-modeller (t.ex. `gpt-4`)

## Licens

Detta är ett utbildningsprojekt.
