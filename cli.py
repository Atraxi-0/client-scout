"""
cli.py
Terminal interface for the ClientScout B2B Intelligence Agent.
Handles user input, triggers the engine, and formats the output.
"""

import sys
import time
from engine import invoke_agent

def print_banner():
    """Prints the application banner."""
    print("=" * 60)
    print("   CLIENTSCOUT: Autonomous B2B Intelligence Agent")
    print("=" * 60)
    print("Type 'exit' or 'quit' to terminate the session.\n")

def main():
    """Main execution loop for the terminal UI."""
    print_banner()
    
    while True:
        try:
            # 1. Capture User Input
            company_name = input("[SYSTEM] Enter target B2B company name: ").strip()
            
            # 2. Handle Exit Commands
            if company_name.lower() in ['exit', 'quit']:
                print("\n[SYSTEM] Terminating ClientScout session. Goodbye.")
                sys.exit(0)
                
            if not company_name:
                print("[WARNING] Company name cannot be empty. Please try again.\n")
                continue
                
            # 3. UI Loading State
            print(f"\n[*] Initializing intelligence sweep for '{company_name}'...")
            print("[*] Engaging reasoning engine and live web search. Please wait...\n")
            
            # 4. Trigger the Engine (The Handoff)
            start_time = time.time()
            report = invoke_agent(company_name)
            elapsed_time = time.time() - start_time
            
            # 5. Display the Output
            print("-" * 60)
            print(report)
            print("-" * 60)
            print(f"[SYSTEM] Report generated in {elapsed_time:.2f} seconds.\n")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n[SYSTEM] Manual interrupt detected. Shutting down.")
            sys.exit(0)
        except Exception as e:
            # Catch unexpected CLI errors
            print(f"\n[CRITICAL ERROR] Terminal UI encountered a failure: {str(e)}\n")

if __name__ == "__main__":
    main()