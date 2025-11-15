"""
Microsoft Fabric Connector
Modulo per connettersi e interagire con Microsoft Fabric
"""

import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Carica le variabili d'ambiente
load_dotenv()


class FabricConnector:
    """
    Classe per gestire la connessione a Microsoft Fabric
    """

    def __init__(
        self,
        tenant_id: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        workspace_id: Optional[str] = None
    ):
        """
        Inizializza il connettore Fabric

        Args:
            tenant_id: Azure Tenant ID
            client_id: Azure Client ID (Service Principal)
            client_secret: Azure Client Secret
            workspace_id: ID del workspace Fabric
        """
        self.tenant_id = tenant_id or os.getenv('FABRIC_TENANT_ID')
        self.client_id = client_id or os.getenv('FABRIC_CLIENT_ID')
        self.client_secret = client_secret or os.getenv('FABRIC_CLIENT_SECRET')
        self.workspace_id = workspace_id or os.getenv('FABRIC_WORKSPACE_ID')

        self._validate_credentials()

    def _validate_credentials(self):
        """Valida che tutte le credenziali necessarie siano presenti"""
        required_fields = {
            'tenant_id': self.tenant_id,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        missing = [k for k, v in required_fields.items() if not v]
        if missing:
            raise ValueError(
                f"Credenziali mancanti: {', '.join(missing)}. "
                "Configurare le variabili d'ambiente o passarle al costruttore."
            )

    def connect(self) -> bool:
        """
        Stabilisce la connessione con Microsoft Fabric

        Returns:
            bool: True se la connessione è riuscita
        """
        try:
            # Importa la libreria ms-fabric-cli
            from fabric_cli import FabricClient

            # Crea il client Fabric
            self.client = FabricClient(
                tenant_id=self.tenant_id,
                client_id=self.client_id,
                client_secret=self.client_secret
            )

            print("✓ Connessione a Microsoft Fabric stabilita con successo!")
            return True

        except ImportError:
            raise ImportError(
                "La libreria ms-fabric-cli non è installata. "
                "Eseguire: pip install ms-fabric-cli"
            )
        except Exception as e:
            print(f"✗ Errore durante la connessione a Fabric: {str(e)}")
            return False

    def get_workspaces(self) -> list:
        """
        Recupera la lista dei workspace disponibili

        Returns:
            list: Lista dei workspace
        """
        if not hasattr(self, 'client'):
            raise RuntimeError("Client non connesso. Chiamare connect() prima.")

        try:
            workspaces = self.client.list_workspaces()
            return workspaces
        except Exception as e:
            print(f"Errore nel recupero dei workspace: {str(e)}")
            return []

    def get_workspace_items(self, workspace_id: Optional[str] = None) -> list:
        """
        Recupera gli elementi in un workspace

        Args:
            workspace_id: ID del workspace (usa quello configurato se non specificato)

        Returns:
            list: Lista degli elementi nel workspace
        """
        if not hasattr(self, 'client'):
            raise RuntimeError("Client non connesso. Chiamare connect() prima.")

        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError("Workspace ID non specificato")

        try:
            items = self.client.list_items(workspace_id=ws_id)
            return items
        except Exception as e:
            print(f"Errore nel recupero degli elementi: {str(e)}")
            return []

    def disconnect(self):
        """Chiude la connessione"""
        if hasattr(self, 'client'):
            delattr(self, 'client')
            print("✓ Disconnesso da Microsoft Fabric")


def main():
    """Esempio di utilizzo del connettore"""
    try:
        # Crea il connettore
        connector = FabricConnector()

        # Connetti a Fabric
        if connector.connect():
            # Recupera i workspace
            print("\n--- Workspace disponibili ---")
            workspaces = connector.get_workspaces()
            for ws in workspaces:
                print(f"  - {ws}")

            # Recupera gli elementi nel workspace configurato
            if connector.workspace_id:
                print(f"\n--- Elementi nel workspace {connector.workspace_id} ---")
                items = connector.get_workspace_items()
                for item in items:
                    print(f"  - {item}")

            # Disconnetti
            connector.disconnect()

    except Exception as e:
        print(f"Errore: {str(e)}")


if __name__ == "__main__":
    main()
