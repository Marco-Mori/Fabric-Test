"""
Esempi di utilizzo del connettore Microsoft Fabric
"""

from fabric_connector import FabricConnector


def example_basic_connection():
    """Esempio 1: Connessione base"""
    print("=" * 50)
    print("ESEMPIO 1: Connessione Base")
    print("=" * 50)

    # Crea il connettore (usa le credenziali dal file .env)
    connector = FabricConnector()

    # Connetti
    if connector.connect():
        print("Connesso con successo!")
        connector.disconnect()


def example_with_credentials():
    """Esempio 2: Connessione con credenziali esplicite"""
    print("\n" + "=" * 50)
    print("ESEMPIO 2: Connessione con Credenziali Esplicite")
    print("=" * 50)

    # Passa le credenziali direttamente
    connector = FabricConnector(
        tenant_id="your-tenant-id",
        client_id="your-client-id",
        client_secret="your-client-secret",
        workspace_id="your-workspace-id"
    )

    if connector.connect():
        print("Connesso con credenziali esplicite!")
        connector.disconnect()


def example_list_workspaces():
    """Esempio 3: Lista workspace"""
    print("\n" + "=" * 50)
    print("ESEMPIO 3: Lista Workspace")
    print("=" * 50)

    connector = FabricConnector()

    if connector.connect():
        # Recupera tutti i workspace
        workspaces = connector.get_workspaces()

        print(f"\nTrovati {len(workspaces)} workspace:")
        for i, workspace in enumerate(workspaces, 1):
            print(f"{i}. {workspace}")

        connector.disconnect()


def example_workspace_items():
    """Esempio 4: Lista elementi in un workspace"""
    print("\n" + "=" * 50)
    print("ESEMPIO 4: Elementi del Workspace")
    print("=" * 50)

    connector = FabricConnector()

    if connector.connect():
        try:
            # Usa il workspace configurato nel .env
            items = connector.get_workspace_items()

            print(f"\nTrovati {len(items)} elementi:")
            for i, item in enumerate(items, 1):
                print(f"{i}. {item}")

        except ValueError as e:
            print(f"Errore: {e}")
            print("Assicurati di configurare FABRIC_WORKSPACE_ID nel file .env")

        connector.disconnect()


def example_context_manager():
    """Esempio 5: Uso come context manager"""
    print("\n" + "=" * 50)
    print("ESEMPIO 5: Context Manager Pattern")
    print("=" * 50)

    # Questo esempio mostra un pattern consigliato
    connector = FabricConnector()

    try:
        connector.connect()

        # Esegui operazioni
        workspaces = connector.get_workspaces()
        print(f"Workspace trovati: {len(workspaces)}")

    finally:
        # Assicura la disconnessione
        connector.disconnect()


if __name__ == "__main__":
    print("\n🔷 ESEMPI DI UTILIZZO - Microsoft Fabric Connector\n")

    try:
        # Esegui gli esempi
        example_basic_connection()
        # example_with_credentials()  # Decommentare per testare
        # example_list_workspaces()  # Decommentare dopo aver configurato le credenziali
        # example_workspace_items()  # Decommentare dopo aver configurato le credenziali
        # example_context_manager()  # Decommentare per testare

        print("\n" + "=" * 50)
        print("✓ Esempi completati!")
        print("=" * 50)

    except Exception as e:
        print(f"\n✗ Errore durante l'esecuzione degli esempi: {str(e)}")
