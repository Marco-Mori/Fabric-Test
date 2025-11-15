#!/usr/bin/env python3
"""
Script per autenticarsi a Microsoft Fabric
"""

import subprocess
import sys


def run_fabric_command(command_args):
    """Esegue un comando fabric_cli"""
    try:
        result = subprocess.run(
            [sys.executable, "/usr/local/lib/python3.11/dist-packages/fabric_cli/main.py"] + command_args,
            capture_output=False,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Errore durante l'esecuzione del comando: {e}")
        return False


def login_interactive():
    """Login interattivo (apre il browser)"""
    print("\n🔐 Avvio login interattivo a Microsoft Fabric...")
    print("Si aprirà una finestra del browser per l'autenticazione.\n")
    return run_fabric_command(["auth", "login"])


def login_service_principal(client_id, client_secret, tenant_id):
    """Login con Service Principal"""
    print("\n🔐 Login con Service Principal...")
    return run_fabric_command([
        "auth", "login",
        "-u", client_id,
        "-p", client_secret,
        "-t", tenant_id
    ])


def check_auth_status():
    """Verifica lo stato dell'autenticazione"""
    print("\n📊 Verifica stato autenticazione...\n")
    return run_fabric_command(["auth", "status"])


def logout():
    """Logout da Fabric"""
    print("\n👋 Logout da Microsoft Fabric...")
    return run_fabric_command(["auth", "logout"])


def main():
    print("=" * 60)
    print("    Microsoft Fabric - Autenticazione")
    print("=" * 60)

    print("\nOpzioni disponibili:")
    print("  1. Login interattivo (browser)")
    print("  2. Login con Service Principal")
    print("  3. Verifica stato autenticazione")
    print("  4. Logout")
    print("  5. Esci")

    choice = input("\nScegli un'opzione (1-5): ").strip()

    if choice == "1":
        if login_interactive():
            print("\n✓ Login completato con successo!")
            check_auth_status()
        else:
            print("\n✗ Login fallito")

    elif choice == "2":
        print("\nInserisci le credenziali del Service Principal:")
        client_id = input("Client ID: ").strip()
        client_secret = input("Client Secret: ").strip()
        tenant_id = input("Tenant ID: ").strip()

        if login_service_principal(client_id, client_secret, tenant_id):
            print("\n✓ Login completato con successo!")
            check_auth_status()
        else:
            print("\n✗ Login fallito")

    elif choice == "3":
        check_auth_status()

    elif choice == "4":
        logout()

    elif choice == "5":
        print("\nCiao!")
        sys.exit(0)

    else:
        print("\nOpzione non valida")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrotto dall'utente")
        sys.exit(0)
