https://x.com/SolShieldLayer

**Privacy layer for Solana transactions – in early development**

## Overview

SolShield is a planned decentralized privacy protocol built on Solana.  
The goal is to provide users with an easy and affordable way to enhance the privacy of their SOL and SPL token transactions while maintaining Solana's speed and low costs.

### Key Planned Features
- **Private Mixes** – Send tokens through an anonymity pool to break transaction links
- **Fee Payment in $SHIELD** – Small fee paid in the native token for each mix
- **Tiered Discounts** – Holding more $SHIELD reduces mixing fees
- **Staking & Real Yield** – Stakers receive a share of all collected mixing fees

## Current Status (January 2026)

**⚠️ Important Notice**  
This project is in the **very early conceptual and prototyping stage**.  

There is currently:
- No deployed SPL token
- No on-chain smart contracts
- No functional mixer or privacy mechanism
- Only a static landing page, mock backend simulation, and documentation

Everything in this repository is for demonstration and planning purposes only.

## Repository Contents

- `frontend/` – Static landing page (HTML + Tailwind CSS + basic wallet connect demo)
- `backend-mock/` – Off-chain Python simulation of mixing logic (concept only)
- `docs/` – Detailed project documentation (Introduction, Tokenomics, Roadmap, etc.)
- `README.md` – This file

## Quick Start (Landing Page)

To view the current website prototype locally:

```bash
# Option 1: Simply open in browser
open frontend/index.html

# Option 2: Use a local server
cd frontend
npx serve          # or
python -m http.server 8000
