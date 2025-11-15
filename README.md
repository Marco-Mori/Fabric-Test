# Microsoft Fabric CLI Integration

Progetto per l'integrazione con Microsoft Fabric utilizzando la libreria `ms-fabric-cli`.

## Requisiti

- Python 3.8 o superiore
- Account Microsoft Fabric
- Service Principal con accesso a Fabric

## Installazione

### 1. Clona il repository

```bash
git clone <repository-url>
cd Fabric-Test
```

### 2. Crea un ambiente virtuale (consigliato)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oppure
venv\Scripts\activate  # Windows
```

### 3. Installa le dipendenze

```bash
pip install -r requirements.txt
```

## Configurazione

### 1. Crea un Service Principal in Azure

Per autenticarti a Microsoft Fabric, hai bisogno di un Service Principal:

1. Vai al [portale Azure](https://portal.azure.com)
2. Naviga su "Azure Active Directory" > "App registrations"
3. Clicca su "New registration"
4. Compila i campi richiesti e clicca "Register"
5. Annota il **Client ID** e il **Tenant ID**
6. Vai su "Certificates & secrets" > "New client secret"
7. Crea un segreto e annota il **Client Secret**

### 2. Configura le credenziali

Copia il file `.env.example` in `.env`:

```bash
cp .env.example .env
```

Modifica il file `.env` con le tue credenziali:

```env
FABRIC_TENANT_ID=your-tenant-id
FABRIC_CLIENT_ID=your-client-id
FABRIC_CLIENT_SECRET=your-client-secret
FABRIC_WORKSPACE_ID=your-workspace-id
```

### 3. Concedi permessi al Service Principal

Assicurati che il Service Principal abbia i permessi necessari sul tuo workspace Fabric.

## Utilizzo

### Esempio Base

```python
from fabric_connector import FabricConnector

# Crea il connettore
connector = FabricConnector()

# Connetti a Fabric
if connector.connect():
    # Recupera i workspace
    workspaces = connector.get_workspaces()
    print(f"Workspace disponibili: {workspaces}")

    # Disconnetti
    connector.disconnect()
```

### Esegui gli esempi

```bash
python fabric_connector.py
```

Oppure esegui gli esempi specifici:

```bash
python example_usage.py
```

## Struttura del Progetto

```
Fabric-Test/
├── fabric_connector.py    # Modulo principale per la connessione
├── example_usage.py       # Esempi di utilizzo
├── requirements.txt       # Dipendenze Python
├── .env.example          # Template per le variabili d'ambiente
├── .gitignore           # File da ignorare in Git
└── README.md            # Questa documentazione
```

## API Reference

### FabricConnector

Classe principale per gestire la connessione a Microsoft Fabric.

#### Costruttore

```python
FabricConnector(
    tenant_id: Optional[str] = None,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    workspace_id: Optional[str] = None
)
```

**Parametri:**
- `tenant_id`: Azure Tenant ID (opzionale, usa .env se non specificato)
- `client_id`: Azure Client ID (opzionale, usa .env se non specificato)
- `client_secret`: Azure Client Secret (opzionale, usa .env se non specificato)
- `workspace_id`: ID del workspace Fabric (opzionale, usa .env se non specificato)

#### Metodi

##### connect()

Stabilisce la connessione con Microsoft Fabric.

```python
connector.connect() -> bool
```

**Returns:** `True` se la connessione è riuscita, `False` altrimenti.

##### get_workspaces()

Recupera la lista dei workspace disponibili.

```python
connector.get_workspaces() -> list
```

**Returns:** Lista dei workspace.

##### get_workspace_items(workspace_id)

Recupera gli elementi in un workspace specifico.

```python
connector.get_workspace_items(workspace_id: Optional[str] = None) -> list
```

**Parametri:**
- `workspace_id`: ID del workspace (usa quello configurato se non specificato)

**Returns:** Lista degli elementi nel workspace.

##### disconnect()

Chiude la connessione.

```python
connector.disconnect()
```

## Troubleshooting

### Errore: "Credenziali mancanti"

Assicurati di aver configurato correttamente il file `.env` con tutte le credenziali richieste.

### Errore: "La libreria ms-fabric-cli non è installata"

Esegui:

```bash
pip install ms-fabric-cli
```

### Errore di autenticazione

Verifica che:
1. Le credenziali nel file `.env` siano corrette
2. Il Service Principal abbia i permessi necessari
3. Il Tenant ID sia corretto

## Contribuire

Le pull request sono benvenute! Per modifiche importanti, apri prima un issue per discutere cosa vorresti cambiare.

## Licenza

[MIT](https://choosealicense.com/licenses/mit/)

## Risorse Utili

- [Documentazione Microsoft Fabric](https://learn.microsoft.com/fabric/)
- [Azure Service Principal](https://learn.microsoft.com/azure/active-directory/develop/app-objects-and-service-principals)
- [ms-fabric-cli su PyPI](https://pypi.org/project/ms-fabric-cli/)
