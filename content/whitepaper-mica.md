# OROG — Crypto-Asset White Paper

**Issued under Regulation (EU) 2023/1114 (MiCA), Title II, Articles 6, 8 and 9 — for a crypto-asset other than an asset-referenced token or an e-money token.**

---

## Mandatory statements

**Date of notification of this white paper to the competent authority:** [TO FILL — to be inserted not less than 20 working days before publication, per Article 8(1) MiCA].

**Date of publication:** [TO FILL].

**Statement in accordance with Article 6(3) MiCA.** *This crypto-asset white paper has not been approved by any competent authority in any Member State of the European Union. The offeror of the crypto-asset is solely responsible for the content of this crypto-asset white paper.*

**Statement of compliance in accordance with Article 6(6) MiCA — Management body declaration.** *The management body of the offeror declares that, to the best of its knowledge, this crypto-asset white paper complies with the requirements of Title II of Regulation (EU) 2023/1114 and that the information presented in this white paper is fair, clear and not misleading and that this white paper makes no omission likely to affect its import.*

Signed by the management body of the offeror on [TO FILL — date] at [TO FILL — place].

**Warnings in accordance with Article 6(5) MiCA.**

- The crypto-asset described in this white paper, OROG, may lose its value in part or in full.
- OROG may not always be transferable.
- OROG may not be liquid.
- OROG is not covered by investor compensation schemes under Directive 97/9/EC.
- OROG is not covered by deposit guarantee schemes under Directive 2014/49/EU.

**Right of withdrawal (Article 13 MiCA).** Retail holders who purchase OROG directly from the offeror or from a crypto-asset service provider placing OROG on behalf of the offeror have the right to withdraw their agreement to purchase without incurring any fees or costs and without being required to give reasons, within a period of fourteen (14) calendar days from the date of their agreement to purchase. The withdrawal procedure is described in Part E §E.13 of this white paper.

**Important.** This white paper is, in places, technical. Prospective acquirers should read it in full and seek independent advice before any acquisition decision. The summary that follows is an introduction only; any decision should be based on the white paper as a whole.

---

## Summary (Article 6(7) MiCA)

*This summary is an introduction to the crypto-asset white paper. The prospective holder of OROG should base any decision to acquire OROG on the content of the crypto-asset white paper as a whole, not on the summary alone. The offer of OROG to the public does not constitute an offer or solicitation to sell financial instruments. Any such offer or solicitation can be made only by means of a prospectus or other offer documents pursuant to applicable national laws. This crypto-asset white paper does not constitute a prospectus as referred to in Regulation (EU) 2017/1129 or any other offer document pursuant to Union or national laws. The crypto-assets referred to in this crypto-asset white paper may lose their value in part or in full, may not always be transferable and may not be liquid. The crypto-assets are not covered by investor compensation schemes or deposit guarantee schemes.*

**What OROG is.** OROG is the native utility crypto-asset of the Orogen network — a decentralised, permissionless network for verifiable Large-Language-Model (LLM) inference. OROG is the means of payment for compute on the network and the unit in which network participants (operators, validators) are compensated.

**Type of crypto-asset.** OROG is classified by the offeror as a crypto-asset *other than an asset-referenced token or an e-money token* within the meaning of Article 3(1)(5) of MiCA. OROG is **not** pegged to any fiat currency, basket, commodity or other reference asset. OROG is **not** electronic money. OROG is **not** a financial instrument under MiFID II.

**Project.** The Orogen network provides an OpenAI-compatible inference API served by independent GPU operators, with multi-layer verification (Trusted Execution Environment attestation, validator replay, optimistic-ML challenges, watermarking) and burn-and-mint settlement on a Substrate-based blockchain with Ethereum-compatible JSON-RPC.

**Utility.** Customers pay for inference in fiat or stablecoin; the gateway burns OROG at oracle spot in exchange for non-transferable USD-pegged compute credits ("CUC"); operators are minted fresh OROG when jobs are finalised; verification is paid from the same per-job emission.

**Settlement split per job emission.** 75 % to the operator that served the inference; 15 % to verification work (validators, opML challengers, zkML provers); 5 % to protocol treasury; 5 % to governance stakers performing active security functions.

**Emission policy.** A pallet-enforced rule binds new mint to rolling 90-day burn × an elasticity factor, with a floor of 0.5 % of supply per year and a ceiling of 5 % of supply per year after the bootstrap phase. There is no foundation discretion to mint outside the rule. There is no halving schedule.

**Allocation summary at Token Generation Event ("TGE"):** Investors 12 %, Team & advisors 12 %, Treasury 10 %, Ecosystem 8 %, Provider bootstrap 8 %, Public/community 5 %, Reserve 5 %, Mining/emission pool 40 % (released by the emission rule over ≈10–15 years).

**Offer.** This white paper relates to the planned public offer of OROG and/or its admission to trading at TGE. The offer modalities (date, jurisdictions, amount, price) are set out in Part E.

**Key risks (non-exhaustive — see Part I for the complete list).** Total loss of value; illiquidity; failure of the offeror or the network to deliver the project; failure of the underlying technology (consensus halt, oracle manipulation, TEE compromise, smart-contract bug); regulatory change; competition; concentration of operators or validators; smart-contract or chain-bridging failure; environmental cost of GPU inference; tax treatment in the holder's jurisdiction.

**Environmental disclosure (Article 6(1)(j) MiCA).** The Orogen blockchain itself uses a Proof-of-Authority/Proof-of-Stake consensus (Substrate AURA/BABE + GRANDPA) whose direct energy footprint is comparable to other PoS L1s and small in absolute terms. The *application* layer — LLM inference performed by operators on GPU hardware — is energy-intensive. Quantitative indicators are reported in Part J in the format required by Annex III to Commission Delegated Regulation (EU) 2025/422 (the ESMA Regulatory Technical Standards on sustainability indicators, where applicable).

---

## Table of contents

- Mandatory statements
- Summary (Article 6(7))
- **Part A** — Information about the offeror
- **Part B** — Information about the issuer (if different)
- **Part C** — Information about the operator of the trading platform
- **Part D** — Information about the crypto-asset project
- **Part E** — Information about the offer to the public or admission to trading
- **Part F** — Information about the crypto-assets
- **Part G** — Information on rights and obligations attaching to the crypto-assets
- **Part H** — Information on the underlying technology
- **Part I** — Information on risks
- **Part J** — Information on principal adverse impacts on climate and the environment

---

## Part A — Information about the offeror

*Per Annex I, Part A, MiCA — required where the white paper is prepared in connection with an offer to the public.*

| Item | Disclosure |
|---|---|
| A.1 Name | [TO FILL — legal name of the offeror entity] |
| A.2 Legal form | [TO FILL — e.g. *Société par actions simplifiée unipersonnelle* (SASU) under French law / Stiftung under Swiss law / etc.] |
| A.3 Registered address and head office | [TO FILL — full address] |
| A.4 Registration date | [TO FILL] |
| A.5 Legal entity identifier (LEI) or other identifier | [TO FILL — 20-character LEI required by Art. 6(1)(b)] |
| A.6 Commercial register number | [TO FILL — e.g. SIREN/RCS for FR; UID for CH] |
| A.7 Phone number | [TO FILL] |
| A.8 Email address | hello@orogen.network (general); legal@orogen.network (legal). Press: press@orogen.network. |
| A.9 Response time for queries from holders | Within fifteen (15) working days for written queries received at legal@orogen.network. |
| A.10 Parent company (if any) | [TO FILL — or "Not applicable"] |
| A.11 Members of the management body | [TO FILL — full name, function, business address for each member, per Annex I A.11] |
| A.12 Business activity of the offeror | The offeror's principal activity is the development, publication and operation of the Orogen network and the issuance, distribution and stewardship of OROG. Ancillary activities include licensing of trademarks ("Orogen", "OROG"), publication of open-source software, and contracting with service providers for protocol operations. The offeror does not, in its own right, operate a regulated crypto-asset service (CASP) and does not provide custody, exchange, trading-platform operation, order routing or financial advice. Where any such service is required, it is delegated to a duly authorised third-party CASP. |
| A.13 Financial condition over the past three years | [TO FILL — audited or management accounts; or, if the entity is newly incorporated, a statement to that effect together with opening balance sheet]. As of the date of this white paper, the offeror has [TO FILL — equity figure] in shareholder equity and [TO FILL — debt figure] in financial debt. |
| A.14 Description of risks specific to the offeror | See Part I §I.2 ("Risks of the offeror"). |

**Conflicts of interest.** The offeror's management body, founders and employees may hold OROG, equity in companies operating on or with the Orogen network, or both. All such holdings are subject to the vesting and lock-up terms described in Part F §F.6 and in the offeror's internal Code of Conduct. The offeror is not aware of any conflict of interest material to the offer that is not disclosed in this white paper.

---

## Part B — Information about the issuer (if different from the offeror)

*Per Annex I, Part B, MiCA — required where the issuer of the crypto-asset is a different legal person from the offeror.*

**Applicability.** [TO FILL: either (i) "Not applicable. The offeror is also the issuer of OROG."  *or* (ii) the table below, completed for the issuer entity.]

| Item | Disclosure |
|---|---|
| B.1 Name | [TO FILL — typically the Orogen Foundation / Stiftung, Zug, Switzerland — per the project's foundation plan, see DECISIONS H2] |
| B.2 Legal form | [TO FILL — e.g. *Stiftung* under Swiss Civil Code arts. 80–89bis] |
| B.3 Registered address and head office | [TO FILL] |
| B.4 Registration date | [TO FILL] |
| B.5 LEI | [TO FILL] |
| B.6 Commercial register number | [TO FILL — Swiss UID] |
| B.7 Parent company (if any) | None — a Swiss Stiftung has no shareholders by operation of law. |
| B.8 Members of the management body / Foundation Council | [TO FILL — names, functions, business addresses] |
| B.9 Business activity | Stewardship of the Orogen protocol; custodianship of the protocol Treasury and Ecosystem allocations on behalf of the network; publication of governance proposals; commissioning of audits and security reviews. |
| B.10 Financial condition | [TO FILL — opening statement of net assets] |

---

## Part C — Information about the operator of the trading platform

*Per Annex I, Part C, MiCA — required where the white paper is prepared in connection with an application for admission to trading.*

**Applicability.** Not applicable as of the date of publication of this white paper. The offeror does not, on the date of publication, request admission to trading on any particular trading platform for crypto-assets in the European Union. Where, in the future, the offeror or any third party requests such admission, the operator of that trading platform shall (per Article 6(2) MiCA) ensure that an updated white paper is published containing the information required by Annex I, Part C.

---

## Part D — Information about the crypto-asset project

*Per Annex I, Part D, MiCA.*

### D.1 Name of the crypto-asset project

Orogen.

### D.2 Name and abbreviation of the crypto-asset

Orogen Network Token, ticker **OROG**.

### D.3 Brief description of the project

Orogen is a decentralised network for verifiable Large-Language-Model (LLM) inference. The network offers an OpenAI-compatible inference API served by independent GPU operators, with a multi-layer verification stack and burn-and-mint economic settlement on a Substrate-based blockchain with Ethereum-compatible JSON-RPC.

**Customer surface.** Application developers, agent platform builders, regulated enterprises and open-weight model authors connect to the network through an OpenAI-compatible gateway. They top up the gateway in fiat or stablecoin and consume metered compute against the resulting USD-pegged credits.

**Supply side.** Independent operators register attested GPU capacity in one of six hardware tiers (datacenter-premium, datacenter-standard, cloud-rented, prosumer, edge, embed-only). Operators stake OROG, run Trusted Execution Environments (NVIDIA H100/H200/B200 confidential-compute, Intel TDX, AMD SEV-SNP), and receive OROG settlement when their work is finalised on chain.

**Verification.** A multi-layer stack: (1) TEE attestation, (2) signed response receipts binding (model, prompt, output, attestation report) on chain, (3) validator replay of a stake-weighted random sample of inferences on independent hardware with deterministic kernels, (4) optimistic-ML (opML) challenge windows, (5) zero-knowledge ML proofs for selected sub-heads (moderation, routing, credit scoring), (6) commit-reveal randomness with customer nonces to bind the prompt to the inference, (7) watermarks where applicable, (8) administrative slashing for proven cheating.

### D.4 Reasons for the project

The market for LLM inference in 2026 is dominated by closed-source APIs from a small number of US vendors. Independent operators of GPU hardware lack a credible payment and verification rail for selling inference time directly to application builders. The project's reason for being is to provide that rail: an open settlement layer that customers can audit, that gives operators predictable USD-denominated revenue mechanics, and that no single vendor can rent-seek on.

### D.5 Key milestones (past and planned)

The following milestones reflect the project's plan as of the date of this white paper. They are forward-looking statements and are not guaranteed (see Part I §I.5).

| Phase | Window | Status (date of white paper) | Description |
|---|---|---|---|
| Stealth / research | 2025 H2 → 2026 Q1 | Completed | Research dossier, design, initial team. |
| Centralised stack | 2026 Q1 → 2026 Q2 | Completed | Inference gateway operational; first paying customers in pilot. |
| Forge testnet | 2026 Q2 → 2027 Q1 | **Live as of date of publication** | Public testnet "Forge". Operators register, validators replay, customers route OpenAI-compatible traffic. Testnet OROG only — no economic value. |
| Audit | 2027 Q1 → 2027 Q2 | Planned | Multi-firm chain and protocol audits. |
| TGE / mainnet | 2027 Q2 | Planned | Token Generation Event; mainnet block production; BME loop active from day 1. |
| Permissionless transition | 2027 Q3 | Planned | Operator registration becomes fully permissionless; multi-vendor attestation required. |
| Subsidy < 1× | 2028 | Planned | Annualised mint $ ≤ annualised real customer revenue $ on a rolling 90-day basis. |

### D.6 Resources allocated to the project

As of the date of publication, the offeror together with affiliated entities employs [TO FILL — headcount] full-time-equivalent personnel. The project's planning anchors call for ≈30 FTE at peak and a total budget on the order of USD 15–20 M over the runway to TGE. Funding sources to date are [TO FILL — e.g. founder equity, pre-seed/seed financing]. Further funding may be raised before TGE; see Part F §F.10.

### D.7 Use of crypto-asset proceeds, if any

If and to the extent OROG is sold to acquirers for fiat or other crypto-assets in connection with the offer described in Part E, proceeds (net of offer-related costs) shall be allocated, indicatively, as follows: protocol engineering and security ≈ 60 %; operator and ecosystem grants ≈ 15 %; legal, compliance and licensing ≈ 10 %; marketing, business development and customer acquisition ≈ 10 %; general working capital ≈ 5 %. The actual allocation may differ. Material variations from this indicative allocation will be disclosed in updates to this white paper per Article 12 MiCA.

### D.8 Planned use of the crypto-asset

OROG is the **only** means by which compute on the Orogen network may be paid for at protocol level. There is no fiat-direct or stablecoin-direct bypass: the gateway smart-contract enforces the burn of OROG at oracle spot in exchange for compute credit. OROG is also the asset in which network participants (operators, validators, opML challengers, zkML provers, governance stakers performing active security functions) are compensated, and the asset in which operator stake and slashing collateral are denominated.

### D.9 Indication of whether the project relates to development, use or acquisition

Development *and* use. The project relates both to the **development** of an open-source, decentralised inference protocol and to its **operational use** as a metered compute service. OROG is a utility crypto-asset used for compute settlement, bonding, and governance.

---

## Part E — Information about the offer to the public or admission to trading

*Per Annex I, Part E, MiCA.*

### E.1 Indication of whether this white paper concerns an offer to the public or an admission to trading

This white paper concerns a planned offer of OROG to the public and, separately, the planned admission of OROG to trading on one or more trading platforms for crypto-assets operated by authorised crypto-asset service providers in the European Union, in each case at or after TGE.

### E.2 Reasons for the offer

To distribute OROG to network participants (operators, validators, customers and the broader user community), to establish a sufficiently liquid secondary market for OROG to support the burn-and-mint loop, and to align long-term incentives across the contributor base.

### E.3 Total amount offered

The total amount of OROG offered to the public at TGE will be a sub-allocation of the **Public / community / airdrop** bucket described in Part F §F.6 (currently sized at 5 % of total initial supply, fully unlocked at TGE). The precise amount, currency-equivalent value and price methodology will be published as an addendum to this white paper not less than 20 working days before the offer opens, per Article 12 MiCA.

[TO FILL — final values once set: total OROG offered, fiat-equivalent cap, minimum/maximum subscription.]

### E.4 Issue price

[TO FILL — issue price; method of price formation: fixed price, auction, book-building, or market-formation event]. Any price-formation methodology shall be disclosed and shall be consistent with the prohibition on insider trading and market manipulation in Title VI MiCA.

### E.5 Subscription period

[TO FILL — opening date, closing date, any extension mechanism]. The subscription period shall be no shorter than is required to give effect to the right of withdrawal in Article 13 MiCA (see §E.13 below).

### E.6 Payment methods accepted

Subject to local payment-services and anti-money-laundering law, the offeror may accept some or all of: EUR, USD, USDC, USDT, ETH, BTC. The list of accepted means of payment in force during the subscription period will be published on orogen.network and may be amended on notice.

### E.7 Allocation method

[TO FILL — pro-rata at price, lottery, first-come-first-served, weighted by KYC tier, weighted by prior testnet participation, etc.]. The allocation method shall not discriminate on any prohibited basis under Union law.

### E.8 Refund mechanism if the offer is not fully subscribed or is cancelled

If, on the closing date of the subscription period, the total amount subscribed does not reach the minimum amount disclosed pursuant to §E.3, *or* if the offer is cancelled by the offeror for any reason, all funds received from subscribers shall be returned to the originating account within fifteen (15) working days of the cancellation or closing, without deduction (other than reasonable and necessarily incurred third-party transaction fees, where it is impossible to refund gross). No OROG shall be transferred to subscribers in the event of a cancellation.

### E.9 Geographic scope of the offer

[TO FILL — list of EU Member States in which the offer is made; list of third countries (if any)]. The offer is *not* made to persons resident in jurisdictions where its making would be unlawful, including (without limitation) jurisdictions on the EU consolidated financial-sanctions list, FATF high-risk jurisdictions, and any jurisdiction in which the offer would require a registration or authorisation that has not been obtained. KYC and sanctions screening will be performed by the offeror or its agents prior to allocation.

### E.10 Holding-period restrictions

OROG sold pursuant to this offer is unrestricted as to subsequent transfer at protocol level. Specific allocations (founders, team, advisors, investors) are subject to vesting and lock-up terms set out in Part F §F.6 and enforced through on-chain vesting contracts.

### E.11 Mechanism for cancellation of the agreement

In addition to the right of withdrawal in Article 13 MiCA (see §E.13), purchase agreements are subject to ordinary contract-law remedies in case of breach, mistake, fraud or other recognised ground in the law applicable to the contract.

### E.12 Modification of the white paper

Any new fact or material inaccuracy in this white paper that is capable of affecting the assessment of OROG, and which arises or becomes known after publication and before the closing of the subscription period, shall result in a modified white paper being published and notified to the competent authority, per Article 12 MiCA. Holders of OROG who acquired prior to such modification shall have the right to withdraw within seven (7) working days of the publication of the modification.

### E.13 Right of withdrawal (Article 13 MiCA)

Retail holders who agree to purchase OROG directly from the offeror, or from a CASP placing OROG on behalf of the offeror, have the right to withdraw within fourteen (14) calendar days of agreeing to the purchase. Withdrawal does not require giving reasons and does not give rise to any cost (other than reasonable third-party transaction costs where unavoidable). Withdrawal is exercised by notice in writing to legal@orogen.network. The right of withdrawal does not apply where OROG has already been admitted to trading on a trading platform for crypto-assets prior to the purchase.

---

## Part F — Information about the crypto-assets

*Per Annex I, Part F, MiCA.*

### F.1 Type and functions

OROG is a **fungible** crypto-asset, *other than an asset-referenced token or an e-money token*, within the meaning of Article 3(1)(5) MiCA. OROG is **not** intended to be:
- a means of payment for goods and services outside the Orogen network;
- pegged to any fiat currency, basket of currencies, commodity, or other reference asset;
- electronic money under Directive 2009/110/EC;
- a financial instrument under MiFID II (Directive 2014/65/EU).

The functions of OROG within the network are:

1. **Burn-and-mint settlement medium.** OROG is the asset that the gateway burns at oracle spot to issue non-transferable USD-pegged compute credits ("CUC"). It is also the asset minted to operators at job finalisation.
2. **Operator stake.** Operators stake OROG as a slashing-eligible bond against good behaviour and tier-cap eligibility.
3. **Verification bond.** Validators, opML challengers and zkML provers stake OROG to participate in verification; their compensation is paid in OROG out of the per-job emission.
4. **Governance.** Holders may stake OROG for governance and, subject to active participation thresholds, receive the governance share of per-job emission.

### F.2 Initial allocation and total supply

The total initial supply of OROG at TGE shall be [TO FILL — exact integer number, e.g. 1,000,000,000 OROG]. The maximum supply is *not* hard-capped by a fixed schedule; instead, supply growth post-TGE is bounded by a pallet-enforced emission rule (see Part D §D.5 and Part F §F.4).

Initial allocation at TGE (percentages of initial supply):

| Bucket | Share | Vesting / lock-up |
|---|---|---|
| Investors (seed + Series A combined) | 12 % | 4-year cliff + 4-year linear vesting (i.e. nothing unlocks before month 48; thereafter pro-rata monthly for 48 months) |
| Team & advisors | 12 % | 4-year cliff + 4-year linear vesting |
| Treasury (Foundation runway) | 10 % | DAO-controlled; spend bounded to 18 months runway at any time |
| Ecosystem / grants / RFPs | 8 % | DAO-controlled, released over multiple years |
| Provider bootstrap allocation | 8 % | Released as part of operator emission over a 24-month ramp |
| Public / community / airdrop | 5 % | Unlocked at TGE |
| Strategic reserve | 5 % | DAO-controlled, 1-year cliff from TGE |
| Mining / emission pool | 40 % | Released as block / job emission, capped by the rule in Part D §D.5 |

### F.3 Issue date

The issue date of OROG is the date of TGE, as published not less than 20 working days in advance per Article 12 MiCA.

### F.4 Maximum supply / supply schedule

There is no fixed maximum supply. Post-TGE supply growth per epoch (each epoch ≈ 72 minutes / 360 blocks) is bounded by the following pallet-enforced rule:

```
target_epoch_mint = MIN(
    BOOTSTRAP_CAP_THIS_EPOCH,
    RollingBurn90d × elasticity_factor / epochs_per_90d,
    HARD_CEILING_PER_EPOCH               // 5 % of supply per year
)
target_epoch_mint = MAX(
    target_epoch_mint,
    FLOOR_PER_EPOCH                      // 0.5 % of supply per year
)
```

with `BOOTSTRAP_CAP` set at 8 % of supply per year in Year 1, ramping linearly to 4 % over Year 2, and the rule then governed by `RollingBurn90d × elasticity_factor` thereafter. `elasticity_factor` is governance-set within [0.8, 1.5]. Governance may amend parameters (elasticity factor, floor, ceiling, sampling rate, tier-stake floors) by on-chain vote subject to a 14-day timelock. Governance may **not** mint outside this rule. The rule structure itself can only be changed by a runtime upgrade with a 90-day timelock.

### F.5 Loss-of-value mechanism

OROG is *burned* (permanently removed from supply) by the gateway when compute credit is purchased. Burn is observable on chain. There is no other supply-destruction mechanism.

### F.6 Allocation to founders, team, advisors and pre-launch investors — detailed vesting

| Recipient class | Share of initial supply | Cliff | Linear vesting after cliff |
|---|---|---|---|
| Pre-launch investors (seed + Series A combined) | 12 % | 48 months from TGE | 48 months, monthly |
| Team & advisors | 12 % | 48 months from TGE | 48 months, monthly |
| Strategic reserve | 5 % | 12 months from TGE | Released by DAO vote |
| Provider bootstrap | 8 % | None | 24-month ramp as part of operator emission |
| Treasury | 10 % | None | DAO-controlled; bounded to 18 months runway at any time |
| Ecosystem / grants / RFPs | 8 % | None | DAO-controlled, multi-year |
| Public / community / airdrop | 5 % | None | Unlocked at TGE |

All vesting and lock-up arrangements are enforced by on-chain vesting contracts published in `pallet-suite` and audited (see Part H §H.6).

### F.7 Number of crypto-assets to be issued

[TO FILL — exact integer]; see §F.2.

### F.8 Description of the rights and obligations attached to OROG

See Part G.

### F.9 Specific arrangements concerning the offer

See Part E.

### F.10 Future offerings

The offeror may, after TGE, conduct further offerings of OROG drawn from the **Strategic reserve** bucket described in §F.6, or from such other buckets as may from time to time be unlocked by the DAO subject to the rule in §F.4. Any future offering shall be subject to a fresh white paper or a duly notified modification of this white paper, per Article 12 MiCA. Holders should not rely on any expectation that future offerings will or will not occur on any particular terms.

### F.11 Issuer retention

The offeror reserves no contractual right to retain OROG it has issued to a third party. Holdings of the offeror's group at TGE are limited to the buckets described in §F.6.

---

## Part G — Information on rights and obligations attached to the crypto-assets

*Per Annex I, Part G, MiCA.*

### G.1 Rights of the holder

A holder of OROG has:

(a) the right to transfer OROG on chain at any time, subject to (i) any vesting or lock-up applicable to the specific allocation they hold and (ii) any transfer-restriction imposed by an authorised CASP under applicable AML/CFT law;

(b) the right to **use** OROG to pay for compute on the Orogen network, by means of the burn-and-mint mechanism described in Part F §F.1;

(c) the right to **stake** OROG to operate, validate, challenge or prove on the network in any of the participant roles described in Part D §D.3, and to receive the corresponding share of per-job emission, subject to the slashing conditions described in §G.3;

(d) the right to **participate in governance**: to propose changes to the soft-parameter set listed in Part F §F.4 (within the timelock and quorum rules of the on-chain governance pallet), and to vote on such proposals in proportion to their stake;

(e) the right to obtain a current copy of this white paper free of charge from the offeror, and to receive any modified version pursuant to Article 12 MiCA;

(f) the right of withdrawal under Article 13 MiCA, as set out in Part E §E.13;

(g) the right to claim damages from the offeror for any breach of the obligations set out in Articles 6–14 MiCA, in accordance with Article 15 MiCA and the law applicable to the holder's contract with the offeror.

OROG does **not** confer:

- any right to receive dividends or other distributions from the offeror or any affiliate;
- any right to a fixed or variable interest payment;
- any equity, voting, or other ownership right in the offeror, the Orogen Foundation or any affiliate (governance under §(d) above operates at the protocol level, not at the level of any legal entity);
- any creditor claim against the offeror or any affiliate;
- any right of redemption against the offeror.

### G.2 Obligations of the holder

The holder of OROG is responsible for:

- complying with all laws applicable in their jurisdiction to the acquisition, holding, use, sale or transfer of crypto-assets, including tax law;
- the security of the private keys controlling their OROG; the offeror has no custody of holder OROG and cannot recover lost keys;
- compliance with all KYC/AML/CFT requirements imposed by CASPs they transact with;
- abstaining from market abuse and from any conduct constituting an offence under Title VI MiCA (insider dealing, unlawful disclosure of inside information, market manipulation).

### G.3 Slashing and forfeiture

Where OROG is staked in an operator, validator, challenger or prover role, it is subject to **slashing** (partial or total forfeiture) for behaviours defined in `pallet-slashing` and enumerated in the project's published Slashing Policy. Slashable events include: failure of attestation; provable cheating (e.g. divergent inference outputs vs replay); double-signing; sustained downtime beyond contractual SLA; provable misbehaviour in opML challenges. Slashed OROG is in part burned and in part redirected to honest participants per the Slashing Policy.

OROG held passively in a non-staking address is *not* subject to slashing.

### G.4 Modification of rights

Any modification of the rights described in this Part G that affects the rights of existing OROG holders shall be implemented only through a runtime upgrade adopted by on-chain governance with a timelock of not less than 90 days, allowing affected holders sufficient time to transfer or otherwise dispose of their OROG. The offeror commits to publishing a modified white paper, per Article 12 MiCA, in respect of any such modification before it takes effect.

### G.5 Restrictions on transferability

There are no protocol-level restrictions on the transferability of OROG, save for vesting / lock-up applicable to specific allocations under Part F §F.6. CASPs may impose transfer restrictions on holders pursuant to applicable AML/CFT law, sanctions law, or their own terms.

### G.6 Procedure for amendments

See §G.4.

### G.7 Complaints handling

Holders may submit complaints in writing to legal@orogen.network. The offeror shall acknowledge receipt within five (5) working days and shall provide a substantive response within thirty (30) calendar days. The offeror's complaints policy is published on orogen.network.

### G.8 Applicable law and competent courts

Subject to mandatory provisions of the law of the holder's habitual residence (in particular consumer-protection law), the relationship between the offeror and the holder shall be governed by the law of [TO FILL — e.g. France / Switzerland]. The competent courts shall be those of [TO FILL]. Nothing in this clause derogates from any consumer's right under Regulation (EU) No 1215/2012 (Brussels I bis) to bring proceedings in the courts of their Member State of residence.

---

## Part H — Information on the underlying technology

*Per Annex I, Part H, MiCA.*

### H.1 Distributed-ledger technology used

The Orogen network operates on a custom Substrate-based blockchain ("Orogen Chain") forked from `polkadot-sdk`. Key technical choices:

- **Block authoring:** AURA (Aleph Round-Robin) at TGE, with planned upgrade to BABE (slot-based VRF-driven authority selection) post-permissionless transition.
- **Finality:** GRANDPA (GHOST-based Recursive ANcestor Deriving Prefix Agreement).
- **EVM compatibility:** Frontier pallet enabling Ethereum JSON-RPC and EVM smart-contract execution.
- **Custom pallets:** `pallet-model-registry`, `pallet-operator-stake`, `pallet-job-market`, `pallet-yuma-consensus`, `pallet-bme` (burn-and-mint engine), `pallet-slashing`, `pallet-pouw-mint` (proof-of-useful-work mint), `pallet-attestation-registry`, `pallet-oracle-twap`, `pallet-nonce-vault`, `pallet-treasury-ext`.
- **Bridge (post-TGE):** A Snowbridge-forked Ethereum bridge enables wrapped OROG on Ethereum (`bridge-snowbridge-fork`). The bridge is **not** launch-blocking and is delivered after mainnet stability.
- **Indexer & explorer:** A Subsquid-based archival indexer (`chain-indexer`) feeds the public attestation explorer.

### H.2 Consensus mechanism and incentive structure

Block production is by a permissioned authority set at TGE (AURA), opening to permissionless validator participation post-Q3 2027 (BABE). Finality is GRANDPA, requiring 2/3 of the validator set. Inference verification is a **separate** layer (Yuma stake-weighted scoring in `pallet-yuma-consensus`) — block authoring and inference verification are decoupled.

Incentive structure:

| Activity | Compensation | Source |
|---|---|---|
| Operator (serves an inference job) | 75 % of per-job emission | `pallet-pouw-mint` on job finalisation |
| Validator (replays sample, scores) | Share of 15 % verification slice | `pallet-yuma-consensus` |
| opML challenger | Share of 15 % verification slice + slashed-stake recovery on successful challenge | `pallet-slashing` |
| zkML prover (for selected sub-heads) | Share of 15 % verification slice | `pallet-pouw-mint` |
| Protocol treasury | 5 % of per-job emission | `pallet-treasury-ext` |
| Governance stakers performing active security functions | 5 % of per-job emission, subject to ≥ 70 % participation threshold over 6 months | `pallet-yuma-consensus` |

The energy footprint of the consensus mechanism itself is that of a Substrate AURA/BABE + GRANDPA chain — orders of magnitude below Proof-of-Work chains. The energy footprint of the *application* (LLM inference on GPUs) is significant and is disclosed in Part J.

### H.3 Audit of the underlying technology

The protocol is the subject of:

(a) **multi-firm chain and protocol audits** scheduled for 2027 Q1–Q2 (see Part D §D.5). At the date of publication of this white paper, audit firms engaged are [TO FILL — e.g. SR Labs, Trail of Bits, OpenZeppelin, Sigma Prime]. Final audit reports will be published on orogen.network on completion;

(b) a **public bug-bounty programme** on Immunefi or equivalent, scaling to a maximum payout of [TO FILL — e.g. USD 1,000,000] for a critical chain-halting bug;

(c) a **continuous chaos-engineering harness** (`chaos-harness`) running scenarios against the testnet 24/7.

Pending publication of final audit results, holders should note that audits reduce — but do not eliminate — the risk of bugs.

### H.4 Smart-contract risk

Custom pallets are written in Rust and executed natively in the runtime. Where Ethereum-compatible smart-contracts are deployed on Orogen Chain via Frontier (e.g. the gateway burn contract), those contracts are written in Solidity, audited and version-pinned. Smart-contract upgradability follows a transparent proxy pattern under timelocked governance.

### H.5 Underlying technology — open source

The chain node (`chain-node`), pallet suite (`pallet-suite`), runtime (`runtime-mainnet`, `runtime-testnet`), tooling (`chain-tooling-rust`), worker daemons (`infer-worker-vllm`, `infer-worker-sglang`, `infer-worker-trtllm`, `infer-worker-llamacpp`), gateway and validator components, SDKs (Python, TypeScript) and frontends are released under permissive open-source licences (Apache-2.0 or MIT) and are publicly available at `github.com/orogen-network`.

### H.6 Software dependencies and inherited risk

The protocol depends on, and inherits the risk profile of, the following major upstream projects: Polkadot SDK (Substrate, Frontier), vLLM, SGLang, TensorRT-LLM, llama.cpp, NVIDIA confidential-compute firmware, Intel TDX firmware, AMD SEV-SNP firmware. A vulnerability disclosed in any of these may require an emergency runtime upgrade or temporary suspension of an affected operator tier.

---

## Part I — Information on risks

*Per Annex I, Part I, MiCA. Non-exhaustive. Holders should read this section in full.*

### I.1 Risks associated with the offer to the public

- **Total or partial loss.** Acquirers may lose all or part of the amount invested in OROG.
- **No regulatory approval.** This white paper has not been approved by any competent authority. Notification to the competent authority does not amount to approval of the offer or to a recommendation to acquire OROG.
- **Allocation risk.** Subscribers may receive less OROG than requested (or none) if the offer is oversubscribed or cancelled.
- **Price risk.** Where the offer price is set by auction or book-building, the realised price may differ materially from any indicative range.
- **Settlement risk.** Failure of a payment-service provider, banking partner or CASP intermediary may delay or prevent settlement.

### I.2 Risks of the offeror

- **Going-concern risk.** The offeror is a relatively new entity. It may face liquidity or solvency events independent of the underlying protocol. Failure of the offeror would not by itself destroy the Orogen protocol (which is governed by the on-chain DAO and stewarded by the Foundation; see Part B) but could materially impair its development.
- **Key-person risk.** The protocol's development depends on a small core team. Departure of key contributors may delay milestones in Part D §D.5.
- **Litigation risk.** As a publisher of open-source software operating in a novel regulatory area, the offeror may become the subject of civil or regulatory proceedings.
- **Counterparty risk.** Service providers (audit firms, banking partners, CASPs placing OROG, cloud providers) may fail or default.

### I.3 Risks of the crypto-assets

- **Volatility.** OROG is expected to be highly volatile. Past price performance (testnet only at the date of this white paper) is not indicative of future performance.
- **Illiquidity.** No assurance can be given that a sufficiently liquid secondary market for OROG will develop or be sustained.
- **Delisting / market-abuse suspension.** OROG may be removed from any CASP's trading platform at the CASP's discretion or by regulatory order.
- **Forks and chain reorganisations.** A contentious fork of Orogen Chain could result in two competing assets; the offeror does not guarantee that any specific fork will be the "canonical" OROG.
- **Custody risk.** Loss, theft or destruction of the holder's private keys results in loss of OROG. There is no recovery mechanism.

### I.4 Risks of the project's implementation

- **Failure to deliver.** The project may fail to deliver some or all of the milestones in Part D §D.5 on the planned schedule, or at all.
- **Insufficient customer demand.** Demand for verifiable LLM inference in the commodity market in 2026–2028 is unproven beyond a small segment. If customer revenue does not develop, the BME loop will operate at the floor and OROG inflation will exceed real burn for an extended period.
- **Insufficient operator participation.** If operators fail to register or maintain stake, network capacity and verification will be impaired.
- **Operator concentration.** Early operator participation may be highly concentrated. The DAO has tools (tier-stake floors, sampling-rate increase) to counter this, but cannot fully eliminate it.
- **Roadmap drift.** Phase-2 and Phase-3 capabilities (RL with verifiable task scoring, federated post-training, decentralised pretraining) are research-grade and may not materialise on the indicative timeline.

### I.5 Risks of the underlying technology

- **Consensus halt or fork.** A bug in the runtime, GRANDPA, AURA/BABE, or in upstream Polkadot SDK could halt block production or finality and require an emergency runtime upgrade.
- **Bridge risk.** The Ethereum bridge (post-TGE) is a high-value target. Bridge bugs or operator collusion could result in wrapped-OROG loss. The bridge is opt-in.
- **TEE compromise.** A break of NVIDIA H100/H200/B200 confidential-compute, Intel TDX or AMD SEV-SNP (e.g. silicon-level CVE) would compromise an entire vendor's operator base. The multi-vendor requirement at the permissionless transition reduces — but does not eliminate — this risk.
- **Oracle manipulation.** The BME loop depends on the OROG→USD oracle. A successful manipulation of one or more oracle sources could result in incorrect burn or mint quantities. Mitigations: TWAP, multi-source median, depth-weighting, governance circuit-breaker (Part D §D.3 verification layer 7).
- **Smart-contract bugs.** Auditing reduces but does not eliminate the risk of bugs.
- **Quantum computing.** A cryptographically-relevant quantum computer would compromise the chain's signature schemes (Sr25519/Ed25519 for substrate accounts, ECDSA secp256k1 for EVM). At the date of publication, the offeror does not consider this risk to be near-term; it is monitored and a post-quantum migration plan will be published as the threat materialises.
- **Software-dependency vulnerabilities.** See Part H §H.6.

### I.6 Risks specific to the regulatory environment

- **Reclassification.** A future change in EU or Member-State law or guidance — including (without limitation) classification of OROG as a financial instrument, an asset-referenced token, an e-money token or a security — could materially affect the legality of holding or transferring OROG, the obligations of the offeror, and the value of OROG.
- **CASP non-compliance.** OROG transactions may be impeded if a CASP through which a holder transacts loses authorisation or is subject to enforcement.
- **AML/CFT.** Holders may be subject to identification, due-diligence, source-of-funds and source-of-wealth requirements by CASPs and by the offeror.
- **Tax.** OROG may give rise to tax in the holder's jurisdiction (income tax, capital-gains tax, VAT on services where applicable). Holders should seek independent tax advice.
- **Sanctions.** Holders may be prohibited from transacting in OROG by sanctions law (EU consolidated list, OFAC, UK OFSI, others).

### I.7 Mitigation measures

The offeror's primary mitigations are: multi-firm audit, public bug-bounty, chaos-engineering harness, multi-vendor TEE requirement, on-chain enforced emission rule, governance timelocks, decoupling of block authoring from inference verification, content-addressing of weights and adapters, signed response receipts, validator replay over independent hardware. These mitigations reduce — but do not eliminate — the risks described above.

---

## Part J — Information on the principal adverse impacts on climate and other environment-related adverse impacts

*Per Article 6(1)(j) MiCA and the disclosures required under Commission Delegated Regulation (EU) 2025/422 (ESMA RTS on sustainability indicators), where applicable. Quantitative indicators are reported on a best-efforts basis pending publication of audited mainnet figures.*

### J.1 Scope

The "principal environmental impacts" of OROG comprise:

(a) the energy consumed and greenhouse-gas ("GHG") emissions arising from the operation of the Orogen Chain consensus protocol (block production, finality, indexer infrastructure);

(b) the energy consumed and GHG emissions arising from the *application layer* — LLM inference, validator replay, opML challenges, zkML proving — performed by independent operators on GPU hardware on the network.

For full disclosure, the application-layer footprint, which is materially larger than the consensus-layer footprint, is included even though Annex I §J of MiCA primarily targets consensus-layer impact.

### J.2 Consensus-layer indicators (Orogen Chain)

| Indicator | Value | Notes |
|---|---|---|
| Consensus mechanism | AURA + GRANDPA at TGE; BABE + GRANDPA post-permissionless transition | Proof-of-Stake / Proof-of-Authority style; **not** Proof-of-Work |
| Annualised electricity consumption — consensus layer (estimated) | [TO FILL — kWh/yr] | Sum of validator-node power × hours active; estimate based on testnet measurements scaled to projected mainnet validator count |
| Renewable-energy share | [TO FILL — %] | Self-reported by validators in the operator-registration manifest; verified by [TO FILL — energy-attestation provider or method] |
| GHG intensity — consensus layer (Scope 2, location-based) | [TO FILL — kg CO₂e / yr] | Computed using EU average grid-intensity factors |
| Number of validator nodes (testnet, date of publication) | [TO FILL] |  |
| Estimated number of validator nodes at mainnet | [TO FILL] |  |

### J.3 Application-layer indicators (GPU inference)

| Indicator | Value | Notes |
|---|---|---|
| Hardware base (testnet) | [TO FILL — H100 / A100 / consumer GPUs by count] |  |
| Annualised electricity consumption — application layer (estimated) | [TO FILL — kWh/yr] | Operator-reported via TEE-attested telemetry; aggregated by `chain-indexer` |
| Energy per million tokens of inference (median) | [TO FILL — kWh / 1M tokens] | Reported per hardware tier |
| Renewable-energy share (application layer) | [TO FILL — %] | Operator-self-reported, with TEE-attested geo-location; attestation method as in §J.2 |
| GHG intensity — application layer (Scope 2, location-based) | [TO FILL — kg CO₂e / yr] |  |

### J.4 Methodology

Indicators in §J.2 and §J.3 are derived from on-chain heartbeat data (`pallet-attestation-registry`, `heartbeat-svc`) and operator manifests, aggregated via `chain-indexer` and published on the public subsidy-and-sustainability dashboard at orogen.network/dashboard. Methodology follows the indicators set out in Annex III to Commission Delegated Regulation (EU) 2025/422, where applicable to a Proof-of-Stake protocol. Renewable-energy claims by operators are verified on a sampling basis by an independent third party [TO FILL — name, frequency of verification].

### J.5 Mitigation actions

The offeror, the Foundation and the DAO commit to the following actions to mitigate the environmental impact of the network:

- prioritising operator participation by parties with verifiable renewable-energy sourcing in tier-cap allocations, where feasible without compromising network neutrality;
- publishing on each anniversary of TGE an updated environmental report against the indicators in this Part J, audited where audit services are reasonably available;
- supporting research on energy-efficient inference (quantisation, batching, deterministic kernels, hardware tiering) and incorporating findings into the operator software stack;
- making the public sustainability dashboard available free of charge to regulators, customers and the public.

### J.6 Limitations

Quantitative indicators in this Part J are best-efforts estimates derived from a pre-mainnet network. Material revisions are expected after TGE as audited data becomes available. Holders should not treat the figures in this Part J as audited financial-statement equivalents.

---

## Annexes

### Annex 1 — Glossary

- **AURA.** Aleph Round-Robin block-authoring algorithm used by Substrate-based chains pre-permissionless.
- **BABE.** Slot-based VRF-driven block-authoring algorithm used by Substrate-based chains in permissionless mode.
- **BME.** Burn-and-Mint Equilibrium — a token-economic pattern in which a token is burned by the customer and minted to the provider in equal $-denominated quantity at oracle spot.
- **CASP.** Crypto-Asset Service Provider — an entity authorised under MiCA to provide crypto-asset services.
- **CUC.** Compute Unit Credit — a non-transferable USD-pegged ephemeral credit issued by the gateway when OROG is burned.
- **Frontier.** Substrate pallet providing Ethereum-JSON-RPC and EVM execution compatibility.
- **GRANDPA.** GHOST-based Recursive ANcestor Deriving Prefix Agreement — Substrate finality gadget.
- **LoRA.** Low-Rank Adaptation — a parameter-efficient fine-tuning technique for transformer models.
- **opML.** Optimistic ML — a verification paradigm in which inference outputs are accepted by default and may be challenged within a window.
- **Pallet.** A Substrate runtime module.
- **PoUW.** Proof of Useful Work.
- **SEV-SNP.** AMD Secure Encrypted Virtualisation – Secure Nested Paging.
- **TDX.** Intel Trust Domain Extensions.
- **TEE.** Trusted Execution Environment.
- **TGE.** Token Generation Event — the first time OROG enters circulation.
- **TWAP.** Time-Weighted Average Price.
- **Yuma.** Stake-weighted scoring mechanism (originating in Bittensor) used to compute consensus on inference quality.
- **zkML.** Zero-Knowledge Machine Learning — cryptographic proof of correctness of an inference computation.

### Annex 2 — References

- Regulation (EU) 2023/1114 of the European Parliament and of the Council of 31 May 2023 on markets in crypto-assets (MiCA).
- Commission Delegated Regulation (EU) 2025/422 supplementing Regulation (EU) 2023/1114 with regard to regulatory technical standards on sustainability indicators (where applicable to a Proof-of-Stake protocol).
- Project research dossier, `github.com/orogen-network`.
- Project technical white paper (separate document), `orogen.network/downloads/orogen-whitepaper.pdf`.

### Annex 3 — Where to obtain a copy of this white paper

- Online: `orogen.network/downloads/orogen-mica-whitepaper.pdf`
- By email request to `legal@orogen.network`
- Free of charge in machine-readable format on request

---

*End of crypto-asset white paper.*

[TO FILL — signature block: name(s), function(s), signature(s) of the member(s) of the management body of the offeror.]
