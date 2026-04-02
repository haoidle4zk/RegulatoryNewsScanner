# Regulatory News Scanner ⚖️

### Quick pitch

Regulation is crypto's biggest unknown. One policy paper from the SEC, one ban from a major economy — billions move. This contract scores the regulatory climate, on-chain.

---

### What does it do?

Reads market data → AI assesses regulatory environment based on sentiment → validators agree → result on-chain.

**Regulatory sentiment:** VERY_HOSTILE · HOSTILE · NEUTRAL · FRIENDLY · VERY_FRIENDLY

**Policy types:** BAN · RESTRICTION · FRAMEWORK · APPROVAL · ADOPTION

### Sample result

```json
{
  "reg_sentiment": "NEUTRAL",
  "key_region": "United States",
  "policy_type": "FRAMEWORK",
  "summary": "Market sentiment suggests regulatory uncertainty remains a key driver."
}
```

### Setup (2 minutes)

GenLayer Studio → paste contract → `param` = `test` → deploy → `scan_regulations`

### Use cases I'm excited about

1. **Auto-compliance alerts** for DAOs
2. **Geographic risk scoring** across jurisdictions
3. **Trading signal** — regulatory sentiment as a leading indicator

### Tech details

~70 lines of Python on GenLayer. Uses `gl.nondet.web.render` + `gl.nondet.exec_prompt` + `gl.eq_principle.strict_eq`.

MIT License | GenLayer Testnet Bradbury
